import streamlit as st
import ollama
st.set_page_config(
    page_title='AI CHATBOT'
)
st.title("WELCOME 🤖")
st.caption("Powered by ollama+streamlit")
if "store" not in st.session_state:
    st.session_state.store = []
for message in st.session_state.store:
    with st.chat_message(message["role"]):
        st.write(message["content"])
text = st.chat_input("Enter your message..")
if text:
    st.session_state.store.append({
        "role": "user",
        "content": text
    })
    with st.chat_message("user"):
        st.write(text)
    response = ollama.chat(
        model="gemma3:1b",
        messages=st.session_state.store
    )
    ans = response["message"]["content"]
    st.session_state.store.append({
        "role": "assistant",
        "content": ans
    })
    with st.chat_message("assistant"):
        st.write(ans)