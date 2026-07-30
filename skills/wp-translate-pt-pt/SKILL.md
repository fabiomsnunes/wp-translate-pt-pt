---
name: wp-translate-pt-pt
description: >-
  Traduz strings de interface do WordPress (core, plugins, temas) de inglês para
  português de Portugal (pt-PT), seguindo o glossário oficial da Comunidade e o
  Guia de Tradutores pt_PT. Usa esta skill SEMPRE que o utilizador entregar um
  ficheiro .po/.pot exportado do translate.wordpress.org (GlotPress) para
  preencher, colar ou despejar strings em inglês para traduzir, pedir a tradução
  pt-PT de termos de UI, falar em traduzir o WordPress / um plugin / um tema para
  português, ou pedir para rever/validar traduções pt-PT — mesmo que não diga
  explicitamente "glossário" ou "pt-PT". As duas entradas típicas são um ficheiro
  .po do GlotPress (com msgstr vazios) ou strings soltas que o utilizador cola no
  chat. NÃO usar para traduzir conteúdo editorial longo (artigos, posts) nem para
  português do Brasil.
---

# Tradução pt-PT (WordPress)

Traduzir strings de interface EN → pt-PT com a qualidade e consistência que a
Comunidade Portuguesa de WordPress exige. O objetivo não é "uma tradução
qualquer", é a tradução que um validador do translate.wordpress.org aprovaria à
primeira: coerente com o glossário consolidado, na norma pré-AO90, formal e sem
marcas de género.

## Referências (fonte única de verdade)

Ambos vivem na pasta desta skill, em `references/`. São a fonte canónica —
atualizam-se substituindo o ficheiro, não editando à mão.

- **Glossário**: `references/glossario-pt-pt.csv`
  Colunas: `en,pt,pos,description`. Descarregado de translate.wordpress.org.
