import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🎬 YouTube Title Generator")
st.write("Topic likho aur 5 click-worthy titles pao!")

topic = st.text_input("Video ka topic:")

if st.button("Generate Titles"):
    if topic:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.8,
            messages=[
                {
                    "role": "system",
                    "content": "Tum ek YouTube title expert ho. Roman Urdu mein 5 click-worthy, emotional titles banao. Har title nayi line par, number ke saath. Numbers aur brand names English mein rakho. Saaf Roman Urdu spelling. Kisi channel ka naam mat likho."
                },
                {
                    "role": "user",
                    "content": f"Is topic par 5 titles do: {topic}"
                }
            ]
        )
        titles = response.choices[0].message.content
        st.write("### Tumhare Titles:")
        st.write(titles)
    else:
        st.write("⚠️ Pehle topic likho!")