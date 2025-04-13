import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"item": "Net Income", "yr_t": 0, "yr_t_1": 0, "is_widget": True},
        {"item": "Revenue", "yr_t": 0, "yr_t_1": 0, "is_widget": False},
        {"item": "Gross PPE", "yr_t": 0, "yr_t_1": 0, "is_widget": True},
        {"item": "Accts Receivable", "yr_t": 0, "yr_t_1": 0, "is_widget": True},
        {"item": "Total Assets", "yr_t": 0, "yr_t_1": 0, "is_widget": False},
        {"item": "Operating Cash Flow", "yr_t": 0, "yr_t_1": 0, "is_widget": True},


        
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "item": "Accounting Item",
        "yr_t": st.column_config.NumberColumn(
            "This Year (t)",
            help="Enter Values for Current Year",
            min_value=0,
        ),
        "yr_t_1": st.column_config.NumberColumn(
            "Prior Year (t-1)",
            help="Enter Values for Prior Year",
            min_value=0,            
        ),
        "is_widget": "Widget ?",
    },
    disabled=["item", "is_widget"],
    hide_index=True,
)

highest_value = edited_df.loc[edited_df["yr_t"].idxmax()]["item"]
st.markdown(f"The largest value in Year t is: **{highest_value}** 🎈")
