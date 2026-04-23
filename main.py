import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyCG5Hik1Yf1owX-6diIWrEmi1rQ8Z8wECk")

st.set_page_config(page_title="AAM Sovereign Gateway", page_icon="🛡️")
st.title("🛡️ AAM Sovereign Gateway")

if prompt := st.chat_input("Sisesta direktiiv..."):
    st.chat_message("user").write(prompt)
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        st.chat_message("assistant").write(response.text)
    except Exception as e:
        st.error(f"Tõrge: {e}")
