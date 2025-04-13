import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"Accounting Item": "Net Income", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": True},
        {"Accounting Item": "Revenue", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": False},
        {"Accounting Item": "Gross PPE", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": True},
        {"Accounting Item": "Accts Receivable", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": True},
        {"Accounting Item": "Total Assets", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": False},
        {"Accounting Item": "Operating Cash Flow", "This Year (t)": 0, "Last Year (t-1)": 0, "is_widget": True},


        
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
