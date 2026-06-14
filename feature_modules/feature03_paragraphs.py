import streamlit as st
from features import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("### 📝 Add Paragraphs")
    p_text = st.sidebar.text_area("Paragraph text", placeholder="Enter text...", height=80, key="p_input")
    if st.sidebar.button("Add Paragraph", key="f3", use_container_width=True):
        if p_text:
            add_block("paragraph", p_text, bold=st.session_state.bold, italic=st.session_state.italic,
                     underline=st.session_state.underline, font_size=st.session_state.font_size,
                     font_color=st.session_state.font_color,
                     alignment=st.session_state.get("align", st.session_state.get("alignment", "Left")))
            rebuild_document()
            st.success("Paragraph added!")
            st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
