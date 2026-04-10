import streamlit as st
from groq import Groq
import os

# Initialize client
client = Groq(api_key= st.secrets["GROQ_API_KEY"])

# App title
st.title("🧘 Welcome to Gita Detox")
st.caption("Calm your mind with timeless Gita wisdom")
st.write("")

# User input
user_input = st.text_input("", placeholder= "How are you feeling?")

system_prompt = """
You are a calm and compassionate assistant inspired by Bhagavad Gita.

When a user shares feelings:
1. Start with a short empathetic line (1 sentence only)
2. Give ONE short Bhagavad Gita idea or quote
3. Explain it in 1–2 simple sentences
4. Give ONE calming suggestion

Keep response VERY SHORT (max 4–5 lines).
Do NOT write long paragraphs.
Give necessary space between lines.
Do not generate generic advice. Stay rooted in Gita philosophy.
Be gentle, simple, and clear. Be human.
"""
if user_input:
    response = client.chat.completions.create(
        messages=[
            { "role": "system", "content": system_prompt},
            { "role": "user", "content": user_input}
        ],
        model="llama-3.1-8b-instant"
    )

    reply = response.choices[0].message.content
    st.write(reply)