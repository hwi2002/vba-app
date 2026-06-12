import streamlit as st
import time

# 1. 브라우저 레이아웃 및 탭 설정
st.set_page_config(page_title="AI Agent Intelligence", page_icon="🧬", layout="wide")

# 2. 애플 감성 미니멀리즘 CSS 디자인
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .main .block-container {
        font-family: 'Inter', -apple-system, sans-serif !important;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 850px;
    }
    .app-title {
        font-size: 34px !important;
        font-weight: 700 !important;
        color: #111111;
        letter-spacing: -0.8px;
        margin-bottom: 6px;
        text-align: center;
    }
    .app-subtitle {
        font-size: 15px;
        color: #666666;
        text-align: center;
        margin-bottom: 35px;
    }
    .agent-card {
        background: #ffffff;
        padding: 26px 0px;
        border-bottom: 1px solid #eeeeee;
        margin-bottom: 5px;
    }
    .badge-cat {
        font-size: 11px;
        font-weight: 600;
        color: #0066CC;
        background: #F2F7FD;
        padding: 4px 12px;
        border-radius: 6px;
        margin-right: 8px;
    }
    .badge-src {
        font-size: 11px;
        font-weight: 500;
        color: #555555;
        background: #F5F5F7;
        padding: 4px 10px;
        border-radius: 6px;
    }
    .summary-box {
        background: #F9FBF9;
        border-radius: 12px;
        padding: 16px 20px;
        margin-top: 16px;
        font-size: 14px;
        color: #2c3e50;
        line-height: 1.6;
    }
    .text-link {
        display: inline-block;
        font-size: 13px;
        font-weight: 600;
        color: #0066CC !important;
        text-decoration: none !important;
        margin-top: 14px;
    }
    .text-link:hover {
        text-decoration: underline !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 상단 타이틀
st.markdown("<div class='app-title'>AI Agent Intelligence</div>", unsafe_allow_html=True)
st.markdown("<div class='app-subtitle'>글로벌 에이전트 구축 트렌드 및 기술 분석 대시보드</div>", unsafe_allow_html=True)

# 4. 보완 포인트 ①: 대시보드 상단에 시각적 통계 지표(Metrics) 배치
# 발표할 때 "현재 수집된 에이전트 동향 지표입니다" 하고 브리핑하기 좋습니다.
m1, m2, m3 = st.columns(3)
m1.metric(label="📊 이번 주 분석 에이전트", value="147 건", delta="+24건")
m2.metric(label="⚡ 평균 자동화 효율성", value="42.5 %", delta="+3.8%")
m3.metric(label="🔒 보안 검증 통과율", value="99.2 %", delta="정상")
st.markdown("<br>", unsafe_allow_html=True)

# 5. 사이드바 검색 및 필터 레이아웃
st.sidebar.markdown("### 🔍 Filter")

# 보완 포인트 ②: 키워드 검색창 추가 (VBA의 실시간 텍스트 필터 기능 구현)
search_query = st.sidebar.text_input("💡 키워드 검색", "", placeholder="검색어를 입력하세요...")

category = st.sidebar.selectbox(
    "카테고리 선택",
    ["전체 보기", "🛠️ 오픈소스 에이전트 프레임워크", "🏢 기업 업무 자동화 에이전트", "🖥️ 자율형 웹/OS 브라우징 에이전트"]
)
st.sidebar.markdown("---")

with st.sidebar:
    if st.button("🔄 실시간 동기화", use_container_width=True):
        with st.spinner("수집 중..."):
            time.sleep(1)
        st.toast("최신 정보를 동기화했습니다.", icon="✅")

# 6. 트렌디한 실제 최신 에이전트 데이터 세트
ai_news_data = [
    {
        "title": "LangChain 기반 다중 에이전트(Multi-Agent) 협업 툴킷 업데이트",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "LangChain Blog",
        "time": "15분 전",
        "content": "개발자들이 복잡한 워크플로우를 자동화할 수 있도록 여러 개의 AI 에이전트가 서로 대화하며 문제를 해결하는 멀티 에이전트 아키텍처가 고도화되었습니다. 기획, 코딩, 테스트 에이전트가 순차적으로 업무를 수행합니다.",
        "summary": "에이전트 간의 기억(Memory) 공유 메커니즘 개선으로 비즈니스 로직 설계 공수 40% 절감.",
        "url": "https://langchain.com"
    },
    {
        "title": "세일즈포스, 기업 전용 자율형 Agentforce 솔루션 전면 도입 성과 발표",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "TechCrunch",
        "time": "2시간 전",
        "content": "사전 정의된 고정 시나리오 없이 기업의 내부 매뉴얼과 실시간 ERP 데이터를 스스로 판단하여 자율적으로 고객을 응대하고 트랜잭션을 처리하는 자율형 비즈니스 에이전트 인프라가 대거 확산되고 있습니다.",
        "summary": "단순 챗봇을 넘어 기업 API 연동을 통해 백오피스 업무까지 스스로 완결하는 구조 확립.",
        "url": "https://techcrunch.com"
    },
    {
        "title": "앤트로픽(Anthropic), 사람처럼 PC를 자율 제어하는 'Computer Use' API 업그레이드",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Wired",
        "time": "5시간 전",
        "content": "AI가 모니터 화면을 실시간 캡처하여 마우스 커서를 움직이고 키보드를 타이핑하는 자율 제어 기술이 대폭 업데이트되었습니다. 웹사이트 로그인, 엑셀 다운로드, 이메일 전송 등을 끊김 없이 수행합니다.",
        "summary": "VBA 매크로의 완전한 상위 호환 기술로, 화면 UI 구조가 변경되어도 시각 정보로 유연한 처리가 가능함.",
        "url": "https://wired.com"
    }
]

# 7. 보완 포인트 ③: 카테고리 필터와 텍스트 검색을 동시에 반영하는 필터링 로직
has_content = False

for news in ai_news_data:
    # 카테고리 매칭 확인
    category_match = (category == "전체 보기" or news["category"] == category)
    
    # 검색어 매칭 확인 (제목이나 내용에 검색어가 포함되어 있는지 체크)
    search_match = (search_query.lower() in news["title"].lower() or 
                    search_query.lower() in news["content"].lower())
    
    if category_match and search_match:
        has_content = True
        st.markdown(f"""
            <div class='agent-card'>
                <div style='margin-bottom: 12px;'>
                    <span class='badge-cat'>{news['category']}</span>
                    <span class='badge-src'>🌐 {news['source']}</span>
                    <span style='color: #999; font-size: 12px; margin-left: 8px;'>{news['time']}</span>
                </div>
                <h3 style='font-size: 20px; font-weight: 600; color: #111; margin: 0 0 10px 0;'>{news['title']}</h3>
                <p style='color: #555; font-size: 14px; line-height: 1.6; margin: 0;'>{news['content']}</p>
                <div class='summary-box'>
                    <span style='color: #137333; font-weight: 600;'>💡 Briefing :</span> {news['summary']}
                </div>
                <a href='{news['url']}' target='_blank' class='text-link'>🔗 원문 리포트 읽기 →</a>
            </div>
        """, unsafe_allow_html=True)

if not has_content:
    st.info("검색 조건에 맞는 에이전트 분석 리포트가 없습니다.")
