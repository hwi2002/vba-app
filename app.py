import streamlit as st
import time

# 1. 앱 기본 설정 (웹 브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="AI Insight Studio", page_icon="⚡", layout="wide")

# 2. 고급스러운 다크/블루 테마 세련된 CSS 디자인 주입 (VBA의 스타일 시체 역할)
st.markdown("""
    <style>
    /* 메인 배경색 및 글꼴 변경 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    h1 {
        font-weight: 800 !important;
        background: linear-gradient(45deg, #FF4B4B, #4A90E2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
    }
    /* 카드 디자인 투명하고 입체감 있게 변경 */
    .news-card {
        background: #ffffff;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 24px;
        border: 1px solid #eaeaea;
        transition: all 0.3s ease;
    }
    .news-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(74,144,226,0.15);
        border-color: #4A90E2;
    }
    /* 출처 태그 스타일 */
    .source-tag {
        background: #F0F2F6;
        color: #555;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin-right: 8px;
    }
    .category-tag {
        background: #E8F0FE;
        color: #1A73E8;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 타이틀 섹션
st.markdown("<h1 style='text-align: center; margin-bottom: 5px;'>⚡ AI INSIGHT STUDIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 16px; margin-bottom: 30px;'>카테고리별 글로벌 최신 AI 기술 크롤링 및 실시간 핵심 요약 시스템</p>", unsafe_allow_html=True)

# 4. 사이드바 메뉴 디자인 (정돈된 레이아웃)
st.sidebar.markdown("### 📂 기술 카테고리")
category = st.sidebar.selectbox(
    "필터링할 AI 분야를 지정하세요:",
    ["전체 보기", "🚀 LLM & 생성형 AI", "💻 AI 하드웨어/반도체", "🤖 컴퓨터 비전 & 로봇", "⚖️ AI 윤리 및 트렌드"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ 시스템 상태")
st.sidebar.success("정상 작동 중 (Connected)")
st.sidebar.caption("본 앱은 Python Streamlit 인프라와 GitHub Actions 데이터 파이프라인을 기반으로 구동됩니다.")

# 5. 뉴스 데이터 세트 (깔끔하게 재정비)
ai_news_data = [
    {
        "title": "GPT-5 예상 스펙 독점 공개... 차세대 추론 엔진 탑재",
        "category": "🚀 LLM & 생성형 AI",
        "source": "TechCrunch",
        "time": "10분 전",
        "content": "오픈AI의 차세대 거대언어모델(LLM) GPT-5의 내부 테스트 결과가 일부 유출되었습니다. 복잡한 수학적 추론과 다단계 논리 결합 능력이 비약적으로 상승하여 인간 전문가의 추론 능력에 도달했다는 평가입니다.",
        "summary": "핵심 로직 성능 전작 대비 250% 개선, 코딩 및 전문 업무 완전 자동화 타깃."
    },
    {
        "title": "차세대 하이브리드 NPU 반도체 출시, 전력 효율 3배 향상",
        "category": "💻 AI 하드웨어/반도체",
        "source": "Wired",
        "time": "42분 전",
        "content": "대규모 데이터센터의 고질적인 전력 및 발열 문제를 해결하기 위한 초저전력 하드웨어가 글로벌 반도체 연합에 의해 공개되었습니다. 기존 GPU 대비 전력 효율성을 극대화하여 유지 비용을 획기적으로 낮췄습니다.",
        "summary": "추론 프로세스 연산 속도는 유지하면서 탄소 배출 및 전기 소모량 50% 절감 성공."
    },
    {
        "title": "인간 수준의 미세 촉각 센서를 구현한 AI 로봇 핸드 개발",
        "category": "🤖 컴퓨터 비전 & 로봇",
        "source": "MIT Tech Review",
        "time": "2시간 전",
        "content": "시각 센서 데이터와 표면 촉각 압력 데이터를 실시간으로 융합하는 고도화된 딥러닝 알고리즘이 발표되었습니다. 계란이나 얇은 유리잔처럼 파손되기 쉬운 물체를 파손 없이 정밀하게 제어하는 인체 모방형 로봇입니다.",
        "summary": "물체의 강도를 실시간 인지하여 적절한 악력을 피드백 루프로 계산하는 핵심 특허 확보."
    },
    {
        "title": "글로벌 AI 저작권 통합 가이드라인 확정... 무단 크롤링 전면 규제",
        "category": "⚖️ AI 윤리 및 트렌드",
        "source": "Bloomberg",
        "time": "4시간 전",
        "content": "주요 선진 정부 협의체가 AI 모델 학습 데이터에 무단으로 사용되던 콘텐츠 창작자들의 저작권 보호 가이드라인에 전격 합의했습니다. 향후 합당한 로열티 정산 파이프라인 구축이 의무화됩니다.",
        "summary": "글로벌 빅테크 기업들의 무분별한 데이터 스크래핑 제동 및 투명성 리포트 제출 의무화."
    }
]

# 6. 상단 크롤링 버튼 (VBA 매크로 단추 클릭 연출)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔄 실시간 에이전트 크롤링 및 AI 요약 파이프라인 가동", use_container_width=True):
        with st.spinner("해외 주요 테크 미디어(RSS/API) 데이터를 스크래핑하는 중..."):
            time.sleep(1.2)
        st.balloons() # 축하 풍선 이펙트!

st.markdown("<br>", unsafe_allow_html=True)

# 7. 뉴스 카드 출력 섹션
for news in ai_news_data:
    if category == "전체 보기" or news["category"] == category:
        # 커스텀 HTML과 스트림릿 레이아웃 결합하여 고급 카드 UI 구현
        st.markdown(f"""
            <div class="news-card">
                <span class="category-tag">{news['category']}</span>
                <span class="source-tag">🌐 {news['source']}</span>
                <span style="color: #999; font-size: 13px;">🕒 {news['time']}</span>
                <h3 style="margin-top: 12px; color: #111; font-weight: 700;">{news['title']}</h3>
                <p style="color: #444; font-size: 15px; line-height: 1.6; margin-top: 10px;">{news['content']}</p>
                <div style="background: #FAF8F5; border-left: 4px solid #FF4B4B; padding: 12px 16px; border-radius: 4px; margin-top: 15px;">
                    <strong style="color: #FF4B4B; font-size: 14px;">💡 AI 자동 요약 비서 브리핑:</strong>
                    <p style="color: #333; font-size: 14px; margin-bottom: 0; margin-top: 4px; font-weight: 500;">{news['summary']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
