# 필요한 라이브러리를 가져옵니다.
# streamlit은 웹 앱을 위해, random은 문구를 무작위로 선택하기 위해 필요합니다.
import streamlit as st
import random

# --- 페이지 기본 설정 ---
# set_page_config는 앱의 제목과 아이콘을 설정하며, 가장 먼저 실행되어야 합니다.
st.set_page_config(
    page_title="교사용 응원 카드",
    page_icon="💌", # 이모지는 여기서 바꿀 수 있어요.
    layout="centered"
)

# --- 응원 문구 리스트 ---
# 선생님께서 자유롭게 추가, 수정, 삭제하실 수 있는 공간입니다.
# 이 리스트에 있는 문구 중 하나가 무작위로 표시됩니다.
encouragement_messages = [
    "선생님의 작은 관심이 한 아이의 우주를 만듭니다.",
    "오늘도 아이들의 성장에 함께해주셔서 감사합니다.",
    "가르침은 세상을 바꾸는 가장 강력한 무기입니다.",
    "선생님의 열정은 교실의 빛입니다. 스스로를 믿으세요!",
    "지친 하루 끝에, 선생님의 노력이 누군가에겐 큰 힘이 되었음을 기억하세요.",
    "아이들의 웃음은 선생님의 훌륭한 가르침에 대한 보답입니다.",
    "괜찮아요, 때로는 실수해도 됩니다. 완벽하지 않아도 최고의 선생님입니다.",
    "선생님은 그냥 지식을 전달하는 사람이 아니라, 가능성을 심어주는 사람입니다.",
    "오늘 하루도 정말 수고 많으셨습니다. 잠시 쉬어가도 괜찮아요.",
    "세상에서 가장 중요한 일 중 하나를 하고 계십니다. 자부심을 가지세요!"
]

# --- 세션 상태(Session State) 초기화 ---
# st.session_state는 앱이 재실행되어도 데이터를 기억하게 해주는 특별한 공간입니다.
# 'current_quote'는 현재 화면에 표시된 응원 문구를 저장합니다.
if 'current_quote' not in st.session_state:
    st.session_state.current_quote = "버튼을 눌러 오늘의 응원을 확인하세요!"
# 'previous_quote'는 바로 이전에 봤던 응원 문구를 저장합니다.
if 'previous_quote' not in st.session_state:
    st.session_state.previous_quote = "아직 이전 응원 기록이 없어요."

# --- 앱 UI 구성 ---
st.title("💌 교사용 응원 카드")
st.write("---")
st.markdown("매일 고생하시는 선생님들을 위해, 작은 위로와 응원의 메시지를 전합니다.")

# st.columns를 사용해 버튼들을 가로로 나란히 배치합니다.
col1, col2 = st.columns(2)

with col1:
    # '오늘의 응원 받기' 버튼
    if st.button("오늘의 응원 받기", use_container_width=True):
        # 1. 현재 문구를 '이전 문구'로 저장합니다.
        st.session_state.previous_quote = st.session_state.current_quote
        
        # 2. 새로운 문구를 무작위로 선택합니다.
        #    (단, 현재 문구와 똑같은 것이 뽑히지 않도록 방지)
        new_quote = random.choice(encouragement_messages)
        while new_quote == st.session_state.current_quote:
            new_quote = random.choice(encouragement_messages)
        
        # 3. 새로 뽑은 문구를 '현재 문구'로 업데이트합니다.
        st.session_state.current_quote = new_quote

with col2:
    # '이전 응원 다시 보기' 버튼
    if st.button("이전 응원 다시 보기", use_container_width=True):
        # 현재 문구와 이전 문구를 서로 맞바꿉니다.
        # 임시 변수(temp)를 활용하여 값을 교환합니다.
        temp = st.session_state.current_quote
        st.session_state.current_quote = st.session_state.previous_quote
        st.session_state.previous_quote = temp

st.write("---")

# 현재 응원 문구를 예쁜 상자 안에 표시합니다.
st.success(f"**{st.session_state.current_quote}**")

st.markdown(
    """
    <style>
    /* 버튼과 UI 요소들의 디자인을 깔끔하게 조정합니다 (선택사항) */
    .stButton>button {
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)