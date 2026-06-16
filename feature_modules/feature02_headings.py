import streamlit as st
from features_helper import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("#### 📑 Add Headings")
    h_level = st.sidebar.radio("Level", [1, 2, 3], horizontal=True, key="h_level")
    h_text = st.sidebar.text_input("Heading text", placeholder="Enter heading...", key="h_input")
    if st.sidebar.button("Add Heading", key="f2", use_container_width=True):
        if h_text:
            add_block(
                "heading", h_text, level=h_level,
                bold=st.session_state.bold,
                italic=st.session_state.italic,
                underline=st.session_state.underline,
                font_color=st.session_state.font_color,
                alignment=st.session_state.get("align", st.session_state.get("alignment", "Left")),
            )
            rebuild_document()
            st.success(f"Heading {h_level} added!")
            st.rerun()
