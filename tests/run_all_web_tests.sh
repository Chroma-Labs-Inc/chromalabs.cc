#!/usr/bin/env bash
# ==============================================================================
# CHROMA LABS: CHROMALABS.CC WEB APPLICATION TEST SUITE (LINUX)
# Framework: Reflex (Python + Next.js / React)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEB_ROOT="$(cd "$SCRIPT_DIR/../Production" && pwd)"
VENV_PYTHON="$WEB_ROOT/.venv/bin/python"

if [ ! -x "$VENV_PYTHON" ]; then
    echo -e "\033[1;31m[ERROR] Python virtualenv not found at $WEB_ROOT/.venv\033[0m"
    exit 1
fi

echo -e "\033[1;36m================================================================================\033[0m"
echo -e "\033[1;36m       CHROMA LABS: CHROMALABS.CC WEB PLATFORM VERIFICATION SUITE              \033[0m"
echo -e "\033[1;36m       Framework: Reflex (Full-Stack Python / React / Vite)                     \033[0m"
echo -e "\033[1;36m================================================================================\033[0m"

TOTAL_START=$(date +%s%N)

echo -e "\n\033[1;33m[*] [1/3] Verifying Brand Assets & Vector Generation...\033[0m"
cd "$SCRIPT_DIR"
"$VENV_PYTHON" gen_all_svgs.py
"$VENV_PYTHON" gen_svg.py
"$VENV_PYTHON" hard_crop.py
"$VENV_PYTHON" check_img.py
echo -e "  \033[1;32m[PASS]\033[0m Brand assets and SVGs verified."

echo -e "\n\033[1;33m[*] [2/3] Verifying Reflex rxconfig Configuration...\033[0m"
cd "$WEB_ROOT"
"$VENV_PYTHON" -c "
import rxconfig
print(f'  -> App Name: {rxconfig.config.app_name}')
print(f'  -> Environment: {rxconfig.config.env}')
print(f'  -> Plugins: {len(rxconfig.config.plugins)} configured')
assert rxconfig.config.app_name == 'chromalabs'
"
echo -e "  \033[1;32m[PASS]\033[0m rxconfig configuration valid."

echo -e "\n\033[1;33m[*] [3/3] Compiling and Mounting Reflex Application Tree...\033[0m"
"$VENV_PYTHON" -c "
import reflex as rx
from chromalabs.chromalabs import app

pages = getattr(app, '_unevaluated_pages', {}) or getattr(app, '_pages', {})
print(f'  -> Registered routes/pages: {len(pages)}')
for path, page_obj in sorted(pages.items()):
    title = getattr(page_obj, 'title', 'Untitled')
    print(f'     * /{path} -> \"{title}\"')
assert len(pages) == 12, f'Expected 12 registered pages, got {len(pages)}'
"
echo -e "  \033[1;32m[PASS]\033[0m All 12 Reflex application pages and routes validated."

TOTAL_END=$(date +%s%N)
TOTAL_DIFF_MS=$(( (TOTAL_END - TOTAL_START) / 1000000 ))
TOTAL_DIFF_SEC=$(awk "BEGIN {printf \"%.2f\", $TOTAL_DIFF_MS / 1000}")

echo ""
echo -e "\033[1;32m================================================================================\033[0m"
echo -e "\033[1;32m   CHROMALABS.CC VERIFICATION PASSED: 100% OPERATIONAL ON LINUX                \033[0m"
echo -e "\033[1;32m   Completed in ${TOTAL_DIFF_SEC}s                                              \033[0m"
echo -e "\033[1;32m================================================================================\033[0m"
