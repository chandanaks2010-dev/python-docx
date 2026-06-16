import streamlit as st
from features_helper import save_document, new_document

def render_sidebar():
    st.sidebar.markdown("#### 💾 Save & Download")
    buffer = save_document()
    st.sidebar.download_button(
        "📥 Download DOCX",
        buffer,
        file_name="document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
        key="download_btn"
    )
    if st.sidebar.button("🗑️ Clear All", key="f10_clear", use_container_width=True):
        new_document()
        st.sidebar.success("Cleared!")
        st.rerun()
