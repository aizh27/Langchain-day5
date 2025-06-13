import os
import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import Runnable
# :closed_lock_with_key: Set your Gemini API key here
os.environ["GOOGLE_API_KEY"] = "AIzaSyDDANK56dFae3szwkTz5244asYXvD4fykc"
# :dart: Streamlit UI
st.set_page_config(page_title="English to French Translator", page_icon=":earth_africa:")
st.title(":earth_africa: English to French Translator")
st.markdown("This app uses **Google Gemini via LangChain** to translate English text to French.")
# :inbox_tray: User input
english_text = st.text_input("Enter an English sentence:")
# :arrows_counterclockwise: Button to trigger translation
if st.button("Translate to French"):
    if not english_text.strip():
        st.warning("Please enter a sentence before translating.")
    else:
        try:
            # :brain: LLM setup
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)
            # :receipt: Prompt template
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that translates English to French."),
                ("user", "Translate this sentence: {text}")
            ])
            # :link: Chain: prompt | llm
            chain: Runnable = prompt | llm
            # :test_tube: Run the chain
            response = chain.invoke({"text": english_text})
            # :white_check_mark: Display result
            st.success("Translation successful!")
            st.markdown(f"**French Translation:**\n\n> {response.content}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
