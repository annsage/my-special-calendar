import streamlit as st
import datetime

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="나만의 오늘과 특별한 날",
    page_icon="🗓️",
    layout="centered"
)

# --- 10월 특별한 날 데이터 ---
# (교사가 미리 입력해두는 데이터)
special_days = {
    3: {"event": "개천절 🇰🇷", "image": "https://i.imgur.com/gJqf0aH.png", "desc": "우리나라가 처음 세워진 날을 기념해요."},
    9: {"event": "한글날 👑", "image": "https://i.imgur.com/W8nK7XF.png", "desc": "세종대왕님이 우리 글 '한글'을 만드신 날이에요."},
    15: {"event": "체육의 날 💪", "image": "https://i.imgur.com/7YyNqjJ.png", "desc": "우리 몸을 튼튼하게! 즐겁게 운동하는 날이에요."},
    17: {"event": "🍁 가을 소풍 (경험)", "image": "https://i.imgur.com/3dI7yTq.png", "desc": "OO 공원에서 단풍잎을 주웠어요. 정말 즐거웠어요!"},
    31: {"event": "🎃 핼러윈 파티 (예정)", "image": "https://i.imgur.com/sY9eSgM.png", "desc": "즐거운 간식 파티를 준비해요! 기대해주세요!"}
}

# --- 앱 제목 ---
st.title("🗓️ 나만의 오늘과 특별한 날")
st.subheader("10월 달력과 계기 교육")

# --- 1. '오늘' 확인하기 (날짜/요일/날씨) ---
st.header("1. ☀️ '오늘'은 며칠일까요?")

col1, col2, col3 = st.columns(3)
with col1:
    month = st.selectbox("몇 월?", ["10월"], key="month")
with col2:
    # 1일부터 31일까지 선택지
    day = st.selectbox("며칠?", list(range(1, 32)), key="day")
with col3:
    weekday = st.selectbox("무슨 요일?", ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"], key="weekday")

st.write("오늘 날씨는 어때요? (골라주세요)")
weather_icons = {"맑음 ☀️": "☀️", "흐림 ☁️": "☁️", "비 ☔": "☔", "눈 ❄️": "❄️"}
selected_weather = st.radio("", list(weather_icons.keys()), horizontal=True, label_visibility="collapsed")

if st.button("짠! 확인하기"):
    st.session_state.today_date = day  # 선택한 날짜 저장
    
    st.success(f"딩동댕! 오늘은 {month} {day}일 {weekday}, {selected_weather}입니다!")
    st.balloons() # 확인 시 풍선 효과

    # 선택한 날짜가 특별한 날인지 확인
    if day in special_days:
        st.info(f"와! 그리고 오늘은 **{special_days[day]['event']}**이기도 해요!")


# --- 2. '10월' 탐색하기 (계기 교육) ---
st.header("2. 🍂 10월의 특별한 날")
st.write("궁금한 날짜의 버튼을 눌러보세요!")

# CSS를 이용해 버튼을 가로로 정렬 (학생들이 누르기 쉽게)
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    height: 60px;
    margin-bottom: 10px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# 3줄로 나눠서 버튼 표시
row1_cols = st.columns(3)
row2_cols = st.columns(2)

# 버튼 클릭으로 특별한 날 정보 보기
if row1_cols[0].button("🇰🇷 10월 3일 (개천절)"):
    day_info = special_days[3]
    st.image(day_info["image"])
    st.subheader(f"오늘은 **{day_info['event']}**입니다.")
    st.write(day_info["desc"])

if row1_cols[1].button("👑 10월 9일 (한글날)"):
    day_info = special_days[9]
    st.image(day_info["image"])
    st.subheader(f"오늘은 **{day_info['event']}**입니다.")
    st.write(day_info["desc"])
    
    # 국어과 연계 (한글 써보기)
    st.text_input("✍️ '고맙습니다'라고 한글로 써볼까요?")

if row1_cols[2].button("💪 10월 15일 (체육의 날)"):
    day_info = special_days[15]
    st.image(day_info["image"])
    st.subheader(f"오늘은 **{day_info['event']}**입니다.")
    st.write(day_info["desc"])
    st.radio("무슨 운동을 좋아해요?", ["달리기", "축구", "줄넘기"], horizontal=True)

if row2_cols[0].button("🍁 10월 17일 (가을 소풍)"):
    day_info = special_days[17]
    st.image(day_info["image"])
    st.subheader(f"**{day_info['event']}** (어제 있었던 일)")
    st.write(day_info["desc"])
    
    # 국어과 연계 (경험 나누기)
    st.radio("소풍이 어땠나요?", ["좋았어요 👍", "보통이에요 🙂", "싫었어요 👎"], horizontal=True)

if row2_cols[1].button("🎃 10월 31일 (핼러윈)"):
    day_info = special_days[31]
    st.image(day_info["image"])
    st.subheader(f"**{day_info['event']}** (기다려지는 날)")
    st.write(day_info["desc"])