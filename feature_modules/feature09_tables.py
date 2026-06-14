import streamlit as st
from features_helper import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("### 📊 Tables")
    t_rows = st.sidebar.number_input("Rows", min_value=1, max_value=10, value=2, key="t_rows")
    t_cols = st.sidebar.number_input("Columns", min_value=1, max_value=10, value=3, key="t_cols")
    if st.sidebar.button("Add Table", key="f9", use_container_width=True):
        add_block("table", None, rows=t_rows, cols=t_cols, data=[[f"R{i}C{j}" for j in range(t_cols)] for i in range(t_rows)])
        rebuild_document()
        st.success("Table added!")
        st.rerun()
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")
