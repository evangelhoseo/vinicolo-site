# Vinícolo — site institucional e loja

Site da **Vinícolo** (vinhos). Cliente da Agência Foco Digital.

- **No ar (revisão):** https://evangelhoseo.github.io/vinicolo-site/
- **Hospedagem:** GitHub Pages, branch `main`, pasta raiz. Push na `main` republica em ~1 min.
- **Domínio próprio:** `vinicolo.com.br` — em migração (ver "Ligar o domínio"). Canonical, OG e
  sitemap já apontam para ele.

## Como funciona

Export **dc-runtime** do Claude Design — mesmo padrão de `danielly-curione-site` e
`tarja-verde-aventuras-site`. É 100% client-side: `support.js` interpreta o `<x-dc>` de cada
página e carrega React/Babel do unpkg em runtime. Não há etapa de compilação.

```
Home.dc.html          ← páginas (editar à mão)
Loja.dc.html  Eventos.dc.html  Evento.dc.html  Blog.dc.html  Post.dc.html
Sobre.dc.html  Contato.dc.html
Header / Footer / AgeGate / WhatsAppButton .dc.html  ← componentes importados pelas páginas
data.js               ← catálogo (PRODUCTS), EVENTOS e POSTS
assets/products/      ← foto de cada vinho: <id>.webp
assets/accessories/   ← foto de cada acessório: acc*.webp
_ds/                  ← design system exportado (tokens CSS + _ds_bundle.js) — não editar
support.js image-slot.js ← runtime dc — não editar
index.html            ← GERADO: cópia exata de Home.dc.html
robots.txt sitemap.xml ← GERADOS
og-image.jpg          ← imagem de compartilhamento (1200×630), usada por todas as páginas
build.py              ← grava o SEO no <head>, gera index/robots/sitemap/CNAME e valida
.nojekyll             ← obrigatório (ver "Pegadinhas")
```

Os links internos apontam direto para os arquivos (`Loja.dc.html`, `Sobre.dc.html`…), nunca para
`/`. Por isso a raiz só serve algo porque `index.html` é cópia da Home.

## Fluxo de alteração

1. Editar o `.dc.html` / `data.js` / `assets/` necessários
2. `python build.py` — copia a Home para `index.html` e valida (sai com erro se algo quebrou)
3. Conferir no preview local
4. Commit direto na `main` e push → o Pages republica; o Actions **Checar site** roda o
   `build.py --check` no mesmo commit

Produto novo na loja = entrada em `PRODUCTS` no `data.js` **+** a foto `assets/products/<id>.webp`
(ou `assets/accessories/` se o id começar com `acc`). O `build.py` acusa foto faltando.

## Preview local

Registrado no `.claude/launch.json` do projeto `Novos Sites` como **`vinicolo`** (porta 8094).
Manualmente:

```bash
python -m http.server 8094 --directory .
```

Precisa ser servido por HTTP — abrir o arquivo direto (`file://`) não funciona.

## Versionamento e rollback

- Todo deploy é um commit na `main`; o histórico do git é o histórico do site.
- Antes de uma rodada grande de mudanças, marcar o estado atual com tag:
  `git tag pre-<assunto>-AAAA-MM-DD && git push origin --tags`
- Voltar o site para um ponto anterior **sem reescrever histórico**:

  ```bash
  git revert --no-edit <commit>..HEAD
  git push
  ```

  Ou, para restaurar tudo a partir de uma tag: `git checkout <tag> -- . && git commit -m "rollback para <tag>" && git push`.
- Nunca `push --force` na `main`.

Tags existentes: `v2026-08-07` — estado publicado antes de o repo ganhar `build.py`/Actions.

## Ligar o domínio vinicolo.com.br

Domínio, DNS e **e-mail** (`contato@vinicolo.com.br`) estão na **GoDaddy** (nameservers
`ns17/ns18.domaincontrol.com`). Até a virada, o domínio serve um site de uma página só feito no
construtor da GoDaddy — sem outras URLs, então não há redirecionamento a fazer.

**A ordem importa: primeiro o DNS, depois o CNAME no repo.** Na ordem inversa o Pages passa a
redirecionar o endereço github.io para um domínio que ainda mostra o site antigo.

1. **GoDaddy → Meus produtos → DNS de vinicolo.com.br.** Mexer **só** nestes registros:
   - Apagar os dois `A @` atuais (`13.248.243.5` e `76.223.105.230` — são do construtor de sites).
   - Criar quatro `A @`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
   - `CNAME www` → `evangelhoseo.github.io` (hoje aponta para `@`).
   - **Não tocar** nos `MX` (`smtp`/`mailstore1.secureserver.net`) nem no `TXT` do SPF: são o
     e-mail.
   - Se o construtor de sites da GoDaddy estiver "conectado" ao domínio, desconectar/despublicar,
     senão ele recria os registros A.
2. Esperar `nslookup vinicolo.com.br 8.8.8.8` devolver os IPs `185.199.x.153` (TTL é 10 min).
3. No `build.py`: `DOMINIO_LIGADO = True`; `python build.py` (cria o `CNAME`); commit e push.
4. `gh api -X PUT repos/evangelhoseo/vinicolo-site/pages -f cname=vinicolo.com.br`
5. Quando o certificado sair (minutos até ~1 h):
   `gh api -X PUT repos/evangelhoseo/vinicolo-site/pages -F https_enforced=true`
6. Search Console: adicionar a propriedade e enviar `https://vinicolo.com.br/sitemap.xml`.

**Janela de HTTPS:** o site da GoDaddy manda `Strict-Transport-Security` com `includeSubDomains`,
então quem já visitou o site antigo só aceita HTTPS. Entre a troca do DNS e a emissão do
certificado do GitHub esse visitante vê erro de certificado. Fazer a virada em horário de pouco
movimento.

## Pegadinhas

- **`.nojekyll` é obrigatório.** O Pages roda Jekyll por padrão e ignora pastas que começam com
  `_` — sem o arquivo, a `_ds/` some e o site perde todo o estilo e os botões. O `build.py` checa.
- **SEO no `<head>` estático é gerado.** O `<helmet>` só é aplicado depois do JS carregar, então o
  `build.py` copia title/description/JSON-LD do `<helmet>` de cada página para o bloco
  `<!-- seo:inicio -->…<!-- seo:fim -->`. Para mudar o SEO, edite o `<helmet>` e rode o build —
  nunca o bloco gerado.
- **URLs terminam em `.dc.html`** (`/Loja.dc.html`). Feio, mas funciona; mudar depois de indexado
  exige redirecionamento, que o Pages não faz.
- **Evento e Post escolhem o item pelo `#hash`**, que o Google ignora: para ele são uma URL só
  cada. Ficam fora do sitemap com title genérico.
- **Reexportar do Claude Design sobrescreve ajustes manuais** (contato, links de compra no
  `data.js`, fotos otimizadas). Comparar com `git diff` antes de commitar um export novo.
- A pasta `uploads/` do export original (fotos brutas, ~45 MB) não é referenciada por nenhuma
  página e ficou fora do repo de propósito.
