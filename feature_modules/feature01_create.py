import streamlit as st
from features_helper import new_document

def render_sidebar():
    st.sidebar.markdown("### ✨ Create Document")
    if st.sidebar.button("🆕 New Document", key="f1", use_container_width=True):
        new_document()
        st.success("New document created!")
        st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
