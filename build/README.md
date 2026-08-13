# Courseware build source

This folder is the single source for TGS-2026061581, **Strategic Mergers and Acquisitions — Valuation, Risk, and Integration**.

## Build

```bash
./build/build_courseware.sh
python3 build/build_assessment_mna.py
```

`build_courseware.sh` generates the 149-slide PPTX/PDF, Lesson Plan DOCX/PDF, Learner Guide DOCX/PDF, and eight individual activity folders. It also extracts 36 diagrams and visual assets from the supplied legacy PPT into `original_visuals/` for reuse in the updated visual-reference galleries.

`build_assessment_mna.py` generates the four confidential assessment DOCX files in `assessment/`. It preserves the approved legacy instrument structure and mappings: WA has four open-ended questions; the Case Study has three integrated tasks.

## Source modules

- `course_data.py`: metadata, TSC, outcomes, topic content, schedules and sources.
- `data_domain1.py` … `data_domain4.py`: eight progressive Bonadio–TGA activity packs.
- `build_slides.py`: all-white visual slide system; detailed procedures are intentionally excluded.
- `build_documents.py`: aligned Lesson Plan, detailed Learner Guide and activity Markdown folders.
- `extract_original_visuals.py`: selected visual reuse from the old PPT.
- `inject_toc.py`: static page-numbered Word contents tables after the first PDF render.
- `build_assessment_mna.py`: WA/CS papers and trainer-only marking guides.

All financial inputs not reported in the Bonadio–TGA announcement are explicitly marked as course assumptions.
