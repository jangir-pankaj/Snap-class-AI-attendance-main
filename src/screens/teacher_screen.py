import streamlit as st
from ui.base_layout import style_base_layout

def teacher_screen():
    st.header('Teacher Screen')
    style_base_layout()
    

    if st.button('Back'):
        st.session_state['login_type'] = None
        st.rerun()