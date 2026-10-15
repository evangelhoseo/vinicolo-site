"""Build do site da Vinícolo (export dc-runtime publicado no GitHub Pages).

Não há etapa de compilação: o Pages serve os arquivos do repo como estão. O build:

  1. grava o SEO no <head> estático de cada página, entre <!-- seo:inicio --> e
     <!-- seo:fim --> (title, description, canonical, Open Graph, JSON-LD, favicon) e põe
     lang="pt-BR" no <html>. Title/description/JSON-LD saem do <helmet> da própria página —
     o <helmet> só é aplicado depois do JS carregar, então quem não roda JS não o enxerga;
  2. index.html = cópia exata de Home.dc.html (a raiz do domínio precisa servir a Home);
  3. gera robots.txt, sitemap.xml e, com DOMINIO_LIGADO, o CNAME;
  4. valida: .nojekyll presente (sem ele o Pages apaga a pasta _ds/ e o site perde todo o
     estilo), toda referência local aponta para um arquivo que existe e todo produto do
     data.js tem foto.

Uso:
  python build.py           # gera e valida
  python build.py --check   # só valida, sem escrever nada (é o que o Actions roda)
"""
import html
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
HOME = RAIZ / "Home.dc.html"
INDEX = RAIZ / "index.html"

DOMINIO = "https://vinicolo.com.br/"
# Só passe para True depois que o DNS do domínio apontar para o GitHub Pages (ver README):
# o CNAME faz o Pages redirecionar o endereço github.io para o domínio.
DOMINIO_LIGADO = False

OG_IMAGEM = "og-image.jpg"
FAVICON = "assets/logo-symbol-positiva.svg"

# arquivo -> (caminho no domínio, vai para o sitemap, title/description se o helmet for template)
PAGINAS = {
    "Home.dc.html": ("", True, None),
    "Loja.dc.html": ("Loja.dc.html", True, None),
    "Eventos.dc.html": ("Eventos.dc.html", True, None),
    "Blog.dc.html": ("Blog.dc.html", True, None),
    "Sobre.dc.html": ("Sobre.dc.html", True, None),
    "Contato.dc.html": ("Contato.dc.html", True, None),
    # Detalhe escolhido pelo #hash: para o Google é uma URL só, então fica fora do sitemap.
    "Evento.dc.html": ("Evento.dc.html", False, ("Evento — Vinícolo",
                       "Degustações, jantares harmonizados e eventos da Vinícolo em Cordeiro, RJ.")),
    "Post.dc.html": ("Post.dc.html", False, ("Blog — Vinícolo",
                     "Notas de degustação, harmonização e bastidores da Vinícolo, escritos pelo Guilherme.")),
}

REF_HTML = re.compile(r'''(?:src|href)=["']([^"'#?]+)''')
REF_DATA = re.compile(r'''["']((?:\./)?(?:assets|_ds)/[^"'?#]+)["']''')
BLOCO_SEO = re.compile(r"\n?<!-- seo:inicio -->.*?<!-- seo:fim -->", re.S)


def helmet(texto):
    m = re.search(r"<helmet>(.*?)</helmet>", texto, re.S)
    return m.group(1) if m else ""


def bloco_seo(arquivo, texto):
    caminho, _, reserva = PAGINAS[arquivo]
    h = helmet(texto)
    titulo = re.search(r"<title>(.*?)</title>", h, re.S).group(1).strip()
    descricao = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    if "{{" in titulo or "{{" in descricao:
        titulo, descricao = reserva
    url = DOMINIO + caminho
    e = lambda s: html.escape(s, quote=True)
    linhas = [
        "<!-- seo:inicio -->",
        f"<title>{e(titulo)}</title>",
        f'<meta name="description" content="{e(descricao)}">',
        f'<link rel="canonical" href="{url}">',
        f'<link rel="icon" href="{FAVICON}" type="image/svg+xml">',
        '<meta property="og:type" content="website">',
        '<meta property="og:locale" content="pt_BR">',
        '<meta property="og:site_name" content="Vinícolo">',
        f'<meta property="og:title" content="{e(titulo)}">',
        f'<meta property="og:description" content="{e(descricao)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{DOMINIO}{OG_IMAGEM}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
    ]
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        linhas.append('<script type="application/ld+json">'
                      + json.dumps(json.loads(ld), ensure_ascii=False) + "</script>")
    linhas.append("<!-- seo:fim -->")
    return "\n".join(linhas)


