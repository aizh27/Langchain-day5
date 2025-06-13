import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# --------------------------------------------
# 1. Gemini API Key Setup (for deployment)
# --------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    google_api_key="AIzaSyDDANK56dFae3szwkTz5244asYXvD4fykc"
)

# --------------------------------------------
# 2. Prompt Template
# --------------------------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that translates English sentences to French."),
    ("user", "Translate this sentence to French: {sentence}")
])

# --------------------------------------------
# 3. LangChain Runnable Chain
# --------------------------------------------
chain: Runnable = prompt | llm | StrOutputParser()

# --------------------------------------------
# 4. Streamlit UI
# --------------------------------------------
st.set_page_config(page_title="English to French Translator", layout="centered")
st.title("🌍 English to French Translator")

sentence = st.text_input("Enter an English sentence:")

if st.button("Translate"):
    if not sentence.strip():
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            with st.spinner("Translating..."):
                result = chain.invoke({"sentence": sentence})
            st.success("Translation successful!")
            st.markdown(f"**🇫🇷 French Translation:** `{result.strip()}`")
        except Exception as e:
            st.error(f"An error occurred: {e}")
