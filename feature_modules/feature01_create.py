import streamlit as st
from features_helper import new_document, add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("#### ✨ Create Document")
    if st.sidebar.button("🆕 New Document", key="f1", use_container_width=True):
        new_document()
        st.success("New document created!")
        st.rerun()
    if st.sidebar.button("↵ Insert Page Break", key="f1_pagebreak", use_container_width=True):
        add_block("page_break", None)
        rebuild_document()
        st.success("Page break inserted!")
        st.rerun()
