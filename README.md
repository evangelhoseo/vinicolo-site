# Vinícolo — site institucional e loja

Site da **Vinícolo** (vinhos). Cliente da Agência Foco Digital.

- **No ar (revisão):** https://evangelhoseo.github.io/vinicolo-site/
- **Hospedagem:** GitHub Pages, branch `main`, pasta raiz. Push na `main` republica em ~1 min.
- **Domínio próprio:** ainda não ligado (o JSON-LD já cita `vinicolo.com.br`).

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
build.py              ← sincroniza index.html e valida o site
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

## Pegadinhas

- **`.nojekyll` é obrigatório.** O Pages roda Jekyll por padrão e ignora pastas que começam com
  `_` — sem o arquivo, a `_ds/` some e o site perde todo o estilo e os botões. O `build.py` checa.
- **SEO está dentro do `<helmet>`**, que só é aplicado depois do JS carregar. Para indexação de
  verdade (domínio próprio), mover title/description/OG/JSON-LD para o `<head>` estático, como foi
  feito na Danielly.
- **Reexportar do Claude Design sobrescreve ajustes manuais** (contato, links de compra no
  `data.js`, fotos otimizadas). Comparar com `git diff` antes de commitar um export novo.
- A pasta `uploads/` do export original (fotos brutas, ~45 MB) não é referenciada por nenhuma
  página e ficou fora do repo de propósito.
