#!/usr/bin/env bash
# Rebuild the aligned PPT, Lesson Plan and Learner Guide from the M&A source.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
CW="$REPO/courseware"
SOFFICE="${SOFFICE:-soffice}"
PPT="$CW/Strategic Mergers and Acquisitions-v2.0.pptx"
LP="$CW/LP-Strategic Mergers and Acquisitions.docx"
LG="$CW/LG-Strategic Mergers and Acquisitions.docx"

python3 "$HERE/extract_original_visuals.py"
python3 "$HERE/build_slides.py"
python3 "$HERE/build_documents.py"

"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$PPT" "$LP" "$LG" >/dev/null 2>&1
python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 1
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$LP" "$LG" >/dev/null 2>&1

printf '%s\n' "Built courseware artifacts in $CW"
ls -1 "$PPT" "${PPT%.pptx}.pdf" "$LP" "${LP%.docx}.pdf" "$LG" "${LG%.docx}.pdf"
