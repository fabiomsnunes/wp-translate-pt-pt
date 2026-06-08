#!/usr/bin/env bash
#
# Refreshes the glossary (references/glossario-pt-pt.csv) from
# translate.wordpress.org. The glossary is a snapshot — run this every now and then
# to keep it aligned with the Community's consolidated terms.
#
# With no arguments it uses the official pt-PT glossary CSV export endpoint.
# To force a different URL (e.g. if the endpoint changes), pass it as an argument
# or via an environment variable:
#
#     ./update-glossary.sh "<csv-export-link>"
#     GLOSSARY_CSV_URL="<csv-export-link>" ./update-glossary.sh
#
# pt-PT glossary page:
#   https://translate.wordpress.org/locale/pt/default/glossary/
#
set -euo pipefail

DEFAULT_URL="https://translate.wordpress.org/locale/pt/default/glossary/-export/"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${SCRIPT_DIR}/../references/glossario-pt-pt.csv"
STAMP="${SCRIPT_DIR}/../references/.glossary-updated"

URL="${1:-${GLOSSARY_CSV_URL:-${DEFAULT_URL}}}"

TMP="$(mktemp)"
trap 'rm -f "${TMP}"' EXIT

echo "A descarregar o glossário de: ${URL}"
curl -fsSL "${URL}" -o "${TMP}"

if [[ ! -s "${TMP}" ]]; then
  echo "ERRO: o download veio vazio. Confirma o URL de exportação." >&2
  exit 1
fi

if ! head -1 "${TMP}" | grep -qi 'en'; then
  echo "AVISO: o ficheiro descarregado não parece um CSV de glossário (cabeçalho inesperado)." >&2
  echo "Primeira linha: $(head -1 "${TMP}")" >&2
fi

mv "${TMP}" "${TARGET}"
trap - EXIT

date +%F > "${STAMP}"

echo "Glossário atualizado: ${TARGET}"
echo "Linhas: $(wc -l < "${TARGET}" | tr -d ' ')"
echo "Carimbo de data: $(cat "${STAMP}")"
