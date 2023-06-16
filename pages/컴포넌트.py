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

# tabs = st.tabs(["김치찌ㅉ개", "된장찌개", "로제마라어묵찌개"])
tab_meins = ["김치찌ㅉ개", "된장찌개", "로제마라어묵찌개"]
tab1, tab2, tab3 = st.tabs(tab_meuns)
img1 = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA0MTJfMTg1%2FMDAxNjgxMjk1NzY4MTA3.byuBE3llW2ljkxpopgBTZRrbxZ-tz4SZNa20DmY0Ylsg.MqfIeGQZvtz25GXK1eBDeQtD5ZZxjwiPWIawS6pdr2gg.JPEG.iamjieunpark%2F1681295600930.jpg&type=sc960_832"
tab1.image(img1)
with tab2:
    img2 ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMjBfMTU3%2FMDAxNjc5MzA1NDUyOTU0.C3XnDShbwPp0HSvvRIF8yzxiTmce3evvJJTk_VzlNvQg.K1GGfilZprrzX_EoC1iKE9SOipaHZGwI4Zi7Y6CqLacg.JPEG.bdan9333%2FIMG_0071.JPG&type=sc960_832"
    st.image(img2)
tab3.write("이런건 없어요...상상도 마라요")

exp = st.expander("Surprise!!!", expanded=false)
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

st.divider()
mode = st.checkbox('강사님 잔소리모드')  # bool (T/F)
col1, col2, col3 = st.columns(3)
r = col2.radio("잔소리 내용 선택", ["취업", "지각", "코딩"])
s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)    # min_value, max_value 목소리 낮추는 옵션
b = col3.selectbox("잔소리 말투 선택",["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야! {x}"
    elif b == "모욕적":
        format = lambda x: f"xxxxx! {x}"
    if r == "취업":
        for i in range(s):
            st.write(format("여러분 8월에는 자소서 넣어야겠죠?"))
    elif r == "코딩":
        st.write(format("저보다 파이썬 잘해요?"))
    elif r == "지각":
        st.write(format("9시랑 9시 1분은 다른 거예요"))


