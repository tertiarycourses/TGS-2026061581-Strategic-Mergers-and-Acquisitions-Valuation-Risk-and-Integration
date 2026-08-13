# Strategic Mergers and Acquisitions — Valuation, Risk, and Integration

WSQ courseware for **TGS-2026061581** and TSC **WST-CFI-5003-1.1-1 — Mergers and Acquisition**.

## Courseware preview

![Strategic Mergers and Acquisitions courseware title slide](screenshot.png)

## Public courseware

- 149-slide visual deck in PPTX and PDF
- Detailed Learner Guide in DOCX and PDF
- Two-day Lesson Plan in DOCX and PDF
- Eight progressive real-world activity packs, each in its own folder
- Reproducible single-source build modules

The slide deck reuses 36 selected diagrams and visual assets from the supplied original presentation. Detailed procedures are kept in the Learner Guide and activity Markdown files rather than the PPT.

## Real-world case spine

All eight activities use the announced Bonadio Group–T. Gschwender & Associates transaction. Reported facts remain distinct from course-only financial assumptions because the public announcement did not disclose transaction terms.

1. Deal Thesis and Structure
2. Valuation Triangulation
3. Three-Year Synergy Forecast
4. Pro Forma and Tax Challenge
5. Target Screening and Diligence
6. M&A Risk Intelligence
7. Integration Program Design
8. Culture, Talent and Client Continuity

## Build

```bash
./build/build_courseware.sh
python3 build/build_assessment_mna.py
```

The assessment generator preserves the approved four-question WA and three-task Case Study mappings. The `assessment/` directory and trainer-only answer keys are deliberately excluded from the public repository.

## Principal sources

- [Course page](https://www.tertiarycourses.com.sg/wsq-strategic-mergers-and-acquisitions-valuation-risk-and-integration.html)
- [Bonadio–TGA transaction report](https://www.cpapracticeadvisor.com/2026/08/06/credit-risk-management-firm-joins-the-bonadio-group/188098/)
- [Trends and Risks in M&A: A Review](https://www.mdpi.com/2227-9091/12/9/143)
- [M&A in the professional services sector](https://www.financierworldwide.com/briefing-room-ma-in-the-professional-services-sector)
- [EY: Nine key steps to setting up an M&A integration program](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/insights/mergers-acquisitions/documents/ey-nine-key-steps-to-setting-up-merger-acquisition-integration-program.pdf)
- [Risk Management in Enterprise M&A](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106493)
