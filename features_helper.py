import streamlit as st
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from io import BytesIO
import pandas as pd


def init_session_state():
    if "doc" not in st.session_state:
        st.session_state.doc = Document()
        st.session_state.content_blocks = []
        st.session_state.bold = False
        st.session_state.italic = False
        st.session_state.underline = False
        st.session_state.font_size = 12
        st.session_state.font_color = "#000000"


def save_document():
    """Feature 10: Save/Download Document"""
    rebuild_document()
    buffer = BytesIO()
    st.session_state.doc.save(buffer)
    buffer.seek(0)
    return buffer


def new_document():
    """Create a fresh Document and clear blocks"""
    st.session_state.doc = Document()
    st.session_state.content_blocks = []


def clear_all():
    st.session_state.content_blocks = []
    st.session_state.doc = Document()


def add_block(block_type, content, **kwargs):
    """Add content block"""
    st.session_state.content_blocks.append({
        "type": block_type,
        "content": content,
        **kwargs
    })


def rebuild_document():
    """Rebuild document from blocks"""
    st.session_state.doc = Document()
    for block in st.session_state.content_blocks:
        if block["type"] == "heading":
            st.session_state.doc.add_heading(block["content"], level=block.get("level", 1))
        elif block["type"] == "paragraph":
            p = st.session_state.doc.add_paragraph()
            run = p.add_run(block.get("content", ""))
            run.bold = block.get("bold", False)
            run.italic = block.get("italic", False)
            run.underline = block.get("underline", False)
            run.font.size = Pt(block.get("font_size", 12))
            try:
                color_val = block.get("font_color", "#000000")
                run.font.color.rgb = RGBColor(
                    int(color_val[1:3], 16),
                    int(color_val[3:5], 16),
                    int(color_val[5:7], 16)
                )
            except Exception:
                pass
            align_map = {
                "Left": WD_PARAGRAPH_ALIGNMENT.LEFT,
                "Center": WD_PARAGRAPH_ALIGNMENT.CENTER,
                "Right": WD_PARAGRAPH_ALIGNMENT.RIGHT,
                "Justify": WD_PARAGRAPH_ALIGNMENT.JUSTIFY,
            }
            try:
                p.alignment = align_map.get(block.get("alignment", "Left"), WD_PARAGRAPH_ALIGNMENT.LEFT)
            except Exception:
                p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        elif block["type"] == "bullet_list":
            for item in block.get("content", []):
                st.session_state.doc.add_paragraph(item, style="List Bullet")
        elif block["type"] == "numbered_list":
            for item in block.get("content", []):
                st.session_state.doc.add_paragraph(item, style="List Number")
        elif block["type"] == "table":
            rows = block.get("rows", max(1, len(block.get("data", []))))
            cols = block.get("cols", max(1, max((len(r) for r in block.get("data", [])), default=1)))
            table = st.session_state.doc.add_table(rows=rows, cols=cols)
            for ri, row in enumerate(block.get("data", [])):
                for cj, cell_content in enumerate(row):
                    table.cell(ri, cj).text = str(cell_content)
        elif block["type"] == "image":
            try:
                width_in = block.get("width_in", 3)
                if width_in:
                    st.session_state.doc.add_picture(block["content"], width=Inches(width_in))
                else:
                    st.session_state.doc.add_picture(block["content"])
            except Exception:
                pass
        elif block["type"] == "page_break":
            st.session_state.doc.add_page_break()


def render_preview():
    """Show live preview"""
    with st.container():
        if not st.session_state.content_blocks:
            st.info("👈 Add content from features above")
            return

        for i, block in enumerate(st.session_state.content_blocks):
            col_content, col_delete = st.columns([20, 1])

            editing_key = f"editing_{i}"
            is_editing = st.session_state.get(editing_key, False)

            with col_content:
                if is_editing:
                    # Editing UI (kept minimal here; main app handles sidebar formatting)
                    st.write("Editing mode")
                else:
                    # display mode
                    if block["type"] == "heading":
                        level = block.get("level", 1)
                        align = block.get("alignment", "Left")
                        css_align = "justify" if align == "Justify" else align.lower()
                        st.markdown(f"<h{level} style='text-align: {css_align}; margin:0 0 8px 0;'>{block['content']}</h{level}>", unsafe_allow_html=True)
                    elif block["type"] == "paragraph":
                        style = ""
                        if block.get("bold"): style += "font-weight: bold; "
                        if block.get("italic"): style += "font-style: italic; "
                        if block.get("underline"): style += "text-decoration: underline; "
                        align = block.get("alignment", "Left")
                        css_align = "justify" if align == "Justify" else align.lower()
                        style += f"text-align: {css_align}; "
                        style += f"font-size: {block.get('font_size', 12)}px; color: {block.get('font_color', '#000000')};"
                        st.markdown(f"<p style='{style}'>{block['content']}</p>", unsafe_allow_html=True)
                    elif block["type"] == "bullet_list":
                        for item in block.get("content", []):
                            st.markdown(f"• {item}")
                    elif block["type"] == "numbered_list":
                        for idx, item in enumerate(block.get("content", []), 1):
                            st.markdown(f"{idx}. {item}")
                    elif block["type"] == "table":
                        data = block.get("data")
                        if data:
                            try:
                                df = pd.DataFrame(data)
                                st.table(df)
                            except Exception:
                                html = "<table style='border-collapse: collapse;'>"
                                for row in data:
                                    html += "<tr>" + "".join(f"<td style='border:1px solid #ddd;padding:6px;'>{str(cell)}</td>" for cell in row) + "</tr>"
                                html += "</table>"
                                st.markdown(html, unsafe_allow_html=True)
                        else:
                            st.write("📊 Table inserted (no data)")
                    elif block["type"] == "image":
                        st.write("🖼️ Image inserted")
                    elif block["type"] == "page_break":
                        st.markdown("---")

            with col_delete:
                if st.button("✏️", key=f"edit_{i}"):
                    st.session_state[editing_key] = True
                    return
                if st.button("🗑️", key=f"del_{i}", help="Delete"):
                    st.session_state.content_blocks.pop(i)
                    rebuild_document()
                    return
