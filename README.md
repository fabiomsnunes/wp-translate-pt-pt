# Tradução pt-PT (WordPress) — skill para Claude Code

Skill para o [Claude Code](https://docs.claude.com/claude-code) que traduz strings
de interface do WordPress (core, plugins, temas) de inglês para **português de
Portugal (pt-PT)**, seguindo o glossário oficial e o Guia de Tradutores da
Comunidade Portuguesa de WordPress.

O objetivo é uma tradução coerente com o glossário consolidado, na norma pré-AO90, formal e sem marcas de género.

## O que faz

- **Modo `.po` (principal)** — recebe um ficheiro `.po` exportado do
  translate.wordpress.org (GlotPress, com os `msgstr` vazios), preenche as
  traduções no próprio ficheiro, preserva header/ordem/comentários e valida o
  resultado. Pronto a carregar de volta no GlotPress.
- **Modo strings soltas** — traduz strings coladas diretamente no chat, devolvendo
  `EN:` / `PT:`.

Aplica as regras do guia (pré-AO90, infinitivo impessoal, sem género, maiúscula só
na 1.ª palavra, acrónimos sem plural, termos que não se traduzem) e consulta o
glossário oficial por pesquisa antes de fixar cada termo.

## Instalação

A skill é uma pasta. Copia `skills/wp-translate-pt-pt/` para a tua pasta de skills do
Claude Code:

```bash
# Global (todos os projetos):
cp -r skills/wp-translate-pt-pt ~/.claude/skills/

# Ou só para um projeto:
cp -r skills/wp-translate-pt-pt /caminho/do/projeto/.claude/skills/
```

O Claude Code passa a invocá-la automaticamente quando entregas um `.po` para
traduzir ou pedes traduções pt-PT.

## Conteúdo

```
skills/wp-translate-pt-pt/
├── SKILL.md                      Instruções e fluxo de trabalho
├── references/
│   ├── glossario-pt-pt.csv       Glossário oficial (snapshot do translate.wordpress.org)
│   └── REGRAS.md                 Interpretação do Guia de Tradutores pt_PT
└── scripts/
    ├── check-placeholders.py     Valida paridade de placeholders num .po
    ├── check-glossary.sh         Diz se o glossário falta ou está obsoleto (>30 dias)
    └── update-glossary.sh        Atualiza o glossário a partir do translate.wordpress.org
```

## Atualizar o glossário

O `glossario-pt-pt.csv` é um snapshot. A própria skill verifica o estado no início
de cada sessão (`check-glossary.sh`): se faltar ou tiver mais de 30 dias, pergunta
se queres atualizar antes de traduzir.

Para atualizar à mão a qualquer momento:

```bash
skills/wp-translate-pt-pt/scripts/update-glossary.sh
```

Usa por omissão o
[endpoint de exportação oficial](https://translate.wordpress.org/locale/pt/default/glossary/-export/)
do glossário pt-PT e grava a data em `references/.glossary-updated`. Para forçar
outro URL (caso o endpoint mude), passa-o como argumento:

```bash
skills/wp-translate-pt-pt/scripts/update-glossary.sh "<link-de-exportacao>"
```

## Validar uma tradução

```bash
# sintaxe + formato do catálogo
msgfmt --check --check-format -o /dev/null ficheiro-pt.po
# paridade de placeholders (%s, %d, %1$s) entre msgid e msgstr
python3 skills/wp-translate-pt-pt/scripts/check-placeholders.py ficheiro-pt.po
```

## Fontes

- [Guia de Tradutores — Português de Portugal (pt_PT)](https://pt.wordpress.org/traducoes/guia-de-tradutores-portugues-de-portugal-pt_pt/)
- [Glossário pt-PT no translate.wordpress.org](https://translate.wordpress.org/locale/pt/default/glossary/)

O glossário e as regras pertencem à Comunidade Portuguesa de WordPress. Esta skill
é apenas uma forma de os aplicar de forma consistente.

## Licença

[GPL-2.0-or-later](./LICENSE), em coerência com o ecossistema WordPress e com os
dados do glossário.
