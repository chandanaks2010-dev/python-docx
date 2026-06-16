import streamlit as st
from features_helper import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("#### 1️⃣ Numbered Lists")
    numbered_items = st.sidebar.text_area("Items (one per line)", placeholder="Item 1\nItem 2\nItem 3", height=80, key="num_inp")
    if st.sidebar.button("Add Numbered List", key="f8", use_container_width=True):
        if numbered_items.strip():
            items = [x.strip() for x in numbered_items.split("\n") if x.strip()]
            add_block(
                "numbered_list", items,
                bold=st.session_state.bold,
                italic=st.session_state.italic,
                underline=st.session_state.underline,
                font_size=st.session_state.font_size,
                font_color=st.session_state.font_color,
                alignment=st.session_state.get("align", st.session_state.get("alignment", "Left")),
            )
            rebuild_document()
            st.success("Numbered list added!")
            st.rerun()
