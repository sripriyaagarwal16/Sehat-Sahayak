# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai
# print("google.generativeai module imported successfully")

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-pro") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
    

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get responses from the Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Healthcare Assistant")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input box for user queries
input = st.text_input("Ask your question:", key="input")
submit = st.button("Submit")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
# Display the chat history in a sidebar
with st.sidebar:
    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

# Styling for a better chatbox experience
st.markdown("""
<style>
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
    }
    .chat-message {
        margin-bottom: 5px;
        padding: 10px;
        border-radius: 5px;
    }
    .chat-message.user {
        background-color: #e0f7fa;
        text-align: left;
    }
    .chat-message.bot {
        background-color: #fff9c4;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)
