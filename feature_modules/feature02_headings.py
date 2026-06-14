import streamlit as st
from features import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("### 📑 Add Headings")
    h_level = st.sidebar.radio("Level", [1, 2, 3], horizontal=True, key="h_level")
    h_text = st.sidebar.text_input("Heading text", placeholder="Enter heading...", key="h_input")
    if st.sidebar.button("Add Heading", key="f2", use_container_width=True):
        if h_text:
            add_block("heading", h_text, level=h_level)
            rebuild_document()
            st.success(f"Heading {h_level} added!")
            st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
