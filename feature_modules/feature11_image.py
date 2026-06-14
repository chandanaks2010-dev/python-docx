import streamlit as st
from io import BytesIO
from features_helper import add_block, rebuild_document


def render_sidebar():
    st.sidebar.markdown("### 🖼️ Images")
    uploaded = st.sidebar.file_uploader("Upload image", type=["png", "jpg", "jpeg", "gif", "bmp"], key="f11_uploader")
    width_in = st.sidebar.slider("Width (inches)", min_value=1, max_value=6, value=3, key="f11_width")
    if st.sidebar.button("Add Image", key="f11_add", use_container_width=True):
        if uploaded is None:
            st.sidebar.warning("Please upload an image first.")
        else:
            img_bytes = BytesIO(uploaded.read())
            img_bytes.seek(0)
            add_block("image", img_bytes, width_in=width_in)
            rebuild_document()
            st.sidebar.success("Image added!")
            st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
