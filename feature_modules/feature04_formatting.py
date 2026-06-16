import streamlit as st

def render_sidebar():
    st.sidebar.markdown("#### 🎨 Bold / Italic / Underline")
    st.session_state.bold = st.sidebar.checkbox("**Bold**", value=st.session_state.bold, key="fmt_bold")
    st.session_state.italic = st.sidebar.checkbox("*Italic*", value=st.session_state.italic, key="fmt_italic")
    st.session_state.underline = st.sidebar.checkbox("<u>Underline</u>", value=st.session_state.underline, key="fmt_under")
