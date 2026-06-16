import streamlit as st
from features_helper import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("#### ● Bullet Lists")
    bullet_items = st.sidebar.text_area("Items (one per line)", placeholder="Item 1\nItem 2\nItem 3", height=80, key="bullet_inp")
    if st.sidebar.button("Add Bullet List", key="f7", use_container_width=True):
        if bullet_items.strip():
            items = [x.strip() for x in bullet_items.split("\n") if x.strip()]
            add_block(
                "bullet_list", items,
                bold=st.session_state.bold,
                italic=st.session_state.italic,
                underline=st.session_state.underline,
                font_size=st.session_state.font_size,
                font_color=st.session_state.font_color,
                alignment=st.session_state.get("align", st.session_state.get("alignment", "Left")),
            )
            rebuild_document()
            st.success("Bullet list added!")
            st.rerun()
