import streamlit as st
import time

# 1. 브라우저 레이아웃 및 탭 설정
st.set_page_config(page_title="AI Agent Trends", page_icon="🧬", layout="wide")

# 2. 애플 감성 미니멀리즘 CSS 디자인 (타이틀 하이라이트 강화)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    .main .block-container {
        font-family: 'Inter', -apple-system, sans-serif !important;
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
    }
    
    /* 타이틀 강력 하이라이트 효과 (네온 민트 그라데이션) */
    .app-title-container {
        text-align: center;
        margin-bottom: 40px;
        padding: 20px 0;
    }
    .app-title {
        font-size: 42px !important;
        font-weight: 800 !important;
        color: #111111;
        letter-spacing: -1.5px;
        line-height: 1.2;
    }
    .app-title span {
        background: linear-gradient(120deg, #00FFCC 0%, #0066CC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .app-subtitle {
        font-size: 15px;
        color: #666666;
        margin-top: 12px;
    }
    
    /* 최신 트렌드 서머리 박스 (가장 상단 요약용) */
    .trend-summary-card {
        background: #F5F5F7;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 40px;
        border: none;
    }
    .trend-summary-title {
        font-size: 16px;
        font-weight: 700;
        color: #111111;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }
    .trend-summary-body {
        font-size: 14.5px;
        color: #333333;
        line-height: 1.6;
    }

    /* 하단 상세 뉴스 카드 디자인 */
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

# 3. 상단 하이라이트 타이틀 영역
st.markdown("""
    <div class='app-title-container'>
        <div class='app-title'>AI Agent <span>Intelligence</span></div>
        <div class='app-subtitle'>글로벌 에이전트 구축 기술동향 핵심 브리핑 시스템</div>
    </div>
""", unsafe_allow_html=True)

# 4. 사이드바 검색 및 카테고리 필터
st.sidebar.markdown("### 🔍 Filter")
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
        st.toast("최신 기술 동향을 업데이트했습니다.", icon="✅")

# 5. 카테고리별 동향 요약 데이터 정의 (대시보드 지표 대신 들어간 상단 텍스트 요약)
category_summaries = {
    "전체 보기": "현재 글로벌 AI 시장은 단순 챗봇 단계를 넘어 스스로 판단하고 행동하는 '자율형 에이전트(Agent)'로 패러다임이 완전히 전환되었습니다. 인프라 구축을 위한 오픈소스 프레임워크부터 PC를 제어하는 OS 브라우징까지 다각도로 고도화가 진행 중입니다.",
    "🛠️ 오픈소스 에이전트 프레임워크": "개발자들이 에이전트를 조립할 수 있는 아키텍처 경쟁이 치열합니다. 최근 트렌드는 단일 AI가 아닌, '기획-코딩-검증' 등 역할을 쪼갠 멀티 에이전트(Multi-Agent) 간의 기억(Memory) 공유 공유 메커니즘 고도화에 집중되어 있습니다.",
    "🏢 기업 업무 자동화 에이전트": "엔터프라이즈 부문에서는 고정된 규칙(Rule) 기반의 매크로 시스템을 대체하기 시작했습니다. 내부 데이터베이스(ERP/CRM)를 API로 연동하여 스스로 권한을 갖고 비즈니스 프로세스를 완결짓는 자율 업무 에이전트가 주류로 자리 잡고 있습니다.",
    "🖥️ 자율형 웹/OS 브라우징 에이전트": "가장 파괴적인 최신 분야입니다. AI가 화면 시각 정보를 인식하여 인간처럼 마우스를 클릭하고 키보드를 타이핑하는 기술이 상용화 단계에 진입했으며, 이는 UI 구조가 바뀌어도 유연하게 대응하는 차세대 자동화 인프라의 핵심입니다."
}

# 상단 카테고리별 요약 파트 띄우기
st.markdown(f"""
    <div class='trend-summary-card'>
        <div class='trend-summary-title'>🧬 {category} 부문 최신 기술 트렌드 요약</div>
        <div class='trend-summary-body'>{category_summaries[category]}</div>
    </div>
""", unsafe_allow_html=True)

# 6. 상세 뉴스 및 원문 연동 데이터 세트
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

# 7. 필터링 및 하단 상세 카드 출력 섹션
has_content = False

for news in ai_news_data:
    category_match = (category == "전체 보기" or news["category"] == category)
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
