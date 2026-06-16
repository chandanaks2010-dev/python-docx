import streamlit as st
from features_helper import add_block, rebuild_document

def render_sidebar():
    st.sidebar.markdown("#### 📊 Tables")
    t_rows = st.sidebar.number_input("Rows", min_value=1, max_value=10, value=3, key="t_rows")
    t_cols = st.sidebar.number_input("Columns", min_value=1, max_value=10, value=3, key="t_cols")

    # Build a default CSV template whenever rows/cols change
    default_lines = []
    for r in range(int(t_rows)):
        default_lines.append(", ".join(f"Cell {r+1}{c+1}" for c in range(int(t_cols))))
    default_csv = "\n".join(default_lines)

    table_csv = st.sidebar.text_area(
        "Table data (one row per line, comma-separated)",
        value=default_csv,
        height=120,
        key="t_data",
        help="Each line is a table row. Values are separated by commas."
    )

    if st.sidebar.button("Add Table", key="f9", use_container_width=True):
        # Parse CSV input into a 2-D list
        data = []
        for line in table_csv.strip().splitlines():
            cells = [c.strip() for c in line.split(",")]
            # Pad or trim to match t_cols
            cells = cells[:int(t_cols)] + [""] * max(0, int(t_cols) - len(cells))
            data.append(cells)
        # Trim or pad rows to match t_rows
        data = data[:int(t_rows)]
        while len(data) < int(t_rows):
            data.append([""] * int(t_cols))

        add_block("table", None, rows=int(t_rows), cols=int(t_cols), data=data,
            bold=st.session_state.bold,
            italic=st.session_state.italic,
            underline=st.session_state.underline,
            font_size=st.session_state.font_size,
            font_color=st.session_state.font_color,
            alignment=st.session_state.get("alignment", "Left"),
        )
        rebuild_document()
        st.success("Table added!")
        st.rerun()
