import streamlit as st

st.title("📱 업무 자동화 모바일 앱")
st.write("VBA 매크로 기능을 구현한 웹 앱 시연 페이지입니다.")

# 입력 창 (VBA 텍스트박스/콤보박스 역할)
name = st.text_input("직원 이름 입력", "홍길동")
work_hours = st.slider("금주 근무 시간", 0, 52, 40)

# 계산 결과 출력 (VBA 메시지박스나 셀 출력 역할)
st.subheader("📊 산출 결과")
if work_hours > 40:
    st.error(f"⚠️ {name}님은 현재 연장 근로 중입니다! (기본 40시간 초과)")
else:
    st.success(f"✅ {name}님은 정상 근무 범위 내에 있습니다.")
