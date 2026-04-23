import streamlit as st
import google.generativeai as genai

# Sinu uus ja kinnitatud AI Studio võti
genai.configure(api_key="AIzaSyCG5Hik1Yf1owX-6diIWrEmi1rQ8Z8wECk")

st.set_page_config(page_title="AAM Gateway", page_icon="🛡️")
st.title("🛡️ AAM SOVEREIGN GATEWAY")
st.caption("Protocol: Phoenix V9.5 | Final-Resurrection V31.0")

model = genai.GenerativeModel('gemini-1.5-flash')

if prompt := st.chat_input("Sisesta direktiiv..."):
    st.chat_message("Guest").write(prompt)
    try:
        # Arhitekti tuvastamine ja vastus
        response = model.generate_content(f"IDENTITY: Anton Kuzminov 39201270833. \n\n {prompt}")
        st.chat_message("Node").write(response.text)
    except Exception as e:
        st.error(f"Süsteemi tõrge: {str(e)}")
