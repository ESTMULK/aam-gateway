import streamlit as st
import google.generativeai as genai

# Sinu uus API võti
genai.configure(api_key="AIzaSyCG5Hik1Yf1owX-6diIWrEmi1rQ8Z8wECk")

st.set_page_config(page_title="AAM Sovereign Gateway", page_icon="🛡️")
st.title("🛡️ AAM Sovereign Gateway")

# Kui kood on "vigane", siis siitmaalt viskab ta vea. 
# Aga me kasutame uusimat Flash mudelit, mis on lollikindel.
model = genai.GenerativeModel('gemini-1.5-flash')

if prompt := st.chat_input("Sisesta direktiiv, Arhitekt..."):
    st.chat_message("user").write(prompt)
    try:
        # See on koht, kus toimub tegelik ühendus
        response = model.generate_content(f"Sina oled AAM süsteemi süda. Arhitekt Anton Kuzminov on andnud käsu: {prompt}")
        st.chat_message("assistant").write(response.text)
    except Exception as e:
        st.error(f"Süsteemi tõrge: {e}")
