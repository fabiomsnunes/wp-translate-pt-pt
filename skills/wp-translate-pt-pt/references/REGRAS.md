# Regras de tradução pt-PT (WordPress)

> Fonte: [Guia de tradutores pt_PT](https://pt.wordpress.org/traducoes/guia-de-tradutores-portugues-de-portugal-pt_pt/)
> Glossário oficial: [`glossario-pt-pt.csv`](./glossario-pt-pt.csv) (fonte única de verdade, descarregado de translate.wordpress.org — não editar à mão; para atualizar, substituir o ficheiro).

## Normas gerais (processo)
- Fontes de referência, por ordem: o **glossário**, a **tabela consolidada** da Comunidade (pesquisa de termos no site oficial) e a ferramenta de **consistência** entre projetos.
- **Em caso de dúvida, não traduzir.** Expor a dúvida primeiro no Palheta (blog de discussão da Comunidade) ou no canal `#traducao` do Slack (`wp-portugal.slack.com`). Aqui isto traduz-se no `⚠️`: marco e tu decides/discutes.
- **Nunca usar tradução automática** (Google Translate). Sugestões só são aprovadas se coerentes com o guia, o glossário e a tabela consolidada.
- **Não decidir alterações a traduções existentes** unilateralmente. Mudar um termo já consolidado exige debate e consenso nos canais da Comunidade — avisar o grupo com os motivos.
- Submissão oficial em `https://translate.wordpress.org/locale/pt`.

## Ortografia
- **Pré-AO90** (português anterior ao Acordo Ortográfico de 1990): `activar`, `acção`, `directório`, `selecção`, `actual`, `óptimo`, `contacto`, `excepção`.
- Traduzir **sempre em pré-AO90**. A conversão para AO90 é automática e unidirecional (gerada a partir do pré-AO90 via Lince), pelo que não se traduz manualmente em AO90; quem quiser AO90 ativa-o nas opções do painel ou instala o plugin **PT AO90** da Comunidade (que usa o pré-AO90 como alternativa quando ainda não há tradução AO90).
- Acrónimos: **sem pontos e sem plural** — `PDF`, `URL`, `ID`, `HTML` (nunca `URLs`, `PDFs`, `PDF's`).

## Formalidade e tratamento
- **Infinitivo impessoal** sempre que possível: "Guardar alterações", "Eliminar artigo", "Iniciar sessão" — não "Guarde", "Elimine". (Infinitivo impessoal: descreve a ação sem a vincular a tempo, modo ou pessoa.)
- Quando é mesmo preciso dirigir-se ao utilizador, usar verbo na 3.ª pessoa do singular, registo formal — **sem** "você": "Tem a certeza de que pretende…", "Não tem permissão para…".
- **Eliminar referências de género** (gestão mais simples, tradução mais inclusiva). Preferir formas neutras a "bem-vindo/a". Quando inevitável, seguir o glossário (ex.: `Mine` → "Meu", invariável).

## Maiúsculas
- Maiúscula só na **primeira palavra** ao referir elementos do sistema (não capitalizar cada palavra ao estilo inglês).
  - EN: "Save Draft" → PT: "Guardar rascunho".
- Manter maiúscula em nomes próprios de funcionalidades do glossário: `Painel`, `Personalizador`, `Editor do site`.

## Advérbios em -mente
- Usar com parcimónia (no máximo um por parágrafo).
- **Nunca acentuados**: `rapidamente`, `automaticamente` (não `rápidamente`).

## Pontuação e espaços (convenção tipográfica geral — não consta do guia)
- Sem espaço antes de `:` `;` `!` `?`.
- Reticências: usar o símbolo `…`, não três pontos seguidos (`...`).
- Aspas: preferir as do original quando coerentes; nas strings de UI manter o que o contexto exigir.

## Estilo
- **Tradução contextual > literal.** Traduzir o sentido, não palavra a palavra.
- Traduzir o máximo possível para português; só manter em inglês os termos marcados no glossário.
- Em polissemia (uma palavra EN, vários sentidos), escolher o termo PT certo para cada contexto (ver no glossário casos como `caption`/`captions`/`subtitles`, `restore`, `label`, `tag`).

## Termos que NÃO se traduzem (mantêm-se em inglês)
`plugin`, `widget`, `hook`, `loop`, `shortcode`, `feeds`, `malware` (masc.), `pingback` (masc.), `trackback` (masc.), `sitemap`, `locale`, `slug` (masc.), `frame`, `charset`, `collation`, `gateway` (fem.), `banner`, `design`, `layout`, `online`/`offline` (sem hífen), `spam` (minúsculas).

## Decisões frequentes (atalhos do glossário)
| EN | pt-PT |
|---|---|
| password | senha (não "palavra-passe") |
| email | email (sem hífen) |
| settings | opções |
| post (noun) | artigo |
| post type | tipo de conteúdo |
| Dashboard | Painel |
| log in / log out | iniciar sessão / sair |
| save | guardar |
| delete | eliminar |
| trash | lixo |
| enable / disable | activar / desactivar |
| featured image | imagem de destaque |
| link | ligação |
| permalink | ligação permanente |
| website / site | site (masc.) |
