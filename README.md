# python-docx

**Module Assigned:** python-docx

---

## Module Details

| | |
|---|---|
| **Library Name** | python-docx |
| **Version** | 0.8.11 |
| **Official Website** | https://python-docx.readthedocs.io/ |
| **Source Repository** | https://github.com/python-openxml/python-docx |

---

## Purpose of this Module

This project demonstrates using the python-docx library to create, read, and modify Microsoft Word (.docx) documents programmatically. It provides examples and utilities for common document automation tasks such as generating reports, formatting text, inserting tables, and exporting data to Word files.

---

## Features implemented by the Learner

11 interactive features are implemented (exceeding the minimum of 10):

1. Create a new `.docx` document and initialize document state
2. Add headings (multiple levels: H1, H2, H3)
3. Add and edit paragraphs
4. Apply character and paragraph formatting (bold, italic, underline, size, color, spacing)
5. Adjust font options (typeface, size, color)
6. Set paragraph alignment (left, center, right, justify)
7. Add unordered (bulleted) lists
8. Add ordered (numbered) lists
9. Insert and populate tables with data (up to 10 × 10, CSV-style input)
10. Save and export the `.docx` file (one-click download + Clear All)
11. Insert images (PNG, JPG, GIF, BMP) with configurable width

### Module Structure (current)

| File | Covers |
|---|---|
| `feature01_create.py` | Feature 1 — create / new document |
| `feature02_headings.py` | Feature 2 — headings |
| `feature03_paragraphs.py` | Feature 3 — paragraphs |
| `feature_formatting.py` | Features 4, 5, 6 — bold/italic/underline, font size & color, alignment (consolidated) |
| `feature_lists.py` | Features 7, 8 — bullet and numbered lists (consolidated) |
| `feature09_tables.py` | Feature 9 — tables (CSV-style input) |
| `feature10_save.py` | Feature 10 — download DOCX + Clear All |
| `feature11_image.py` | Feature 11 — insert images |
| `features_helper.py` | Shared engine: session state, `add_block`, `rebuild_document`, live preview |

## Streamlit GUI (Live Preview)
This repository includes a Streamlit-based UI to interactively build and preview .docx documents.

- Main app file: `streamlit_UI.py`
- Features are exposed in the left sidebar (11 feature modules).
- Live preview and document generation appear in the main area.
- Custom CSS is loaded from `assets/styles.css` when present.

### Sidebar layout (current)
| Sidebar section | What it does |
|---|---|
| Document Builder | Create / reset document |
| ⚙️ Formatting Options *(expander)* | Bold, italic, underline, font size, color, alignment — applied to all content added below |
| Headings | Add heading with level 1–3 |
| Paragraphs | Add freeform paragraph text |
| Lists | Bullet or numbered list (radio toggle, one per add) |
| Tables | CSV-style grid input with configurable rows × columns |
| Images | Upload image file, set width in inches |
| Save & Download | Download `.docx` or Clear All |

## Installation
Follow these steps from the repository root (platform-agnostic).

