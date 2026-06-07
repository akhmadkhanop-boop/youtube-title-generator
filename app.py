import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AK TITLE GENATER")
st.write("apni dacummntry topic ka title batao kun sa topic ba nana hain")



topic = st.text_input("topic batao")
persone = st.text_input("kis skahsait pa ban hain batao")

if st.button("Genernate title"):
    if topic:
        
        with st.spinner("AI such ra hain sabar karu"):
            
            if persone:
                user_content = f"yar mar topic hain {topic} our ya shaksait ka name hain {persone} apna ak powerfull title banan hain 7 title da du magar powerfull  hun alg alg hun sar ak jasa na hun"
            else:
                user_content = f"yar mar toic hain {topic} poerfull title ban ban ka dun 5 title hun tik hain taq luga videro oa clike kar"
                
            response = client.chat.completions.create(
                    model = "llama-3.3-70b-versatile",
                    temperature = 0.8,
                    messages = [
                       {
                           "role" : "system",
                           "content" : "tum ak professianal title export hun  apna muj powerfull tile banna hain main adcummntry channel ka leya ban ra hun apna  clicke bana hain taq luga mar video pa ka our mar channel pa viwes aya hain"
                           
                       },
                       {
                           "role" : "user",
                           "content" : user_content
                       }
                    ]
                )
                
                
            titles = response.choices[0].message.content
                
            st.subheader("====== TITLE GENERATOR ======")
            st.write(titles)
                
                
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("titles.txt", "a", encoding="utf-8") as f:
                f.write(f"\n\n=== {time_now} - {topic} ===\n")
                f.write()
                
            st.success("title ban gaya hain mubark hun")
    else:
        st.warning("topic nahi dal hain")
            
            
        

                
           