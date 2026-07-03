import streamlit as st
from src.components.header import header_home
from src.ui.style_base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home
def home_screen():
    header_home()

    style_base_layout()
    style_background_home()
    col1 , col2 = st.columns(2, gap="large")

  # 1. Keeps your beautiful white card styles intact
    st.markdown("""
        <style>
        [data-testid="stColumn"] {
            background-color: white !important;
            padding: 25px !important;
            border-radius: 24px !important;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1) !important;
            text-align: center !important;
        }
        [data-testid="stColumn"] h2 {
            color: #333333 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Re-applied your exact original image strings from your code backup
    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120) 
        if st.button("Student Portal", type="primary", icon=":material/arrow_outward:", icon_position="right", key="btn_student"):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145) 
        if st.button("Teacher Portal", type="primary", icon=":material/arrow_outward:", icon_position="right", key="btn_teacher"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()
        
