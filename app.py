# pip install streamlit
# streamlit hello
# ctrl + c : 실행 종료 (터미널)

import streamlit as st
# streamlit -> (가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit 의 기능을 사용하겠다.

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("나의 파이썬 streamlit 웹 페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 페이지, 너를 위해 구웠지")

# streamlit run app.py