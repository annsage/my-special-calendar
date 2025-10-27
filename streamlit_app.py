import streamlit as st
import datetime

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="나만의 오늘과 특별한 날",
    page_icon="🗓️",
    layout="centered"
)

# --- CSS 스타일 추가 ---
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
/* 이미지 스타일 */
.stImage > img {
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}
/* 입력창 */
.stTextInput > label, .stSelectbox > label {
    font-weight: bold;
    color: #2F4F4F;
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
.quiz-box .stRadio > label {
    font-size: 1.2em;
    color: #8B4513; /* Saddle Brown */
}
/* 유튜브 링크 */
.youtube-link {
    display: inline-block;
    background-color: #FF0000; /* Red */
    color: white;
    padding: 10px 15px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.2em;
    margin-top: 10px;
}
.youtube-link:hover {
    background-color: #CC0000; /* Darker Red */
    color: white;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


# --- 10월 특별한 날 데이터 ---
# (교사가 미리 입력해두는 데이터)
special_days = {
    3: {"event": "개천절 🇰🇷", "image": "https://i.imgur.com/gJqf0aH.png", "desc": "우리나라가 처음 세워진 날을 기념해요.", "emoji": "🇰🇷"},
    9: {"event": "한글날 👑", "image": "https://i.imgur.com/W8nK7XF.png", "desc": "세종대왕님이 우리 글 '한글'을 만드신 날이에요.", "emoji": "👑", "youtube_link": "https://youtu.be/itrj1bNww2c?si=espynvLXhNL1flPx"}, # 유튜브 링크 추가
    15: {"event": "체육의 날 💪", "image": "https://i.imgur.com/7YyNqjJ.png", "desc": "우리 몸을 튼튼하게! 즐겁게 운동하는 날이에요.", "emoji": "💪"},
    30: {"event": "🍁 가을 소풍", "image": "https://i.imgur.com/3dI7yTq.png", "desc": "OO 공원으로 소풍을 가요! 정말 기대돼요!", "emoji": "🚌", "prep": "개인 도시락, 물통, 모자, 편한 운동화"}, # 날짜 수정 및 설명 수정
    31: {"event": "🎃 핼러윈 파티", "image": "https://i.imgur.com/sY9eSgM.png", "desc": "즐거운 간식 파티를 준비해요! 기대해주세요!", "emoji": "🎃"}
}

# --- 앱 제목 및 초기 캘린더 이미지 ---
st.title("🗓️ 나만의 오늘과 특별한 날")

# 시작 시 캘린더 그림
st.image("https://i.imgur.com/4N3qVnF.png", caption="오늘도 즐거운 하루가 시작될 거예요!", use_column_width=True)


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
st.write("궁금한 날짜의 버튼을 눌러보세요!")

# 버튼 컬럼 배치 (3개씩 묶어서)
btn_cols = st.columns(3)
day_keys = sorted(special_days.keys()) # 날짜 순서대로 정렬

for i, day_num in enumerate(day_keys):
    with btn_cols[i % 3]: # 3개씩 배치
        day_info = special_days[day_num]
        if st.button(f"{day_info['emoji']} 10월 {day_num}일 ({day_info['event'].split(' ')[0]})", key=f"btn_{day_num}"):
            st.subheader(f"{day_info['emoji']} {day_info['event']}")
            st.image(day_info["image"], use_column_width=True)
            st.write(day_info["desc"])

            # --- 한글날 특별 활동 (링크, 가사, 퀴즈) ---
            if day_num == 9:
                # 유튜브 링크 (st.markdown 활용)
                st.markdown(f"""
                <a href="{day_info['youtube_link']}" target="_blank" class="youtube-link">
                    🎵 한글송 동요 듣기 🇰🇷 (클릭)
                </a>
                """, unsafe_allow_html=True)
                st.write(" ") # 공백 추가

                # 가사 이미지
                st.subheader("🖼️ 한글송 가사 보기")
                
                # !!! 중요 !!!
                # 선생님께서 올려주신 '한글송 가사판 (덕지쌤).jpg' 이미지의 URL을 여기에 넣어주세요.
                # (예: Imgur, Google Drive 공유 링크 등)
                YOUR_IMAGE_URL_HERE = "https://placehold.co/600x800/FFFACD/8B4513?text=여기에+가사+이미지+URL을+넣어주세요!"
                
                if YOUR_IMAGE_URL_HERE == "https://placehold.co/600x800/FFFACD/8B4513?text=여기에+가사+이미지+URL을+넣어주세요!":
                    st.warning("코드의 YOUR_IMAGE_URL_HERE 부분에 실제 가사 이미지 URL을 넣어주셔야 이미지가 보입니다.")
                st.image(YOUR_IMAGE_URL_HERE, caption="한글송 가사")

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
