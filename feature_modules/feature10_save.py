import streamlit as st
from features import save_document, clear_all

def render_sidebar():
    st.sidebar.markdown("### 💾 Save & Download")
    if st.sidebar.button("📥 Download DOCX", key="f10_download", use_container_width=True):
        buffer = save_document()
        st.sidebar.download_button(
            "Click to Download",
            buffer,
            file_name="document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
            key="download_btn"
        )
    if st.sidebar.button("🗑️ Clear All", key="f10_clear", use_container_width=True):
        clear_all()
        st.sidebar.success("Cleared!")
        st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
