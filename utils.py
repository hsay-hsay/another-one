import streamlit as st  
from streamlit_extras.app_logo import add_logo

# Adds company logo at the top of sidebar
def add_company_logo():
    add_logo('images/resoluteai_logo_smol.jpg', height=80)
    st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] {
                    padding-top: 1rem;
                    background-position: 10px 10px;
                }
                [data-testid="stSidebarNav"]::before {
                    content: "My Company Name";
                    margin-left: 20px;
                    margin-top: 20px;
                    font-size: 1px;
                    position: relative;
                    top: 1px;
                }
            </style>
            """,
            unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <style>
            .css-1y4p8pa {
                padding-top: 0rem;
                max-width: 50rem;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
    
    
def set_sidebar_state():
    # set sidebar collapsed before login
    if 'sidebar_state' not in st.session_state:
        st.session_state.sidebar_state = 'collapsed'

    # hide collapsed control button
    hide_bar = """
            <style>
            [data-testid="collapsedControl"] {visibility:hidden;}
            </style>
            """

    # set sidebar expanded after login
    # if login_after:
    #     st.session_state.sidebar_state = 'expanded'
    # else:
    st.session_state.sidebar_state = 'collapsed'
    st.markdown(hide_bar, unsafe_allow_html=True)