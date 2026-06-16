import streamlit as st


def render_sidebar():
    with st.sidebar.expander("⚙️ Formatting Options", expanded=False):
        st.markdown("**Style**")
        st.session_state.bold      = st.checkbox("Bold",      value=st.session_state.bold,      key="fmt_bold")
        st.session_state.italic    = st.checkbox("Italic",    value=st.session_state.italic,    key="fmt_italic")
        st.session_state.underline = st.checkbox("Underline", value=st.session_state.underline, key="fmt_under")

        st.markdown("**Font**")
        st.session_state.font_size  = st.select_slider("Size", options=[8, 10, 12, 14, 16, 18, 20, 24, 28], value=st.session_state.font_size, key="font_sz")
        st.session_state.font_color = st.color_picker("Color", value=st.session_state.font_color, key="font_col")

        st.markdown("**Alignment**")
        st.session_state.alignment = st.radio("Alignment", ["Left", "Center", "Right", "Justify"], key="align", horizontal=True)
