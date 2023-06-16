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


# 마크다운
# https://heropy.blog/2017/09/30/markdown/
st.title("마크다운")
# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdown -> 명백하게 마크다운을 사용하겠다
st.divider()
st.subheader("제목")
# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""")  # 문자열을 넣으면 마크다운임
st.divider()

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

# 레이아웃
st.divider()
st.subheader("레이아웃")
st.write("""
         ### 순서가 없는 리스트
         1. 순서가
         2. 있는
         4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
            1. 들여쓰기1
                1. 들여쓰기2 #1로 시작하지 않으면 들여쓰기는
                    1. 들여쓰기3
        1. 순서가
        1. 1로 넣어도
        1. 증가됨
        
         * 별 또는 (-)는  여백 1칸 이상과 사용하면 순서가 없는 리스트
         * 별 또는 (-)는  여백 1칸 이상과 사용하면 순서가 없는 리스트
         * 별 또는 (-)는  여백 1칸 이상과 사용하면 순서가 없는 리스트


        $$$ 가로줄
        ---
        (---)
        ___
        (___)
        
        ### 테이블(표)
        |머리|
        |---||---|
        |몸통|
        |이름|직업|
        |파이썬|백수|
        |자바|일잘러|
        |-|-|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MjNfMjYx%2FMDAxNjg0ODQyOTU2MzAy.NqVTY2XhBU4Tv_TNXQ9BB_Mm9TNadkXibZZ_XpDYuxAg.rvcI1B9yOW2yFvekAvsjFKfttnvYw2B_xRCV4P5Mg4sg.PNG.jisoo-060202%2Fimage.png&type=sc960_832"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MjNfMjYx%2FMDAxNjg0ODQyOTU2MzAy.NqVTY2XhBU4Tv_TNXQ9BB_Mm9TNadkXibZZ_XpDYuxAg.rvcI1B9yOW2yFvekAvsjFKfttnvYw2B_xRCV4P5Mg4sg.PNG.jisoo-060202%2Fimage.png&type=sc960_832)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MjNfMjYx%2FMDAxNjg0ODQyOTU2MzAy.NqVTY2XhBU4Tv_TNXQ9BB_Mm9TNadkXibZZ_XpDYuxAg.rvcI1B9yOW2yFvekAvsjFKfttnvYw2B_xRCV4P5Mg4sg.PNG.jisoo-060202%2Fimage.png&type=sc960_832)
    
    
    
""")

#인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가 멋진 말 - 유명한 사람
    
    > 진입장벽은 수익이다 - 어느 코딩 강사
    
    책이나, 사람말 인용할 떄...
    >인용 첫줄
    > > 인용문 안에 인용문

    ### 코드
    '코드를 나타낼 떄 주로 쓰이는 묶음 표시'
    '''
         
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면..:
    print("파이썬!")
    '''
    '''python
    print("파이썬")
    '''
""")


import streamlit as st

st.title("컴포넌트")
# 위-아래로 한줄로만...
st.write("🍉")
cols = st.columns(2) # 컬럼 리스트
cols[0].write("🍉")
cols[1].write("🍉")

cols = st.columns(3)
# 🌋 -> n 등분 -> 3등분
cols[0].write("🌋")
cols[1].write("🌋")
cols[-1].write("🌋")
cols = cols[0].columns(3) # 열의 열린 거임
cols[0].write("🌋")
cols[1].write("🌋")
cols[-1].write("🌋")
col1, col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1:
    st.write("왼쪽")
# col1을 기준으로 streamlit을 써주겠다
# 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
with col2:
    st.write("오른쪽")

# tabs = st.tabs(["김치찌개", "된장찌개", "로제마라어묵찌개"])
tab_meuns = ["김치찌개", "된장찌개", "로제마라어묵찌개"]
tab1, tab2, tab3 = st.tabs(tab_meuns)
img1 = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA0MTJfMTg1%2FMDAxNjgxMjk1NzY4MTA3.byuBE3llW2ljkxpopgBTZRrbxZ-tz4SZNa20DmY0Ylsg.MqfIeGQZvtz25GXK1eBDeQtD5ZZxjwiPWIawS6pdr2gg.JPEG.iamjieunpark%2F1681295600930.jpg&type=sc960_832"
tab1.image(img1)
with tab2:
    img2 ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MThfMjEx%2FMDAxNjg0MzY5NDYzMTU1.w1M2SqkJHLAGvGaj-fb3VGLtjHpdgpTqDFWrRxaOB-sg.iNA0Z1LzkUvKyeBH1HHdKTS9cUp5HnJcOSzpv5Qch68g.JPEG.cera23%2FIMG_3947.JPG&type=sc960_832"
    st.image(img2)
tab3.write("이런건 없어요...상상도 마라요")

exp = st.expander("Surprise!!!", expanded=False)
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# whit exp: ...

# 입력
st.title("입력")
# st.text_input("나의 이름은")
name = st.text_input("나의 이름은") # 변수로 받을수있음
name2 = st.text_input("너의 이름은") # 변수로 받을수있음
# st.text_input("")  -> 이것도 가능
# st.write(name)
# st.write(name2)
st.write(f"신랑 {name}과 신부{name2}는 ...")
# number = st.number_input("당신의 나이는?")
number = st.number_input("당신의 나이는?", step=1) # step는 하나의
# st.write(f"나의 나이는 {number}세")
age = st.number_input(f"나의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")
height = st.number_input("당신의 키는?", step=10)
st.write(f"나의 키는 {height}cm")
# https://docs.streamlit.io/library/api-reference/widgets


st.divider()
mode = st.checkbox('강사님 잔소리모드')  # bool (T/F)
r = st.radio("잔소리 내용 선택", ["취업", "지각", "코딩"])
if mode:
    # r -> 취업, 코딩, 지각
    if r == "취업":
        for i in range(s):
            st.write("여러분 8월에는 자소서 넣어야겠죠?")
    elif r == "코딩":
        st.write("저보다 파이썬 잘해요?")
    elif r == "지각":
        st.write("9시랑 9시 1분은 다른 거예요")