def pagina_com_seo(arquivo):
    texto = (RAIZ / arquivo).read_text(encoding="utf-8")
    texto = BLOCO_SEO.sub("", texto)
    texto = re.sub(r"<html[^>]*>", '<html lang="pt-BR">', texto, count=1)
    viewport = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    assert viewport in texto, f"{arquivo}: meta viewport não encontrada no <head>"
    return texto.replace(viewport, viewport + "\n" + bloco_seo(arquivo, texto), 1)


def arquivos_gerados():
    saida = {arq: pagina_com_seo(arq) for arq in PAGINAS}
    saida["index.html"] = saida["Home.dc.html"]
    saida["robots.txt"] = f"User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}sitemap.xml\n"
    urls = "".join(f"  <url><loc>{DOMINIO}{c}</loc></url>\n"
                   for c, no_sitemap, _ in PAGINAS.values() if no_sitemap)
    saida["sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                            f"{urls}</urlset>\n")
    if DOMINIO_LIGADO:
        saida["CNAME"] = DOMINIO.split("//")[1].rstrip("/") + "\n"
    return saida


def referencias(arquivo: Path, padrao):
    texto = arquivo.read_text(encoding="utf-8")
    for alvo in padrao.findall(texto):
        if "{{" in alvo or re.match(r"^[a-z]+:", alvo) or alvo.startswith("//"):
            continue  # template do runtime, URL externa, mailto:, tel:
        yield alvo


def validar():
    erros = []
    if not (RAIZ / ".nojekyll").exists():
        erros.append(".nojekyll ausente — o Pages vai ignorar a pasta _ds/")
    if not (RAIZ / OG_IMAGEM).exists():
        erros.append(f"{OG_IMAGEM} ausente — é a imagem de compartilhamento de todas as páginas")
    if (RAIZ / "CNAME").exists() and not DOMINIO_LIGADO:
        erros.append("CNAME existe mas DOMINIO_LIGADO = False no build.py")

    fontes = sorted(RAIZ.glob("*.dc.html")) + [INDEX]
    for arquivo in fontes:
        for alvo in referencias(arquivo, REF_HTML):
            if not (RAIZ / alvo).exists():
                erros.append(f"{arquivo.name}: referência quebrada -> {alvo}")
    for alvo in referencias(RAIZ / "data.js", REF_DATA):
        if not (RAIZ / alvo).exists():
            erros.append(f"data.js: referência quebrada -> {alvo}")

    # A Loja monta a foto como assets/<products|accessories>/<id>.webp (ver imgFolder no
    # Loja.dc.html), então produto novo no data.js sem a foto correspondente vira imagem quebrada.
    produtos = (RAIZ / "data.js").read_text(encoding="utf-8").split("export const", 2)[1]
    for pid in re.findall(r'"id":\s*"([^"]+)"', produtos):
        pasta = "accessories" if pid.startswith("acc") else "products"
        if not (RAIZ / "assets" / pasta / f"{pid}.webp").exists():
            erros.append(f"data.js: produto {pid} sem foto em assets/{pasta}/{pid}.webp")
    return erros


def main():
    so_checar = "--check" in sys.argv
    erros = []

    for nome, conteudo in arquivos_gerados().items():
        destino = RAIZ / nome
        atual = destino.read_text(encoding="utf-8") if destino.exists() else None
        if atual == conteudo:
            continue
        if so_checar:
            erros.append(f"{nome} desatualizado — rode `python build.py` e commite")
        else:
            destino.write_text(conteudo, encoding="utf-8", newline="\n")
            print(f"{nome} atualizado")

    erros += validar()
    if erros:
        print("\n".join(f"ERRO: {e}" for e in erros))
        sys.exit(1)
    print("OK: SEO, index.html, robots/sitemap em dia; nenhuma referência local quebrada")


if __name__ == "__main__":
    main()
