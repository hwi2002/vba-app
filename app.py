import streamlit as st
import time

# 1. 브라우저 및 레이아웃 설정
st.set_page_config(page_title="AI Agent Weekly", page_icon="📝", layout="wide")

# 2. 고급 모던 UI 디자인 CSS 주입 (프로토타입 감성 완전 제거)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* 전체 레이아웃 정돈 */
    .main .block-container {
        font-family: 'Pretendard', -apple-system, sans-serif !important;
        padding-top: 4rem;
        padding-bottom: 4rem;
        max-width: 820px;
        background-color: #ffffff;
    }
    
    /* 깔끔하고 직관적인 메인 헤더 (거창한 그라데이션 배제) */
    .brand-header {
        text-align: center;
        margin-bottom: 45px;
    }
    .brand-title {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #1a1a1a;
        letter-spacing: -0.8px;
        margin-bottom: 6px;
    }
    .brand-subtitle {
        font-size: 14px;
        color: #737373;
        font-weight: 400;
    }
    
    /* [스타일 1] 상단 요약 섹션: 깊이감 있는 미니멀 카드 형태 */
    .summary-section {
        background: #fdfdfd;
        border: 1px solid #e5e5e5;
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 50px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
    }
    .summary-header {
        font-size: 15px;
        font-weight: 700;
        color: #171717;
        margin-bottom: 16px;
        letter-spacing: -0.3px;
    }
    .summary-list {
        margin: 0;
        padding-left: 20px;
        color: #404040;
        font-size: 14.5px;
        line-height: 1.7;
    }
    .summary-list li {
        margin-bottom: 10px;
    }
    .summary-list li strong {
        color: #171717;
    }

    /* [스타일 2] 하단 상세 카드 섹션: 전형적인 뉴스레터 아티클 스타일 */
    .article-card {
        padding: 32px 0;
        border-bottom: 1px solid #f0f0f0;
    }
    .article-meta {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 14px;
    }
    .tag-category {
        font-size: 11px;
        font-weight: 600;
        color: #2563eb;
        background: #eff6ff;
        padding: 4px 10px;
        border-radius: 4px;
    }
    .tag-source {
        font-size: 12px;
        font-weight: 500;
        color: #525252;
    }
    .tag-time {
        font-size: 12px;
        color: #a3a3a3;
    }
    .article-title {
        font-size: 21px;
        font-weight: 700;
        color: #111111;
        line-height: 1.4;
        margin: 0 0 12px 0;
        letter-spacing: -0.5px;
    }
    .article-content {
        color: #525252;
        font-size: 14.5px;
        line-height: 1.65;
        margin: 0 0 16px 0;
    }
    
    /* 상세 카드 내부의 AI 인사이클 박스 (상단 요약과 다르게 플랫하게 처리) */
    .article-insight {
        background: #f8fafc;
        border-radius: 8px;
        padding: 14px 18px;
        font-size: 13.5px;
        color: #334155;
        border-left: 3px solid #cbd5e1;
    }
    
    /* 세련된 우측 화살표 텍스트 링크 */
    .article-link {
        display: inline-block;
        font-size: 13.5px;
        font-weight: 600;
        color: #2563eb !important;
        text-decoration: none !important;
        margin-top: 14px;
    }
    .article-link:hover {
        text-decoration: underline !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 정돈된 브랜드 헤더 영역
st.markdown("""
    <div class='brand-header'>
        <div class='brand-title'>AI Agent Weekly</div>
        <div class='brand-subtitle'>실무 관점의 글로벌 인공지능 에이전트 동향 리포트</div>
    </div>
""", unsafe_allow_html=True)

# 4. 사이드바 검색 및 필터 구조
st.sidebar.markdown("### 🔍 Filter")
search_query = st.sidebar.text_input("키워드 검색", "", placeholder="검색어를 입력하세요...")
category = st.sidebar.selectbox(
    "카테고리 선택",
    ["전체 보기", "🛠️ 오픈소스 에이전트 프레임워크", "🏢 기업 업무 자동화 에이전트", "🖥️ 자율형 웹/OS 브라우징 에이전트"]
)
st.sidebar.markdown("---")

with st.sidebar:
    if st.button("🔄 최신 동향 새로고침", use_container_width=True):
        with st.spinner("업데이트 중..."):
            time.sleep(1)
        st.toast("최신 기술 동향이 동기화되었습니다.", icon="📝")

# 5. [스타일 1 적용] 카테고리별 항목별 상세 요약 데이터 브리핑
category_summaries = {
    "전체 보기": """
        <ul class='summary-list'>
            <li><strong>패러다임의 시프트:</strong> 전 세계 AI 시장의 초점이 단순 질의응답형 챗봇에서 사용자의 개입 없이 목표를 완결하는 <strong>'자율형 에이전트(Agent)'</strong>로 완전히 이동했습니다.</li>
            <li><strong>엔터프라이즈 중심의 확장:</strong> 고정된 프로그래밍 규칙을 따르던 기존 자동화(VBA, RPA) 시장이 대규모 비정형 데이터를 처리할 수 있는 AI 인프라와 결합하며 대대적인 교체 국면을 맞이했습니다.</li>
            <li><strong>멀티 에이전트의 주류화:</strong> 하나의 거대한 모델이 모든 문제를 해결하는 대신, 특정 도메인에 특화된 다수의 작은 에이전트가 협업하는 아키텍처가 실무 표준으로 정착 중입니다.</li>
        </ul>
    """,
    "🛠️ 오픈소스 에이전트 프레임워크": """
        <ul class='summary-list'>
            <li><strong>오케스트레이션 고도화:</strong> 개발자가 직접 에이전트의 행동 흐름을 제어하고 설계할 수 있는 모듈형 오픈소스 아키텍처 경쟁이 심화되고 있습니다.</li>
            <li><strong>컨텍스트 유지력 개선:</strong> 여러 에이전트가 대화를 주고받을 때 누수되던 메모리(Memory) 레이어를 독립형 DB와 연동하여 장기 기억 보존력을 대폭 끌어올렸습니다.</li>
            <li><strong>개발 생산성 제고:</strong> 프레임워크 자체 표준화가 이루어지며 현업 엔지니어들의 에이전트 파이프라인 빌드 공수가 기존 대비 약 40% 이상 절감되었습니다.</li>
        </ul>
    """,
    "🏢 기업 업무 자동화 에이전트": """
        <ul class='summary-list'>
            <li><strong>백오피스 완전 자동화:</strong> 사내 매뉴얼이나 문서를 RAG(검색 증강 생성) 형태로 읽는 단계를 넘어, 실제 사내 ERP, CRM 등 핵심 레거시 인프라의 권한을 제어하는 구조로 진화했습니다.</li>
            <li><strong>자율적 예외 처리:</strong> 사전에 정의되지 않은 돌발 비즈니스 상황이나 예외 오류가 발생했을 때, AI가 스스로 판단하고 대안을 수집하여 프로세스를 중단 없이 완결합니다.</li>
            <li><strong>VBA 생태계의 전환점:</strong> 엑셀 내부 매크로로 처리하던 한계를 넘어, 이메일 수신부터 결제 승인, 보고서 작성까지 전사적 도구를 유기적으로 잇는 파이프라인으로 빠르게 대체 중입니다.</li>
        </ul>
    """,
    "🖥️ 자율형 웹/OS 브라우징 에이전트": """
        <ul class='summary-list'>
            <li><strong>시각 정보 기반 인터페이스:</strong> 소스 코드나 API가 제공되지 않는 구형 웹사이트나 프로그램도 AI가 모니터 화면 캡처본을 보고 인간처럼 마우스 위치와 키보드 입력을 정확히 인지합니다.</li>
            <li><strong>UI 변동 대응력 확보:</strong> 웹페이지 디자인이나 단추 위치가 변경되면 오작동하던 기존 크롤러나 매크로와 달리, 시각 인식 모델을 바탕으로 상황에 맞춰 유연하게 경로를 재탐색합니다.</li>
            <li><strong>대규모 에이전트 경제 진입:</strong> 앤트로픽의 'Computer Use'를 필두로 PC 조작 기술이 확장됨에 따라 사무직 직원의 단순 반복 동작을 완벽히 대행하는 가상 비서 시대가 열렸습니다.</li>
        </ul>
    """
}

# 상단 요약 섹션 출력
st.markdown(f"""
    <div class='summary-section'>
        <div class='summary-header'>📋 {category} 부문 핵심 트렌드 브리핑</div>
        {category_summaries[category]}
    </div>
""", unsafe_allow_html=True)

# 6. 상세 뉴스 및 원문 연동 데이터 세트
ai_news_data = [
    {
        "title": "LangChain 기반 다중 에이전트(Multi-Agent) 협업 툴킷 업데이트",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "LangChain Blog",
        "time": "15분 전",
        "content": "개발자들이 복잡한 비즈니스 워크플로우를 유연하게 자동화할 수 있도록 여러 개의 AI 에이전트가 상호 작용하며 문제를 해결하는 멀티 에이전트 아키텍처가 업데이트되었습니다. 기획, 코딩, 테스트 에이전트가 각자 역할을 맡아 순차적으로 결과물을 도출합니다.",
        "summary": "에이전트 간 메모리 공유 및 역할 분담 체계 표준화로 시스템 안정성 확보.",
        "url": "https://langchain.com"
    },
    {
        "title": "세일즈포스, 기업 전용 자율형 Agentforce 솔루션 전면 도입 성과 발표",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "TechCrunch",
        "time": "2시간 전",
        "content": "정해진 시나리오 답변에 의존하던 기존 챗봇의 한계를 극복하고, 사내 매뉴얼과 실시간 고객 데이터를 바탕으로 스스로 판단하여 환불 절차 및 기술 상담을 자율적으로 처리하는 기업 전용 솔루션이 도입 성과를 발표했습니다.",
        "summary": "단순 응대를 넘어 백오피스 API와 결합해 실질적인 비즈니스 트랜잭션을 완결하는 구조 구축.",
        "url": "https://techcrunch.com"
    },
    {
        "title": "앤트로픽(Anthropic), 사람처럼 PC를 자율 제어하는 'Computer Use' API 업그레이드",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Wired",
        "time": "5시간 전",
        "content": "AI 에이전트가 PC 모니터 화면을 실시간 스크린샷으로 캡처하여 마우스 커서의 좌표를 계산하고 클릭하며, 텍스트 상자에 타이핑하는 기술이 한 단계 진화했습니다. 파일 다운로드 및 크로스 브라우징 이메일 전송 등을 안정적으로 구현합니다.",
        "summary": "화면의 UI 구조나 버튼 위치가 변경되어도 시각 정보 바탕으로 유연한 대처 가능 (기존 매크로의 완전한 상위 호환).",
        "url": "https://wired.com"
    }
]

# 7. [스타일 2 적용] 필터링 및 하단 상세 카드 출력 섹션
has_content = False

for news in ai_news_data:
    category_match = (category == "전체 보기" or news["category"] == category)
    search_match = (search_query.lower() in news["title"].lower() or 
                    search_query.lower() in news["content"].lower())
    
    if category_match and search_match:
        has_content = True
        st.markdown(f"""
            <div class='article-card'>
                <div class='article-meta'>
                    <span class='tag-category'>{news['category']}</span>
                    <span class='tag-source'>🌐 {news['source']}</span>
                    <span class='tag-time'>{news['time']}</span>
                </div>
                <div class='article-title'>{news['title']}</div>
                <div class='article-content'>{news['content']}</div>
                <div class='article-insight'>
                    <strong>💡 실무 인사이이트:</strong> {news['summary']}
                </div>
                <a href='{news['url']}' target='_blank' class='article-link'>원문 아티클 읽기 ↗</a>
            </div>
        """, unsafe_allow_html=True)

if not has_content:
    st.info("검색 조건에 맞는 에이전트 분석 리포트가 없습니다.")
