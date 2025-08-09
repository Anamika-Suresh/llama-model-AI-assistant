import ollama
import streamlit as st

st.header("F.R.I.D.A.Y")
msg = st.text_input("ChatBox")

if st.button("Send"):
    response = ollama.chat(
        model='friday',
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    st.session_state.last_response = response['message']['content']

if "last_response" in st.session_state:
    st.write(st.session_state.last_response)
