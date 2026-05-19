import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):

    with st.container(border=True):   # ✅ this creates a "card"

        st.markdown(f"### {name}")
        st.markdown(f"**Code:** `{code}` | **Section:** {section}")

        if stats:
            cols = st.columns(len(stats))
            for col, (icon, label, value) in zip(cols, stats):
                col.markdown(f"{icon} **{value}** {label}")

    if footer_callback:
        footer_callback()   # ✅ button will work correctly here