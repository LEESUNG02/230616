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

st.image("img/img.jpeg")  # 파일 경로 (app.py)
st.image(image="img/다운로드.jpeg")  # 키워드를 사용해서...
st.image("img/다운로드.jpeg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/다운로드.jpeg", width=100)  # 파일 경로 (app.py)

# https://imgur.com/



# streamlit run app.py
# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdown -> 명백하게 마크다운을 사용하겠다

stt.write# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""") # 문자열을 넣으면 마크다운임

# 서식
text = """
기울임 : *별표* 또는 _언더바_ 하나씩 써주면

진하게(bold) : **별표** 또는 __언더바__ 두개씩 써주면

기울임 + 진하게(bold) : ***별표*** 또는 ___언더바___ 세개씩 써주면

(읽히는 순서 기울임 -> 기울밈+잔하게 -> 진하게 순임)

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark> 

"""

# st.write(text)
# 태그를 허용하는 옵션
st.markdown(text, unsafe_allow_html=True)