import streamlit as st
import os
from features_helper import init_session_state, rebuild_document, render_preview
from feature_modules.feature01_create import render_sidebar as render_f1
from feature_modules.feature02_headings import render_sidebar as render_f2
from feature_modules.feature03_paragraphs import render_sidebar as render_f3
from feature_modules.feature04_formatting import render_sidebar as render_f4
from feature_modules.feature05_font import render_sidebar as render_f5
from feature_modules.feature06_alignment import render_sidebar as render_f6
from feature_modules.feature07_bullets import render_sidebar as render_f7
from feature_modules.feature08_numbered import render_sidebar as render_f8
from feature_modules.feature09_tables import render_sidebar as render_f9
from feature_modules.feature10_save import render_sidebar as render_f10
from feature_modules.feature11_image import render_sidebar as render_f11

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
# SIDEBAR: 10 FEATURES
# ============================================================
st.sidebar.markdown("## 🎯 11 Features")
st.sidebar.markdown("---")

# render each feature's sidebar block
render_f1()
render_f2()
render_f3()
render_f4()
render_f5()
render_f6()
render_f7()
render_f8()
render_f9()
render_f11()
render_f10()