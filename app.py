import streamlit as st
import requests

st.set_page_config(page_title="Ask Vlad's Agent", page_icon="🤖")

st.title("🤖 Ask Vlad's AI Agent")
st.markdown("### Curious about Vlad? Ask (almost) anything! (actually just a few questions)")

st.markdown("#### ✅ Examples of questions I **can** answer:")
st.markdown("""
- 🧑 Who is Vlad?  
- 🎬 What are his favourite movies, games, or singers?  
- 💻 What is his tech stack?  
- 🐱 Does he have a pet?  
- 🎸 What are his hobbies?  
- 🌍 Where was he born?
- 🧠 What is his view on life?
""")

st.markdown("<hr style='margin:1em 0'>", unsafe_allow_html=True)

st.markdown("#### ⚠️ Examples of questions I **don’t** know (yet):", unsafe_allow_html=True)
with st.expander("Show examples of 'unknowns'"):
    st.markdown("""
    - 💍 What is Vlad’s opinion on marriage?  
    - 🎧 Does Vlad like Kanye West?  
    - 🎂 When is Vlad’s birthday?  
    - 🎨 What is his favorite color?  
    - 🤔 What is his MBTI personality type?  
    """)

st.markdown("<hr style='margin:1em 0'>", unsafe_allow_html=True)

question = st.text_input("💬 Your question", placeholder="e.g., What are Vlad's favorite games?")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "https://rag-vlad-api-189704280321.europe-west1.run.app/ask",
                    json={"question": question}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    st.success(answer)
                else:
                    st.error(f"Error: {response.status_code} — {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")

st.markdown("<hr style='margin:2em 0'>", unsafe_allow_html=True)

st.markdown(
    "Made by [Vlad](https://www.linkedin.com/in/vladbkv/) · "
    "[GitHub](https://github.com/Vladislav1753) · "
    "Powered by RAG & LangChain",
    unsafe_allow_html=True
)
