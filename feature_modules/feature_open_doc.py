import streamlit as st
from features_helper import open_document, rebuild_document

def render_sidebar():

    st.sidebar.markdown("#### 📂 Open Existing Document")

    uploaded_file = st.sidebar.file_uploader(
        "Choose a Word document",
        type=["docx"],
        key="upload_doc"
    )

    if uploaded_file is not None:
        open_document(uploaded_file)        
        rebuild_document()
        st.success("Document opened successfully!")
        st.rerun()