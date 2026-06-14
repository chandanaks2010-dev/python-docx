# python-docx (project: phython-docx)

Library Name: python-docx  
Version: 0.8.11  
Official Website: https://python-docx.readthedocs.io/ and https://github.com/python-openxml/python-docx

## Purpose of this Module
This project demonstrates using the python-docx library to create, read, and modify Microsoft Word (.docx) documents programmatically. It provides examples and utilities for common document automation tasks such as generating reports, formatting text, inserting tables, and exporting data to Word files.

## Features implemented by the Learner
This project exposes the following 10 interactive features (matching the `feature_modules`):

1. Create a new `.docx` document and initialize document state
2. Add headings (multiple levels)
3. Add and edit paragraphs
4. Apply character and paragraph formatting (bold, italic, underline, size, color, spacing)
5. Adjust font options (typeface, size)
6. Set paragraph alignment (left, center, right, justify)
7. Add unordered (bulleted) lists
8. Add ordered (numbered) lists
9. Insert and populate tables with data
10. Save and export the `.docx` file

## Streamlit GUI (Live Preview)
This repository includes a Streamlit-based UI to interactively build and preview .docx documents.

- Main app file: `streamlit_UI.py`
- Features are exposed in the left sidebar (10 feature modules).
- Live preview and document generation appear in the main area.
- Custom CSS is loaded from `assets/styles.css` when present.

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

## Usage Notes
- Use the sidebar to configure document content and formatting via the 10 feature modules.
- The Live Preview section updates based on sidebar inputs; use the Save feature to export a .docx file.
- Ensure `assets/styles.css` exists if you want the custom styling applied.

## Industry Applications
1. Automated report generation for finance and analytics  
2. HR — offer letters, contracts, and automated employee documents  
3. Legal — templated contracts, NDAs, and document assembly  
4. Education — generate assignments, certificates, and feedback forms  
5. Publishing / Documentation — convert data outputs into formatted Word docs

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