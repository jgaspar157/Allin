import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = st.secrets[QvfpyQY5BYdPmcfghbl_cwvV9rP0DKgdua0YQITedUJjiVt8MA]  # Store securely in Streamlit secrets

# Streamlit app UI
st.title("ChatGPT Dynamic Answers App")
st.subheader("Ask me anything, and I'll generate a dynamic response!")

# Input field for user questions
user_input = st.text_input("Enter your question or query:")

# Generate response
if user_input:
    try:
        with st.spinner("Generating response..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7,
            )
            answer = response['choices'][0]['message']['content']
            st.success("Response generated!")
            st.write(answer)
    except Exception as e:
        st.error(f"Error: {e}")
