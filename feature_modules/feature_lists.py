import streamlit as st
from features_helper import add_block, rebuild_document


def render_sidebar():
    st.sidebar.markdown("#### 📋 Lists")
    list_type = st.sidebar.radio("List type", ["Bullet", "Numbered"], horizontal=True, key="list_type")
    items_input = st.sidebar.text_area("Items (one per line)", placeholder="Item 1\nItem 2\nItem 3", height=80, key="list_inp")

    label = "Add Bullet List" if list_type == "Bullet" else "Add Numbered List"
    if st.sidebar.button(label, key="f_lists", use_container_width=True):
        if items_input.strip():
            items = [x.strip() for x in items_input.split("\n") if x.strip()]
            block_type = "bullet_list" if list_type == "Bullet" else "numbered_list"
            add_block(
                block_type, items,
                bold=st.session_state.bold,
                italic=st.session_state.italic,
                underline=st.session_state.underline,
                font_size=st.session_state.font_size,
                font_color=st.session_state.font_color,
                alignment=st.session_state.get("alignment", "Left"),
            )
            rebuild_document()
            st.success(f"{list_type} list added!")
            st.rerun()
