# pip install streamlit
# streamlit hello
# ctrl + c : 실행 종료 (터미널)
# streamlit run app.py

import streamlit as st
# streamlit -> (가져오기) -> as (st 이름)
# st라는 변수명으로 streamlit 의 기능을 사용하겠다.

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)을 가지고 있다

st.title("나의 파이썬 streamlit 웹 페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 페이지, 너를 위해 구웠지")

# 기능이 실행되는 순서대로 화면에서 표현
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")  # 유튜브 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/jorp5JH.png")  # 인터넷 링크
# 여러 가지 옵션을 넣어서 세부 기능들을 차이
st.image("img/img.jpeg")  # 파일 경로 (app.py)
st.image(image="img/img.jpeg")  # 키워드를 사용해서...
st.image("img/img.jpeg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img.jpeg", width=100)  # 파일 경로 (app.py)
# https://imgur.com/


# streamlit run app.py

