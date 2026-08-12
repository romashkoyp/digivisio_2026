# Digivisio 2026

## Overview
Curated learning roadmaps built from [opin.fi](https://opin.fi) open study options. A profession skills map [roadmap.sh](https://roadmap.sh) is matched to courses in a cleaned CSV catalog; the result is published as a staged HTML roadmap.

## Pipeline

```
opin-*.json, part_1.json, part_2.json
        │
        ▼  Data prep (Python scripts)
extracted_links.csv → combined_courses.csv → unique_courses_en.csv
        │
        ▼  Step 1 — Google AI Studio
   product-manager.pdf + unique_courses_en.csv
        │
        ▼
   content.md
        │
        ▼  Step 2 — Cursor agent
   roadmap.html
```

---

## Data prep — Course catalog (JSON → CSV)

Scraped opin.fi exports are normalized into an English, deduplicated course list used in Step 1.

| Script | Input | Output |
|--------|-------|--------|
| `extract_links.py` | `opin-*.json` | `extracted_links.csv` |
| `combine_json_to_csv.py` | `part_1.json`, `part_2.json` | `combined_courses.csv` |
| `process_courses.py` | `combined_courses.csv` | `unique_courses_en.csv` |
| `compare_urls.py` | `extracted_links.csv`, `scraped_urls.json` | `unique_urls.csv` |

---

## Step 1 — Generate `content.md` (Google AI Studio)

**Tool:** [Google AI Studio](https://aistudio.google.com)

**Inputs:** `product-manager.pdf`, `unique_courses_en.csv`

**Prompt:**

> According to product-manager.pdf skills description, choose an appropriate courses form csv for each node skill, return result as table: skill, course name, course url, credits. Each skill can have only one course.

**Output:** `content.md` — markdown mapping each skill to one course (table or staged list).

---

## Step 2 — Build roadmap page (Cursor agent)

**Tool:** Cursor agent

**Inputs:** `content.md`  
**Style reference:** `roadmap.html`

**Prompt:**

> Create a simple web page in single html file in visual style of roadmap where person can see needed skills to be project manager and which courses this person should accept. Try to order courses according to project manager evaluation, from basics to pro skills. User should use this roadmap to plan his/her time and resources content.md Each course formated as link to course source link.

**Output:** `roadmap.html` — single-file static page; skills ordered basics → pro; each course title links to its opin.fi URL.

---

## File structure

```
Digivisio_2026/
│
├── README.md
│
├── # Skills map (Step 1 input)
├── product-manager.pdf          # Profession skills map (not in repo — add locally)
│
├── # Raw scrape data (data prep input)
├── opin-2026-05-11.json
├── opin-2026-05-11 (1).json
├── opin-2026-05-11 (2).json
├── opin-2026-05-11 (3).json
├── opin-2026-05-11 (4).json
├── part_1.json
├── part_2.json
│
├── # Data prep scripts
├── extract_links.py
├── combine_json_to_csv.py
├── process_courses.py
├── compare_urls.py
│
├── # CSV outputs (data prep)
├── extracted_links.csv          # Unique trimmed URLs from opin-*.json
├── combined_courses.csv         # Merged URL + description from part_*.json
├── combined_courses.txt         # Text export of combined catalog
├── unique_courses_en.csv        # English-only, deduplicated → Step 1 input
│
├── # Pipeline outputs (Steps 1–2)
├── content.md                   # Skills + matched courses (Step 1)
├── roadmap.html                 # Project manager roadmap UI (Step 2)
│
└── # Other roadmaps (examples)
    └── index-designer.html      # Graphic designer roadmap (same HTML pattern)
```

## Artifacts by stage

| Stage | File | Role |
|-------|------|------|
| Data prep | `extracted_links.csv` | Trimmed unique course URLs |
| Data prep | `combined_courses.csv` | Full merged course catalog |
| Data prep | `unique_courses_en.csv` | English-only, deduplicated catalog for Step 1 |
| Step 1 | `content.md` | Roadmap source (skills + courses) |
| Step 2 | `roadmap.html` | Published roadmap UI |

## Tech
- **Data prep:** Python 3 (stdlib: `csv`, `json`, `re`, `pathlib`)
- **Content:** Google AI Studio
- **UI:** Static HTML/CSS via Cursor (no build step)
- **Source:** [opin.fi](https://opin.fi) study options
