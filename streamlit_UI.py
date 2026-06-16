import streamlit as st
import os
from features_helper import init_session_state, rebuild_document, render_preview
from feature_modules.feature01_create      import render_sidebar as render_create
from feature_modules.feature02_headings    import render_sidebar as render_headings
from feature_modules.feature03_paragraphs  import render_sidebar as render_paragraphs
from feature_modules.feature_formatting    import render_sidebar as render_formatting
from feature_modules.feature_lists         import render_sidebar as render_lists
from feature_modules.feature09_tables      import render_sidebar as render_tables
from feature_modules.feature11_image       import render_sidebar as render_image
from feature_modules.feature10_save        import render_sidebar as render_save

st.set_page_config(
    page_title="Python-docx Demo | 11 Features", 
    layout="wide", 
    page_icon="📄"
)

# Custom CSS for Demo App
css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as _f:
        _css = _f.read()
    st.markdown(f"<style>{_css}</style>", unsafe_allow_html=True)


# Initialize session state
init_session_state()
    

# ============================================================
# MAIN CONTENT: LIVE PREVIEW
# ============================================================
st.markdown("## 👁️ Live Preview & Document")
render_preview()

st.markdown("---")

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.markdown("## 📄 Document Builder")
st.sidebar.markdown("---")

render_create()

# Formatting — applies to all text content below
render_formatting()

st.sidebar.markdown("---")
render_headings()
render_paragraphs()
render_lists()

st.sidebar.markdown("---")
render_tables()
render_image()

st.sidebar.markdown("---")
render_save()