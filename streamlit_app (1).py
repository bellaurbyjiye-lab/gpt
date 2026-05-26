import streamlit as st
from openai import OpenAI

st.title("LLM 응답 웹 앱")

# API Key를 session_state에 저장
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key = st.text_input(
    "OpenAI API Key",
    type="password",
    value=st.session_state.api_key
)

if api_key:
    st.session_state.api_key = api_key

@st.cache_data
def get_llm_response(api_key, prompt):
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt
    )
    return response.output_text

prompt = st.text_area("질문을 입력하세요")

if st.button("Ask", disabled=(not api_key or not prompt)):
    answer = get_llm_response(api_key, prompt)
    st.write(answer)
