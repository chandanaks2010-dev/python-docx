import streamlit as st

def render_sidebar():
    st.sidebar.markdown("### 📍 Text Alignment")
    align_choice = st.sidebar.radio("Alignment", ["Left", "Center", "Right", "Justify"], key="align")
    st.session_state.alignment = align_choice
    st.sidebar.write(f"Selected: {align_choice}")
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
