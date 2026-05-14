import streamlit as st
from ui.base_layout import style_base_layout

def student_screen():
    style_base_layout()
    st.header('Student Screen')
    

    if st.button('Back'):
        st.session_state['login_type'] = None
        st.rerun()

    