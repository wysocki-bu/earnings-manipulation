# Import Streamlit
import streamlit as st

# **** Page layout setup ****
App_page_0 = st.Page(
    "pages/main.py",
    title="Click here to select stock",
    default=True
)
App_page_1 = st.Page(
    "pages/page1.py",
    title="1) See Raw Stock Data"
)
App_page_2 = st.Page(
    "pages/page2.py",
    title="2) See Data Statistics"
)
App_page_3 = st.Page(
    "pages/page3.py",
    title="3) See Stock Price Graph"
)
App_page_4 = st.Page(
    "pages/page4.py",
    title="4) List Model Training Code"
)
App_page_5 = st.Page(
    "pages/page5.py",
    title="5) List StreamLit App Code"
)
App_page_6 = st.Page(
    "pages/page6.py",
    title="6) V2 of List StreamLit App Code"
)
App_page_7 = st.Page(
    "pages/page7.py",
    title="7) Manually Enter Data"
)
App_page_8 = st.Page(
    "pages/page8.py",
    title="8) Regression Output"
)



# **** Set up navigation with section headers ****
pg = st.navigation(
    {
        "Start Here:": [App_page_0],
        "Dashboard Options": [App_page_1, App_page_2, App_page_3, App_page_4, App_page_5, App_page_6, App_page_7, App_page_8]
    }
)


# **** text/images shared on all pages ****
st.sidebar.markdown("Sidebar Prompts:")


# **** Execute the navigation code ****
pg.run()
