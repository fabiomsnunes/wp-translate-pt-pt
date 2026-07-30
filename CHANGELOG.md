# Changelog

Todas as alterações relevantes a esta skill são documentadas aqui.
O formato segue o [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) e o
versionamento é [SemVer](https://semver.org/).

## [0.1.0]

### Adicionado
- Skill `wp-translate-pt-pt` para tradução EN → pt-PT de strings de interface do
  WordPress, com dois modos: ficheiro `.po` do GlotPress e strings soltas no chat.
- Glossário oficial (`references/glossario-pt-pt.csv`) — snapshot do
  translate.wordpress.org.
- `references/REGRAS.md` — interpretação do Guia de Tradutores pt_PT (pré-AO90,
  infinitivo impessoal, sem género, maiúsculas, acrónimos, termos que não se
  traduzem).
- `scripts/check-placeholders.py` — validação de paridade de placeholders num `.po`.
- `scripts/update-glossary.sh` — atualização do glossário a partir da fonte oficial.
