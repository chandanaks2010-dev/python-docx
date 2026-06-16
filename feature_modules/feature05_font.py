import streamlit as st

def render_sidebar():
    st.sidebar.markdown("#### 🔤 Font Size & Color")
    st.session_state.font_size = st.sidebar.select_slider("Size", options=[8, 10, 12, 14, 16, 18, 20, 24, 28], value=12, key="font_sz")
    st.session_state.font_color = st.sidebar.color_picker("Color", value="#000000", key="font_col")
