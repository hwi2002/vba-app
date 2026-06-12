import streamlit as st
import time

# 1. 브라우저 및 레이아웃 설정
st.set_page_config(page_title="AI 에이전트 트렌드 리포트", page_icon="📝", layout="wide")

# 2. 시인성 강화를 위한 고대비/대형 폰트 CSS 디자인
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* 전체 글꼴 및 본문 너비 조절 - 눈이 편안한 크기 */
    .main .block-container {
        font-family: 'Noto Sans KR', sans-serif !important;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
        max-width: 900px;
        background-color: #ffffff;
    }
    
    /* 직관적이고 깔끔한 메인 제목 */
    .header-box {
        text-align: center;
        margin-bottom: 35px;
        padding: 10px 0;
    }
    .header-title {
        font-size: 36px !important;
        font-weight: 900 !important;
        color: #111111; /* 선명한 검은색 */
        letter-spacing: -1px;
    }
    .header-subtitle {
        font-size: 16px;
        color: #555555;
        font-weight: 500;
        margin-top: 8px;
    }
    
    /* [스타일 1] 상단 요약 섹션: 선명한 테두리와 체크마크로 가독성 극대화 */
    .summary-card {
        background: #F8F9FA; /* 연한 회색 배경 */
        border: 2px solid #E9ECEF;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 40px;
    }
    .summary-title {
        font-size: 18px;
        font-weight: 700;
        color: #0D6EFD; /* 신뢰감을 주는 파란색 */
        margin-bottom: 16px;
        border-bottom: 2px solid #0D6EFD;
        padding-bottom: 8px;
    }
    .summary-item {
        font-size: 16px;
        color: #212529; /* 고대비 진한 글자색 */
        line-height: 1.6;
        margin-bottom: 12px;
    }
    .summary-item strong {
        color: #000000;
        font-weight: 700;
    }

    /* [스타일 2] 하단 상세 카드 섹션: 확실히 구분되는 개별 상자 형태 */
    .detail-card {
        background: #FFFFFF;
        border: 1px solid #CED4DA;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .meta-row {
        margin-bottom: 12px;
    }
    .badge-category {
        font-size: 12px;
        font-weight: 700;
        color: #198754; /* 초록색 */
        background: #E8F5E9;
        padding: 4px 10px;
        border-radius: 6px;
        display: inline-block;
    }
    .badge-source {
        font-size: 13px;
        font-weight: 600;
        color: #495057;
        margin-left: 8px;
    }
    .badge-time {
        font-size: 13px;
        color: #6C757D;
        margin-left: 8px;
    }
    .detail-title {
        font-size: 22px;
        font-weight: 700;
        color: #111111;
        margin: 8px 0 12px 0;
        line-height: 1.4;
    }
    .detail-content {
        color: #333333;
        font-size: 15.5px;
        line-height: 1.65;
        margin-bottom: 16px;
    }
    
    /* 상세 카드 내부의 AI 인사이클 박스 (상단 요약과 다르게 노란색 포인트 강조) */
    .insight-box {
        background: #FFFDE7; /* 연한 노란색 포스트잇 느낌 */
        border-left: 4px solid #FBC02D;
        border-radius: 4px;
        padding: 14px 16px;
        font-size: 14.5px;
        color: #212529;
        margin-bottom: 14px;
    }
    
    /* 눈에 아주 잘 띄는 직관적인 파란색 단추형 링크 */
    .action-link {
        display: inline-block;
        font-size: 14px;
        font-weight: 700;
        color: #FFFFFF !important;
        background-color: #0D6EFD;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none !important;
    }
    .action-link:hover {
        background-color: #0B5ED7;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 메인 타이틀 영역
st.markdown("""
    <div class='header-box'>
        <div class='header-title'>AI 에이전트 기술 동향 리포트</div>
        <div class='header-subtitle'>실무자를 위한 카테고리별 인공지능 트렌드 핵심 요약</div>
    </div>
""", unsafe_allow_html=True)

# 4. 사이드바 필터 메뉴
st.sidebar.markdown("### 🔍 데이터 필터링")
search_query = st.sidebar.text_input("키워드로 찾기", "", placeholder="검색어를 입력하세요...")
category = st.sidebar.selectbox(
    "카테고리 변경",
    ["전체 보기", "🛠️ 오픈소스 에이전트 프레임워크", "🏢 기업 업무 자동화 에이전트", "🖥️ 자율형 웹/OS 브라우징 에이전트"]
)
st.sidebar.markdown("---")

with st.sidebar:
    if st.button("🔄 최신 데이터 불러오기", use_container_width=True):
        with st.spinner("정보 업데이트 중..."):
            time.sleep(1)
        st.toast("동향 리포트가 최신화되었습니다.", icon="📝")

# 5. [사용자 친화적 항목별 요약] 대폭 길어지고 명확해진 카테고리별 요약 문구
category_summaries = {
    "전체 보기": """
        <div class='summary-item'>✅ <strong>기술 패러다임의 대전환:</strong> 이제 인공지능은 단순히 질문에 대답하는 챗봇 단계를 지나, 스스로 판단하고 행동하여 업무를 완결하는 <strong>'자율형 에이전트'</strong> 체제로 완전히 진화했습니다.</div>
        <div class='summary-item'>✅ <strong>업무 자동화 시장의 지각변동:</strong> 사전에 지정된 규칙만 따르던 기존의 매크로(VBA)나 RPA 시스템이, 비정형 문서와 돌발 상황까지 처리할 수 있는 대규모 AI 에이전트 기반 인프라로 빠르게 대체되는 추세입니다.</div>
        <div class='summary-item'>✅ <strong>협업형 멀티 에이전트의 확산:</strong> 하나의 거대한 AI 모델에게 모든 일을 시키는 것보다 기획, 코딩, 검증 등 역할을 세분화한 여러 개의 작은 AI 에이전트들을 유기적으로 협업시키는 구조가 실무 표준으로 정착되었습니다.</div>
    """,
    "🛠️ 오픈소스 에이전트 프레임워크": """
        <div class='summary-item'>✅ <strong>에이전트 조립 도구의 경쟁 심화:</strong> 개발자가 비즈니스 흐름에 맞춰 AI의 행동 반경을 직접 제어하고 설계할 수 있는 모듈형 프레임워크 아키텍처 기술이 나날이 고도화되고 있습니다.</div>
        <div class='summary-item'>✅ <strong>대화 메모리(Memory) 레이어 강화:</strong> 여러 AI 에이전트가 소통할 때 정보가 유실되지 않도록, 별도의 데이터베이스와 연동하여 과거의 작업 히스토리를 기억하는 장기 기억 보존력이 대폭 개선되었습니다.</div>
        <div class='summary-item'>✅ <strong>실무 개발 공수 절감 효과:</strong> 에이전트 구축 프로세스가 표준화되면서 현업 엔지니어들이 업무 자동화 파이프라인을 빌드하는 데 걸리는 시간과 노력이 기존 대비 <strong>40% 이상 크게 단축</strong>되었습니다.</div>
    """,
    "🏢 기업 업무 자동화 에이전트": """
        <div class='summary-item'>✅ <strong>회사 핵심 인프라와의 연동:</strong> 사내 매뉴얼을 단순히 검색해서 띄워주는 수준을 넘어, 이제는 실제 전사적자원관리(ERP)나 고객관계관리(CRM) 시스템의 API를 AI가 직접 제어하여 자율적으로 데이터를 처리합니다.</div>
        <div class='summary-item'>✅ <strong>돌발 상황 자율 대처 능력:</strong> 에러가 나면 멈추던 기존 매크로와 달리, 사전에 정의되지 않은 예외적인 비즈니스 오류가 발생하더라도 AI가 스스로 대안을 탐색하여 중단 없이 업무를 완결짓습니다.</div>
        <div class='summary-item'>✅ <strong>전사적 도구의 통합 파이프라인:</strong> 엑셀 내부에 갇혀있던 업무 처리 한계를 깨고 이메일 수신 확인부 터 보고서 자동 작성, 결제 시스템 승인 요청까지 전사 도구들을 하나로 묶는 강력한 자동화가 실현되고 있습니다.</div>
    """,
    "🖥️ 자율형 웹/OS 브라우징 에이전트": """
        <div class='summary-item'>✅ <strong>인간과 동일한 화면 인식 기술:</strong> 개발자용 API나 소스 코드가 제공되지 않는 낙후된 구형 프로그램이더라도, AI가 모니터 화면을 눈으로 보듯 캡처하여 마우스 클릭과 키보드 입력을 정확하게 수행합니다.</div>
        <div class='summary-item'>✅ <strong>UI 디자인 변동에 대한 유연성:</strong> 웹페이지의 단추 위치나 메뉴 레이아웃이 조금만 바뀌어도 오작동하던 기존 크롤러나 매크로와 다르게, 시각 인식 모델을 기반으로 상황에 맞춰 막힘없이 유연하게 대처합니다.</div>
        <div class='summary-item'>✅ <strong>가상 업무 비서 시대의 도래:</strong> 앤트로픽의 'Computer Use' 같은 기술의 등장으로 사무직 직원들이 하루 종일 컴퓨터 앞에서 수행하는 단순 반복 동작들을 완벽하게 대행하는 서비스가 상용화 단계에 접수되었습니다.</div>
    """
}

# 상단 요약 섹션 출력
st.markdown(f"""
    <div class='summary-card'>
        <div class='summary-title'>📢 [핵심 요약] {category} 한눈에 보기</div>
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
        "summary": "에이전트 간 메모리 공유 및 역할 분담 체계 표준화로 전체 업무 파이프라인의 시스템 안정성 확보.",
        "url": "https://langchain.com"
    },
    {
        "title": "세일즈포스, 기업 전용 자율형 Agentforce 솔루션 전면 도입 성과 발표",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "TechCrunch",
        "time": "2시간 전",
        "content": "정해진 시나리오 답변에 의존하던 기존 챗봇의 한계를 극복하고, 사내 매뉴얼과 실시간 고객 데이터를 바탕으로 스스로 판단하여 환불 절차 및 기술 상담을 자율적으로 처리하는 기업 전용 솔루션이 도입 성과를 발표했습니다.",
        "summary": "단순 상담을 넘어 백오피스 시스템과 결합해 실질적인 결제 및 데이터 정산 업무까지 스스로 완결하는 구조.",
        "url": "https://techcrunch.com"
    },
    {
        "title": "앤트로픽(Anthropic), 사람처럼 PC를 자율 제어하는 'Computer Use' API 업그레이드",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Wired",
        "time": "5시간 전",
        "content": "AI 에이전트가 PC 모니터 화면을 실시간 스크린샷으로 캡처하여 마우스 커서의 좌표를 계산하고 클릭하며, 텍스트 상자에 타이핑하는 기술이 한 단계 진화했습니다. 파일 다운로드 및 크로스 브라우징 이메일 전송 등을 안정적으로 구현합니다.",
        "summary": "화면의 UI 구조나 버튼 위치가 변경되어도 시각 정보 바탕으로 유연한 대처 가능 (기존 매크로의 완전한 상위 호환 기술).",
        "url": "https://wired.com"
    }
]

# 7. 하단 상세 카드 출력 섹션
for news in ai_news_data:
    category_match = (category == "전체 보기" or news["category"] == category)
    search_match = (search_query.lower() in news["title"].lower() or 
                    search_query.lower() in news["content"].lower())
    
    if category_match and search_match:
        st.markdown(f"""
            <div class='detail-card'>
                <div class='meta-row'>
                    <span class='badge-category'>{news['category']}</span>
                    <span class='badge-source'>🌐 {news['source']}</span>
                    <span class='badge-time'>🕒 {news['time']}</span>
                </div>
                <div class='detail-title'>{news['title']}</div>
                <div class='detail-content'>{news['content']}</div>
                <div class='insight-box'>
                    <strong>💡 현업 적용 포인트:</strong> {news['summary']}
                </div>
                <div style='margin-top: 15px;'>
                    <a href='{news['url']}' target='_blank' class='action-link'>🔗 원문 기사 링크 이동</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
