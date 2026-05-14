import streamlit as st

def footer_home():
    st.markdown(f"""
        <div style='margin-top:2rem;gap:6px;display:flex;align-items:center;justify-content:center'>
            <p style='font-weight:bold;color:white;'> Created with ❤️ by Pankaj Jangir </p>
        </div>
    """,unsafe_allow_html=True)