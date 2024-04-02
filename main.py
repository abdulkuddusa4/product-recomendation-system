import streamlit as st
import pandas as pd
import numpy as np
import openai
import services
from streamlit_chat import message

openai.api_key = "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"

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo-16k",
#   messages=[
#       {
#       "role": "system",
#       "content": "You are a good assistant"
#       },
#       {
#         "role": "user",
#         "content": "hello"
#       }
#   ],
#     # stream=True,
# )

# json_response = completion.choices[0].message.content
javascript_code =f"""
    <script>
        //inputElement = document.getElementsByClassName("stTextInput")[0];
        //inputElement.scrollIntoView({{ behavior: "smooth", block: "center" }});
        console.log(document.getElementsByClassName("stTextInput")[0]);

    </script>
    """
st.title('Product Recomendation System')
#
if "user_input" not in st.session_state:
    st.session_state['user_input'] = None
#
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
try:
    if user_input := st.session_state.get('user_input'):
        with st.container():
            st.session_state['messages'].append((user_input, True))
            response=services.get_agent_response(user_input)
            st.session_state['messages'].append((response, False))
    elif 'chat_history' not in st.session_state:
        with st.container():
            st.session_state['messages'].append((services.get_agent_response(None), False))
except openai.error.RateLimitError as e:
    with st.container():
        st.session_state['chat_history'].pop()
        st.session_state['messages'].append(("plz wait as it is not paid account", False))
finally:
    with st.container():
        st.text_input("user",on_change=lambda :st.components.v1.html(javascript_code),
                      placeholder="query", key="user_input")
    for msg, is_user in st.session_state['messages'].__reversed__():
        message(msg, is_user)
    # scroll_to_input =
    # st.components.v1.html(scroll_to_input)
    # st.markdown(scroll_to_input, unsafe_allow_html=True)
    # st.write(scroll_to_input, unsafe_allow_html=True)
print("end")
#
# with st.container() as cont:
#     cont.
