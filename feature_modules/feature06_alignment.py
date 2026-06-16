import streamlit as st

def render_sidebar():
    st.sidebar.markdown("#### 📍 Alignment")
    align_choice = st.sidebar.radio("Alignment", ["Left", "Center", "Right", "Justify"], key="align")
    st.session_state.alignment = align_choice