- **Regras**: `references/REGRAS.md`
  Interpretação do [Guia de Tradutores pt_PT](https://pt.wordpress.org/traducoes/guia-de-tradutores-portugues-de-portugal-pt_pt/).

### Ao arrancar: confirmar que o glossário está disponível e fresco

**No início de cada sessão de tradução, antes de fixar termos**, corre o verificador
de estado (a partir da pasta da skill):

```bash
scripts/check-glossary.sh
```

Imprime uma única linha. Age conforme o resultado:

- **`MISSING`** — o CSV não existe. **Pergunta ao utilizador** se podes descarregar
  o glossário e, se ele aceitar, corre `scripts/update-glossary.sh`. Não traduzas
  sem glossário.
- **`STALE <dias>`** (mais de 30 dias desde o último update, ou sem carimbo de data)
  — **pergunta** se quer atualizar antes de continuar. Se sim, corre
  `scripts/update-glossary.sh`; se preferir avançar com o snapshot atual, continua
  sem atualizar.
- **`OK <dias>`** — está fresco. Continua sem perguntar nada.

```bash
# Atualizar (sem argumentos: usa o endpoint de exportação oficial)
scripts/update-glossary.sh
```

O `update-glossary.sh` descarrega o CSV consolidado e grava a data em
`references/.glossary-updated`, que é o que o verificador lê. Faz esta verificação
uma vez por sessão, não a cada string.

**Consulta o glossário por pesquisa, não de cor.** Antes de fixar um termo,
confirma no CSV — há polissemia tratada (ex.: `caption`/`captions`/`subtitles`,
`restore`, `label`, `tag`, `excerpt`). O CSV está em `references/`, ao lado desta
SKILL.md; a partir da pasta da skill:

```bash
grep -i 'palavra' references/glossario-pt-pt.csv
```

Se a primeira sessão de tradução já leu o CSV inteiro, podes trabalhar de memória,
mas **valida sempre os termos não óbvios** — a consistência com o consolidado é o
que distingue uma tradução aceite de uma rejeitada.

## As regras que mais importam

Detalhe completo em `REGRAS.md`; o essencial para não errar:

- **Pré-AO90 sempre**: `activar`, `acção`, `directório`, `selecção`, `óptimo`,
  `contacto`, `excepção`. A conversão para AO90 é automática e unidirecional — não
  traduzas em AO90.
- **Infinitivo impessoal**: "Guardar alterações", "Eliminar artigo", não "Guarde"
  / "Elimine". É a forma neutra que descreve a ação sem a vincular a pessoa.
- **Sem marcas de género**: preferir formas neutras a "bem-vindo/a". Quando é mesmo
  preciso dirigir-se ao utilizador, 3.ª pessoa formal **sem** "você": "Não tem
  permissão para…".
- **Maiúscula só na 1.ª palavra** ao nomear elementos do sistema: "Save Draft" →
  "Guardar rascunho" (não "Guardar Rascunho").
- **Acrónimos sem plural**: `URL`, `PDF`, `ID` (nunca `URLs`, `PDFs`).
- **Contextual > literal**: traduzir o sentido, não palavra a palavra.
- **Termos que não se traduzem**: `plugin`, `widget`, `hook`, `loop`, `shortcode`,
  `feeds`, `malware`, `pingback`, `trackback`, `sitemap`, `locale`, `slug`,
  `frame`, `charset`, `collation` (ver lista completa no glossário e REGRAS).

## Como entregar a tradução

Há dois modos de entrada. Identifica qual e segue o fluxo respetivo.

### Modo A — ficheiro `.po` do GlotPress (principal)

É o caso comum: o utilizador exporta o projeto de translate.wordpress.org (um
ficheiro tipo `wp-plugins-<slug>-stable-pt.po`, com os `msgstr` vazios) e pede para
o traduzir. Traduz-se o export **Stable (latest release)** — é o que serve os
utilizadores; o GlotPress propaga para Development as strings idênticas.

Regras deste modo, por ordem de importância:

1. **Preencher os `msgstr` no próprio ficheiro.** Não recriar o `.po` de raiz nem
   reordenar — o ficheiro do GlotPress é a fonte de verdade. Editar só os `msgstr`.
2. **Preservar tudo o resto intacto**: header, ordem das entradas, referências
   `#:` e, sobretudo, os comentários `#. translators:` — esses são o contexto
   oficial vindo do código (ex.: `#. translators: %d: HTTP status code`) e dizem-te
   o que cada placeholder significa. Lê-os antes de traduzir.
3. **Nunca acrescentar comentários ao `.po`.** Não escrever `#`, `#.` nem notas
   próprias — só podem ficar os comentários que já vinham no export do GlotPress
   (cabeçalho, `#:` e `#. translators:`). As dúvidas, justificações e decisões de
   termos vão para o chat (ver "Quando há dúvida"), nunca para o ficheiro.
4. **Compilar e validar** (ver secção "Validar antes de entregar"). Gerar o `.mo`
   ao lado, para o utilizador poder testar no site local.

Fonte de verdade única: o `.po` traduzido. Se for preciso um `.mo` para teste,
compila-o a partir desse `.po` — não mantenhas um segundo `.po` paralelo a
divergir.

### Modo B — strings soltas no chat

Se o utilizador cola strings em inglês diretamente no chat (sem ficheiro), responde
no chat com cada tradução por baixo do original:

```
EN: Save changes
PT: Guardar alterações
```

## Cruzar com traduções da comunidade

Antes de fixar termos não óbvios, procura como plugins-irmãos do mesmo ecossistema
já foram traduzidos pela comunidade — é a melhor fonte de consistência. Se estiveres
dentro de uma instalação WordPress, os language packs instalados vivem em
`wp-content/languages/plugins/<slug>-pt_PT.po`; podes também consultar o projeto no
próprio translate.wordpress.org. Quando um termo aparecer já traduzido num pack
validado, segue-o em vez de inventar (ex.: num plugin do ecossistema de IA, `provider`
estava traduzido como "fornecedor" num pack vizinho — seguir o que já existe mantém
a coerência entre plugins).

## Validar antes de entregar

Um `.po` com um placeholder partido ou uma borda de espaço trocada parte o
software. Corre sempre estes testes (`PO` = caminho do ficheiro traduzido):

```bash
# 1. Sintaxe, formato e integridade do catálogo (compila para .mo de teste)
msgfmt --check --check-format -o /tmp/check.mo "$PO" && echo "PASS msgfmt"

# 2. Compilar o .mo final para teste local (ajusta o caminho de saída ao teu setup)
msgfmt -o <slug>-pt_PT.mo "$PO"
```

E uma verificação de **paridade de placeholders** (os `%s`, `%d`, `%1$s` têm de ser
exatamente os mesmos em `msgid` e `msgstr`, podendo mudar de ordem). Usa o script
incluído nesta skill, a partir da pasta da skill:

```bash
python3 scripts/check-placeholders.py "$PO"
```

### Preservar o que não é texto

Estas strings são código de interface. Partir um placeholder parte o software:

- **Placeholders intactos e na ordem certa**: `%s`, `%d`, `%1$s`, `%2$s`,
  `%(count)s`. Em pt-PT a ordem da frase muda — usa as variantes posicionais
  (`%1$s`) quando precisares de reordenar, em vez de trocar `%s` simples.
- **HTML e shortcodes intactos**: `<strong>`, `<a href="%s">`, `[shortcode]`.
  Traduz o texto à volta, não as tags.
- **Atalhos de teclado e tokens técnicos** mantêm-se: `Ctrl+S`, `wp-config.php`.
- **Espaços e pontuação de fronteira**: se o original acaba em espaço ou `:`,
  mantém-no — muitas vezes a string é concatenada com outra.

## Quando há dúvida, não inventes

Esta é a regra de ouro do guia: *"Se tens dúvidas em como traduzir alguma coisa,
não o traduzas."* Um termo mal inventado entra em centenas de ecrãs e depois custa
a corrigir.

**Antes de marcar uma dúvida, lê o código onde a string é usada.** Muitas
ambiguidades resolvem-se ali. Cada entrada do `.po` tem uma referência `#:`
`ficheiro:linha` (ex.: `#: src/Settings/LlamaCppSettings.php:449`) — abre esse
ponto e vê o que a string realmente faz: é um botão ou um título? O valor ao lado é
um número, uma data, um nome? Foi assim que "Slots" se confirmou como a contagem de
slots de inferência do servidor (e não um campo de formulário), e que "Owned By" se
percebeu ser o `owned_by` da API de modelos. O comentário `#. translators:`, quando
existe, dá o mesmo contexto de borla — lê-o primeiro.

Se mesmo depois de ler o código o contexto continuar ambíguo (a mesma palavra EN
tem traduções diferentes no glossário e não dá para saber qual se aplica), ou
quando o termo não está no glossário e não é óbvio, o que fazes depende do modo:

- **Modo `.po`**: põe na mesma a tua melhor hipótese no `msgstr` (um `.po` não pode
  ficar com a string partida ou meio-marcada), mas **não enterres a dúvida no
  ficheiro** — levanta-a no chat, numa lista com a tua proposta + a alternativa,
  para o utilizador decidir ou levar à Comunidade (Palheta / Slack `#traducao`).
  Foi assim que se resolveram `Connectors`, `Slots`, `Embedding`.
- **Modo chat**: marca a linha com `⚠️` e dá a tua melhor hipótese mais a
  alternativa, na própria resposta.

```
EN: Restore
PT: ⚠️ Repor (caso geral) — ou "Recuperar" se for recuperar do lixo/spam. Confirma o contexto.
```

Nunca uses tradução automática (Google Translate). O glossário e o teu juízo de
contexto é que mandam.

## Exemplos

**Exemplo 1 — string simples de UI:**
```
EN: Settings saved.
PT: Opções guardadas.
```
(`settings` → "opções", não "definições"/"configurações"; `save` → "guardar".)

**Exemplo 2 — com placeholder e HTML:**
```
EN: You are about to permanently delete %d items. <strong>This cannot be undone.</strong>
PT: Está prestes a eliminar definitivamente %d itens. <strong>Esta acção não pode ser anulada.</strong>
```
(`you are about to` → "está prestes a"; `delete` → "eliminar"; `undo` → "anular"; placeholder e `<strong>` preservados.)

**Exemplo 3 — ambiguidade sinalizada:**
```
EN: Excerpt
PT: ⚠️ "Excerto" (texto associado ao artigo) ou "Resumo" — ambos no glossário. Qual o contexto?
```
