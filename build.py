"""Build do site da Vinícolo (export dc-runtime publicado no GitHub Pages).

Não há etapa de compilação: o Pages serve os arquivos do repo como estão.
O build só faz o que, feito à mão, já deu errado:

  1. index.html = cópia exata de Home.dc.html (a raiz do domínio precisa servir a Home);
  2. .nojekyll presente (sem ele o Pages apaga a pasta _ds/ e o site perde todo o estilo);
  3. toda referência local (src/href em *.dc.html e caminhos assets/ no data.js) aponta
     para um arquivo que existe.

Uso:
  python build.py           # sincroniza index.html e valida
  python build.py --check   # só valida, sem escrever nada (é o que o Actions roda)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
HOME = RAIZ / "Home.dc.html"
INDEX = RAIZ / "index.html"

REF_HTML = re.compile(r'''(?:src|href)=["']([^"'#?]+)''')
REF_DATA = re.compile(r'''["']((?:\./)?(?:assets|_ds)/[^"'?#]+)["']''')


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
    home = HOME.read_bytes()
    erros = []

    if INDEX.read_bytes() != home:
        if so_checar:
            erros.append("index.html difere de Home.dc.html — rode `python build.py` e commite")
        else:
            INDEX.write_bytes(home)
            print("index.html atualizado a partir de Home.dc.html")

    erros += validar()
    if erros:
        print("\n".join(f"ERRO: {e}" for e in erros))
        sys.exit(1)
    print("OK: index.html em dia, .nojekyll presente, nenhuma referência local quebrada")


if __name__ == "__main__":
    main()
