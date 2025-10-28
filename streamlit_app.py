import streamlit as st
import datetime

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="나만의 오늘과 특별한 날",
    page_icon="🗓️",
    layout="centered"
)

# --- CSS 스타일 추가 (달력 스타일 포함) ---
st.markdown("""
<style>
/* ... (이전 CSS 스타일은 동일하게 유지) ... */
h1 { color: #2F4F4F; text-align: center; font-size: 3em; }
h2 { color: #4682B4; font-size: 2.2em; border-bottom: 2px solid #B0C4DE; padding-bottom: 0.3em; }
h3 { color: #5F9EA0; font-size: 1.8em; }
div.stButton > button {
    width: 100%; height: 60px; margin-bottom: 10px; font-size: 18px; font-weight: bold;
    color: white; background-color: #6A5ACD; border: none; border-radius: 12px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2); transition: all 0.2s ease-in-out;
}
div.stButton > button:hover { background-color: #483D8B; transform: translateY(-2px); }
.stAlert.success { background-color: #E0FFE0; color: #2E8B57; border-left: 5px solid #3CB371; }
.stAlert.info { background-color: #E6F3FF; color: #4169E1; border-left: 5px solid #6495ED; }
.quiz-box { background-color: #FFFACD; border: 2px dashed #FFD700; border-radius: 10px; padding: 15px 20px; margin-top: 20px; }
.youtube-link {
    display: inline-block; background-color: #FF0000; color: white; padding: 10px 15px;
    border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 1.2em; margin-top: 10px;
}
.youtube-link:hover { background-color: #CC0000; color: white; }

/* === 새로 추가된 달력 테이블 스타일 === */
.calendar-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    font-size: 1.1em;
}
.calendar-table th {
    background-color: #4682B4; /* Steel Blue */
    color: white;
    padding: 10px;
    text-align: center;
}
.calendar-table td {
    border: 1px solid #B0C4DE; /* Light Steel Blue */
    padding: 15px 10px;
    height: 80px;
    text-align: right;
    vertical-align: top;
    font-weight: bold;
    color: #555;
}
/* 오늘이 아닌 다른 달의 날짜 (여기서는 비워둠) */
.calendar-table .empty {
    background-color: #f8f8f8;
}
/* 특별한 날 스타일 */
.calendar-table .special-day {
    background-color: #E6F3FF; /* Light Blue */
    color: #4169E1; /* Royal Blue */
}
.calendar-table .special-day .day-number {
    font-size: 1.2em;
}
.calendar-table .special-day .day-emoji {
    font-size: 1.5em;
    display: block;
    text-align: center;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)


# --- 10월 특별한 날 데이터 (이미지 키 제거) ---
special_days = {
    3: {"event": "개천절 🇰🇷", "desc": "우리나라가 처음 세워진 날을 기념해요.", "emoji": "🇰🇷"},
    9: {"event": "한글날 👑", "desc": "세종대왕님이 우리 글 '한글'을 만드신 날이에요.", "emoji": "👑", "youtube_link": "https://youtu.be/itrj1bNww2c?si=espynvLXhNL1flPx"},
    15: {"event": "체육의 날 💪", "desc": "우리 몸을 튼튼하게! 즐겁게 운동하는 날이에요.", "emoji": "💪"},
    30: {"event": "🍁 가을 소풍", "desc": "OO 공원으로 소풍을 가요! 정말 기대돼요!", "emoji": "🚌", "prep": "개인 도시락, 물통, 모자, 편한 운동화"},
    31: {"event": "🎃 핼러윈 파티", "desc": "즐거운 간식 파티를 준비해요! 기대해주세요!", "emoji": "🎃"}
}

# --- 달력 생성 함수 (10월 기준) ---
def generate_october_calendar(special_data):
    """
    10월 달력 HTML을 생성합니다.
    2024년 10월 1일은 화요일(weekday=1)이었습니다. 이를 기준으로 합니다.
    (일=0, 월=1, 화=2, 수=3, 목=4, 금=5, 토=6)
    """
    start_day_of_week = 2  # 10월 1일의 요일 (화요일=2)
    
    calendar_html = "<table class='calendar-table'>"
    # 요일 헤더
    calendar_html += "<thead><tr><th>일</th><th>월</th><th>화</th><th>수</th><th>목</th><th>금</th><th>토</th></tr></thead>"
    calendar_html += "<tbody><tr>"
    
    # 1일 전 빈 칸 채우기
    for _ in range(start_day_of_week):
        calendar_html += "<td class='empty'></td>"
        
    # 날짜 채우기 (1일부터 31일)
    for day_num in range(1, 32):
        # 특별한 날인지 확인
        if day_num in special_data:
            day_info = special_data[day_num]
            cell_content = f"<span class='day-number'>{day_num}</span><span class='day-emoji'>{day_info['emoji']}</span>"
            calendar_html += f"<td class='special-day'>{cell_content}</td>"
        else:
            calendar_html += f"<td>{day_num}</td>"
        
        # 토요일(요일 인덱스 6)이면 줄바꿈
        if (day_num + start_day_of_week) % 7 == 0:
            calendar_html += "</tr><tr>"
            
    # 마지막 주 빈 칸 채우기
    current_weekday = (31 + start_day_of_week) % 7
    if current_weekday != 0:
        for _ in range(7 - current_weekday):
            calendar_html += "<td class='empty'></td>"
            
    calendar_html += "</tr></tbody></table>"
    return calendar_html

# --- 앱 제목 ---
st.title("🗓️ 나만의 오늘과 특별한 날")


# --- 1. '오늘' 확인하기 (날짜/요일/날씨) ---
st.header("1. ☀️ '오늘'은 며칠일까요? (10월)")

col1, col2, col3 = st.columns(3)
with col1:
    month = st.selectbox("몇 월?", ["10월"], key="month_select")
with col2:
    day = st.selectbox("며칠?", list(range(1, 32)), key="day_select")
with col3:
    weekday = st.selectbox("무슨 요일?", ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"], key="weekday_select")

st.write("오늘 날씨는 어때요? (골라주세요)")
weather_icons = {"맑음 ☀️": "☀️", "흐림 ☁️": "☁️", "비 ☔": "☔", "눈 ❄️": "❄️"}
selected_weather = st.radio("", list(weather_icons.keys()), horizontal=True, label_visibility="collapsed", key="weather_radio")

if st.button("짠! 확인하기 ✨"):
    st.session_state.today_date = day
    
    st.success(f"딩동댕! 오늘은 {month} {day}일 {weekday}, {selected_weather}입니다!")
    st.balloons() 

    if day in special_days:
        st.info(f"🎉 와! 그리고 오늘은 **{special_days[day]['event']}**이기도 해요!")


# --- 2. '10월' 탐색하기 (계기 교육) ---
st.header("2. 🍂 10월의 특별한 날들을 탐색해봐요!")

# 10월 달력 표 삽입
st.markdown(generate_october_calendar(special_days), unsafe_allow_html=True)

st.write("궁금한 날짜의 버튼을 눌러보세요!")

# 버튼 컬럼 배치 (3개씩 묶어서)
btn_cols = st.columns(3)
day_keys = sorted(special_days.keys()) # 날짜 순서대로 정렬

for i, day_num in enumerate(day_keys):
    with btn_cols[i % 3]: # 3개씩 배치
        day_info = special_days[day_num]
        if st.button(f"{day_info['emoji']} 10월 {day_num}일 ({day_info['event'].split(' ')[0]})", key=f"btn_{day_num}"):
            st.subheader(f"{day_info['emoji']} {day_info['event']}")
            # st.image(day_info["image"], use_column_width=True) # 이미지 코드 제거
            st.write(day_info["desc"])

            # --- 한글날 특별 활동 (링크, 퀴즈) ---
            if day_num == 9:
                # 유튜브 링크
                st.markdown(f"""
                <a href="{day_info['youtube_link']}" target="_blank" class="youtube-link">
                    🎵 한글송 동요 듣기 🇰🇷 (클릭)
                </a>
                """, unsafe_allow_html=True)
                st.write(" ") # 공백 추가

                # 가사 이미지 관련 코드 모두 제거

                # 복습 퀴즈
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("🧠 복습 퀴즈!")
                
                quiz_question = "가사 내용 중 '훈민정음'은 국보 몇 호일까요?"
                quiz_options = ["10호", "70호", "100호"]
                
                answer = st.radio(quiz_question, quiz_options, key=f"quiz_{day_num}")
                
                if st.button("정답 확인!", key=f"check_{day_num}"):
                    if answer == "70호":
                        st.success("🎉 정답입니다! 훈민정음은 국보 제70호입니다.")
                    else:
                        st.error("😥 아쉬워요! 다시 생각해볼까요?")

                # 부연 설명
                with st.expander("자세히 알아보기 (선생님과 함께 눌러봐요)"):
                    st.write("""
                        - **훈민정음(訓民正音)**은 '백성을 가르치는 바른 소리'라는 뜻이에요.
                        - 우리나라의 **국보 제70호**로 지정되어 있어요.
                        - 1997년에는 **유네스코 세계기록유산**에도 등재되었답니다!
                    """)
                st.markdown('</div>', unsafe_allow_html=True)

            # --- 가을 소풍 특별 활동 (준비물, 기대) ---
            if day_num == 30:
                st.write(f"🎒 **가을 소풍 준비물:** {day_info['prep']}")
                st.text_input("🎉 소풍에서 가장 기대되는 것은 무엇인가요?", key=f"picnic_expect_{day_num}")
                st.radio("소풍이 어땠나요? (다녀온 후)", ["좋았어요 👍", "보통이에요 🙂", "싫었어요 👎"], horizontal=True, key=f"picnic_feeling_{day_num}")