- Create and activate a virtual environment:

   - Windows (PowerShell)

      ```powershell
      python -m venv .venv
      .venv\Scripts\Activate.ps1
      ```

   - Windows (cmd)

      ```cmd
      python -m venv .venv
      .venv\Scripts\activate.bat
      ```

   - macOS / Linux

      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```

- Install dependencies from `requirements.txt` (recommended):

   ```bash
   pip install -r requirements.txt
   ```

If you prefer installing packages individually:

```bash
pip install python-docx streamlit Pillow
```

## How to run (GUI)
1. Open a terminal in the project folder (e.g., `c:\Sem1\python-docx`).
2. Activate the virtual environment (see Installation).
3. Launch the Streamlit app using the module runner (recommended):

```bash
python -m streamlit run streamlit_UI.py
```

Or use the `streamlit` CLI directly:

```bash
streamlit run streamlit_UI.py
```

4. Streamlit will print a local URL; open it in your browser to use the interactive GUI.
5. Use the sidebar to configure the document; use the Save feature to export a `.docx` file.

## Recent Changes

### Refactored module architecture
- Features 4, 5, 6 (formatting / font / alignment) merged into a single `feature_formatting.py` module rendered as a collapsible sidebar expander **⚙️ Formatting Options**. Formatting state is stored in `st.session_state` and applied to all content blocks added after it is set.
- Features 7, 8 (bullet list / numbered list) merged into `feature_lists.py` with a radio button to switch list type. Both list types share one "Add" button.

### New feature: Images (Feature 11)
- Added `feature_modules/feature11_image.py`.
- Supports PNG, JPG, JPEG, GIF, BMP uploads via Streamlit file uploader.
- Configurable width slider (1–6 inches).
- Image alignment inherits the active alignment setting.
- `Pillow>=8.0` added to `requirements.txt`.

### Shared engine (`features_helper.py`)
- Centralised `init_session_state()`, `add_block()`, `rebuild_document()`, `save_document()`, `new_document()`, and `render_preview()`.
- Live preview renders HTML inline for headings, paragraphs, bullet/numbered lists, tables, and images.
- `rebuild_document()` re-creates the `.docx` from the full `content_blocks` list on every change, keeping the in-memory document in sync.

### Table module improvements
- Rows and columns are configurable with number inputs (up to 10 × 10).
- A CSV-style text area with auto-generated default values makes data entry fast.
- Input is automatically padded or trimmed to match the declared row × column dimensions.

### Save module
- **📥 Download DOCX** uses Streamlit's `download_button` for one-click export.
- **🗑️ Clear All** button resets the document and all content blocks.

## Usage Notes
- Use the sidebar to configure document content and formatting via the 11 feature modules.
- The Live Preview section updates based on sidebar inputs; use the Save feature to export a .docx file.
- Ensure `assets/styles.css` exists if you want the custom styling applied.

## Industry Applications

10 real-world applications (exceeding the minimum of 5):

1. **Automated Report Generation** — finance and analytics teams generate recurring reports (P&L, KPIs, balance sheets) directly from databases without manual Word editing; tools like Power BI and Tableau export pipelines use similar techniques
2. **HR Documents** — automatically produce offer letters, contracts, salary slips, and onboarding packs populated from HRMS systems (SAP SuccessFactors, Workday)
3. **Legal** — assemble templated contracts, NDAs, compliance documents, and court filings at scale; DocuSign and Clio use document generation under the hood
4. **Education** — generate personalised assignments, certificates, progress reports, and feedback forms for large student cohorts from LMS data (Moodle, Canvas)
5. **Healthcare** — produce patient discharge summaries, lab reports, and prescription documents auto-filled from EHR systems (Epic, Cerner)
6. **E-commerce & Retail** — generate product catalogues, purchase orders, invoices, and delivery notes from order management systems (Shopify, SAP)
7. **Government & Public Sector** — create compliance reports, audit trails, and citizen-facing letters in standardised Word formats required by regulatory bodies
8. **Banking & Insurance** — auto-generate loan sanction letters, policy documents, KYC reports, and claim settlement letters from core banking systems
9. **Software / DevOps** — export test reports, API documentation, and release notes from CI/CD pipelines (Jenkins, GitHub Actions) into formatted Word documents for stakeholders

### Popular Tools & Platforms That Use python-docx (or equivalent)

| Tool / Platform | How document generation is used |
|---|---|
| **Django / Flask web apps** | Generate downloadable Word reports on demand for end users |
| **Jupyter Notebooks** | Export analysis results and charts as formatted `.docx` reports |
| **Airflow / Prefect pipelines** | Schedule and auto-distribute Word reports as pipeline outputs |
| **Pandas + python-docx** | Convert DataFrame analysis results into formatted Word tables |
| **ReportLab / docxtpl** | Companion libraries for more complex templated Word generation |
| **Zapier / Make (Integromat)** | Trigger Word document creation from form submissions or CRM events |
| **Microsoft Power Automate** | Similar automated document generation workflows in enterprise environments |

---

## Basic Usage Example
```python
from docx import Document

doc = Document()
doc.add_heading('Report Title', level=1)
p = doc.add_paragraph('Generated with ')
p.add_run('python-docx').bold = True
table = doc.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Name'
hdr_cells[1].text = 'Value'
hdr_cells[2].text = 'Notes'
doc.save('example.docx')