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


