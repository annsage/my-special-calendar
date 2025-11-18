import streamlit as st
import datetime

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="3학년 2반의 기록",
    page_icon="🏫",
    layout="centered"
)

# --- CSS 스타일 추가 (달력 스타일 포함) ---
st.markdown("""
<style>
/* 전체 폰트 설정 */
body {
    font-family: 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
}
/* 앱 제목 */
.stApp > header {
    background-color: transparent;
}
h1 {
    color: #2F4F4F; /* Dark Slate Gray */
    text-align: center;
    font-size: 3em;
    margin-bottom: 0.5em;
}
h2 {
    color: #4682B4; /* Steel Blue */
    font-size: 2.2em;
    border-bottom: 2px solid #B0C4DE; /* Light Steel Blue */
    padding-bottom: 0.3em;
    margin-top: 1.5em;
    margin-bottom: 1em;
}
h3 {
    color: #5F9EA0; /* Cadet Blue */
    font-size: 1.8em;
    margin-top: 1em;
}
/* 버튼 스타일 */
div.stButton > button {
    width: 100%;
    height: 60px;
    margin-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
    color: white;
    background-color: #6A5ACD; /* Slate Blue */
    border: none;
    border-radius: 12px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    transition: all 0.2s ease-in-out;
}
div.stButton > button:hover {
    background-color: #483D8B; /* Dark Slate Blue */
    transform: translateY(-2px);
    box-shadow: 4px 4px 10px rgba(0,0,0,0.3);
}
/* 라디오 버튼 스타일 */
div.stRadio > label {
    font-size: 1.1em;
    font-weight: bold;
    color: #2F4F4F;
}
/* 성공 메시지 */
.stAlert.success {
    background-color: #E0FFE0; /* Light Green */
    color: #2E8B57; /* Sea Green */
    border-left: 5px solid #3CB371; /* Medium Sea Green */
    font-size: 1.2em;
}
/* 정보 메시지 */
.stAlert.info {
    background-color: #E6F3FF; /* Light Blue */
    color: #4169E1; /* Royal Blue */
    border-left: 5px solid #6495ED; /* Cornflower Blue */
    font-size: 1.1em;
}
/* 퀴즈 박스 */
.quiz-box {
    background-color: #FFFACD; /* Lemon Chiffon */
    border: 2px dashed #FFD700; /* Gold */
    border-radius: 10px;
    padding: 15px 20px;
    margin-top: 20px;
}
/* === 달력 테이블 스타일 === */
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
.calendar-table .empty { background-color: #f8f8f8; }
.calendar-table .special-day {
    background-color: #E6F3FF; /* Light Blue */
    color: #4169E1; /* Royal Blue */
}
.calendar-table .special-day .day-number { font-size: 1.2em; }
.calendar-table .special-day .day-emoji {
    font-size: 1.5em;
    display: block;
    text-align: center;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)


# --- 11월 특별한 날 데이터 ---
special_days = {
    3: {"event": "학생마당 🎤", "desc": "우리 반 친구들의 멋진 장기자랑 시간!", "emoji": "🎤"},
    10: {"event": "휠체어 무용 공연 💃", "desc": "아름다운 공연을 관람해요.", "emoji": "💃"},
    14: {"event": "명랑운동회 🏃‍♂️", "desc": "다 함께 으쌰으쌰! 신나는 운동회!", "emoji": "🏃‍♂️"},
    19: {"event": "시간표 맞추기 📝", "desc": "오늘의 시간표를 완성해봐요.", "emoji": "📝"}, # 텍스트 수정
    28: {"event": "책 읽어주시는 선생님 📚", "desc": "재미있는 동화책 이야기 시간!", "emoji": "📚"}
}

# --- 달력 생성 함수 (11월 기준) ---
def generate_november_calendar(special_data):
    """
    11월 달력 HTML을 생성합니다. (2025년 11월 1일은 토요일(weekday=6) 기준)
    (일=0, 월=1, 화=2, 수=3, 목=4, 금=5, 토=6)
    """
    start_day_of_week = 6  # 11월 1일의 요일 (토요일=6)
    
    calendar_html = "<table class='calendar-table'>"
    calendar_html += "<thead><tr><th>일</th><th>월</th><th>화</th><th>수</th><th>목</th><th>금</th><th>토</th></tr></thead>"
    calendar_html += "<tbody><tr>"
    
    # 1일 전 빈 칸 채우기
    for _ in range(start_day_of_week):
        calendar_html += "<td class='empty'></td>"
        
    # 날짜 채우기 (1일부터 30일)
    for day_num in range(1, 31):
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
    current_weekday = (30 + start_day_of_week) % 7
    if current_weekday != 0:
        for _ in range(7 - current_weekday):
            calendar_html += "<td class='empty'></td>"
            
    calendar_html += "</tr></tbody></table>"
    return calendar_html

# --- 앱 제목 ---
st.title("🗓️ 3학년 2반의 기록")


# --- 1. '오늘' 확인하기 (날짜/요일/날씨) ---
st.header("1. ☀️ '오늘'은 며칠일까요? (11월)")

col1, col2, col3 = st.columns(3)
with col1:
    month = st.selectbox("몇 월?", ["11월"], key="month_select")
with col2:
    day = st.selectbox("며칠?", list(range(1, 31)), key="day_select")
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


# --- 2. '11월' 탐색하기 (계기 교육) ---
st.header("2. 🍂 11월의 특별한 날들을 탐색해봐요!")

# 11월 달력 표 삽입
st.markdown(generate_november_calendar(special_days), unsafe_allow_html=True)

st.write("궁금한 날짜의 버튼을 눌러보세요!")

# 버튼 컬럼 배치 (3개씩 묶어서)
btn_cols = st.columns(3)
day_keys = sorted(special_days.keys()) # 날짜 순서대로 정렬

for i, day_num in enumerate(day_keys):
    with btn_cols[i % 3]: # 3개씩 배치
        day_info = special_days[day_num]
        if st.button(f"{day_info['emoji']} 11월 {day_num}일 ({day_info['event'].split(' ')[0]})", key=f"btn_{day_num}"):
            st.subheader(f"{day_info['emoji']} {day_info['event']}")
            st.write(day_info["desc"])

            # --- 학생마당 (3일) ---
            if day_num == 3:
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("🎤 학생마당 기대 활동")
                st.text_input("가장 기대되는 친구의 장기자랑은 무엇인가요?")
                st.info("이 활동은 '국어' > '11월 행사' > '발표 태도 익히기' 자료와 연결됩니다.")
                st.markdown('</div>', unsafe_allow_html=True)

            # --- 휠체어 무용 공연 (10일) ---
            if day_num == 10:
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("💃 공연 관람 예절 퀴즈")
                st.radio("공연을 볼 때의 예절이 아닌 것을 골라보세요.",
                         ["조용히 앉아서 보기", "친구와 큰 소리로 떠들기", "멋진 공연에 박수치기"])
                st.info("이 활동은 '국어' > '11월 행사' > '공연 관람 예절' 자료에서 가져왔습니다.")
                st.markdown('</div>', unsafe_allow_html=True)

            # --- 명랑운동회 (14일) ---
            if day_num == 14:
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("🏃‍♂️ 우리 반 응원 구호")
                st.text_input("우리 반 응원 구호를 힘차게 외쳐보세요!", "예: 3반 이겨라! 👏")
                st.info("이 활동은 '국어' > '11월 행사' > '응원 문구 만들기' 자료와 연결됩니다.")
                st.markdown('</div>', unsafe_allow_html=True)

            # --- [수정됨] 급식/시간표 (19일) ---
            if day_num == 19:
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("📝 11월 19일 (수) 시간표 맞추기")
                st.write("각 교시에 맞는 과목을 선택해 시간표를 완성해보세요!")
                
                # 과목 선택지 (요청하신 목록 그대로, 중복 제거 안 함)
                subjects = [
                    "-선택-", "국어", "창체", "뉴스포츠", "수학", "과학", 
                    "체육", "재활", "진로", "정보", "보건", "수학", 
                    "동아리", "음악", "수중감각", "정보", "미술"
                ]

                # 시간표 테이블 (st.columns 활용)
                col1, col2 = st.columns([1, 3]) # [교시, 과목선택] 비율
                
                with col1:
                    st.write("**1교시**")
                with col2:
                    st.selectbox("1교시 과목", subjects, key="period_1", label_visibility="collapsed")
                
                with col1:
                    st.write("**2교시**")
                with col2:
                    st.selectbox("2교시 과목", subjects, key="period_2", label_visibility="collapsed")

                with col1:
                    st.write("**3교시**")
                with col2:
                    st.selectbox("3교시 과목", subjects, key="period_3", label_visibility="collapsed")

                with col1:
                    st.write("**4교시**")
                with col2:
                    st.selectbox("4교시 과목", subjects, key="period_4", label_visibility="collapsed")

                # 점심시간 (급식 메뉴 입력란 삭제 및 기대 메뉴 추가)
                st.markdown("---") # 구분선
                col1_lunch, col2_lunch = st.columns([1, 3])
                with col1_lunch:
                    st.write("🍽️ **점심시간**")
                with col2_lunch:
                    st.text_input("가장 기대되는 메뉴는 무엇인가요?", key="lunch_menu_expect", placeholder="예: 돈까스!")
                st.markdown("---") # 구분선

                with col1:
                    st.write("**5교시**")
                with col2:
                    st.selectbox("5교시 과목", subjects, key="period_5", label_visibility="collapsed")
                
                with col1:
                    st.write("**6교시**")
                with col2:
                    st.selectbox("6교시 과Mok", subjects, key="period_6", label_visibility="collapsed")

                st.markdown('</div>', unsafe_allow_html=True)

            # --- 책 읽어주시는 선생님 (28일) ---
            if day_num == 28:
                st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
                st.subheader("📚 이야기 감상")
                st.text_area("오늘 들은 이야기 중 가장 기억에 남는 장면은 무엇인가요?", key="reading_response")
                st.info("이 활동은 '국어' > '11월 행사' > '독후 감상 표현하기' 자료와 연결됩니다.")
                st.markdown('</div>', unsafe_allow_html=True)