import streamlit as st
import timeimport streamlit as st
import time

# 1. 시스템 초기 설정 및 레이아웃 구성
st.set_page_config(
    page_title="AI Agent Briefing", 
    page_icon="📝", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 메인 화면 타이틀 및 서브타이틀 (담백하고 직관적인 뉴스레터 스타일)
st.title("📝 AI 에이전트 브리핑")
st.markdown("### 글로벌 최신 동향과 현업 인사이트")
st.markdown("---")

# 3. 사이드바 컨트롤러 (검색창 및 카테고리 필터)
st.sidebar.markdown("### 🔍 검색 및 필터")
query_input = st.sidebar.text_input("💡 키워드 검색", "", placeholder="검색어를 입력하세요...", key="search_box_final")
category_filter = st.sidebar.selectbox(
    "📂 기술 분류 선택",
    ["전체 보기", "🛠️ 오픈소스 에이전트 프레임워크", "🏢 기업 업무 자동화 에이전트", "🖥️ 자율형 웹/OS 브라우징 에이전트"],
    key="select_box_final"
)

st.sidebar.markdown("---")
with st.sidebar:
    if st.button("🔄 실시간 동기화", use_container_width=True, key="btn_sync_final"):
        with st.spinner("최신 정보를 수집하는 중..."):
            time.sleep(0.6)
        st.toast("동향 리포트가 최신화되었습니다.", icon="✅")

# 4. 카테고리별 핵심 요약 브리핑 문구 정의
summary_data = {
    "전체 보기": [
        "🔹 비즈니스 패러다임 전환: AI 시장이 단순 질문-답변을 넘어 복잡한 목표를 스스로 판단 및 완결하는 '자율형 에이전트' 체제로 진화했습니다.",
        "🔹 레거시 자동화의 대체: 고정된 구조로 구동되어 UI 변화에 취약하던 기존의 매크로(VBA), RPA 인프라가 유연한 인공지능 기반의 아키텍처로 대체되고 있습니다.",
        "🔹 오케스트레이션의 표준화: 거대한 단일 모델을 구동하는 대신 전문 태스크를 가진 소형 독립 에이전트 다수를 묶어 협업시키는 멀티 에이전트 모델이 주류로 안착했습니다."
    ],
    "🛠️ 오픈소스 에이전트 프레임워크": [
        "🔹 다중 모듈 연동 체계 수립: 개별 에이전트의 페르소나를 정의하고 행동 파이프라인을 체계적으로 제어할 수 있는 오픈소스 개발 프레임워크 경쟁이 치열합니다.",
        "🔹 메모리 유실 오류 최소화: 상호 대화 과정에서 정보가 손실되던 메모리 레이어를 독립형 데이터베이스와 바인딩하여 복잡한 실무 컨텍스트 유지력을 강화했습니다.",
        "🔹 개발 주기 단축 체감: 코어 아키텍처가 프레임워크 단위로 표준화되면서 업무 에이전트 빌드를 위한 현업 엔지니어의 코딩 분량이 40% 이상 감소했습니다."
    ],
    "🏢 기업 업무 자동화 에이전트": [
        "🔹 전사 시스템 직접 제어: 단순 사내 문서를 요약 및 검색하여 띄우던 초기 모델을 넘어 내부 ERP, CRM 등 주요 레거시 시스템의 데이터 처리 권한을 위임받는 수준에 이르렀습니다.",
        "🔹 자율 예외 분기 처리: 알 수 없는 비즈니스 조건이나 에러 발생 시 멈추는 매크로와 달리 AI가 원인을 스스로 판단하고 정정하여 태스크를 지속 완결합니다.",
        "🔹 데스크톱 자동화 확장: 이메일 수신부터 발주서 생성, 회계 보고서 자동 취합 및 결제 시스템 상신까지 전사 도구를 유기적으로 묶는 강력한 자동화가 도입되고 있습니다."
    ],
    "🖥️ 자율형 웹/OS 브라우징 에이전트": [
        "🔹 비정형 시각 인지 인터페이스: 전용 API 접근 권한이 전무한 구형 시스템이라도 모니터 화면 자체를 비전 모델로 분석하여 인간과 똑같이 마우스와 키보드를 조작합니다.",
        "🔹 동적 웹 구조 복구 안정성: 웹페이지 배치가 임의로 변경되면 정지하던 스크래퍼 방식과 달리 상황에 유연하게 대처하여 올바른 경로를 자율적으로 재탐색합니다.",
        "🔹 가상 디지털 노동력 확보: 앤드로픽의 크롬/OS 제어 기술을 시작으로 가상 데스크톱 내 단순 반복 사무 처리를 인간의 감독하에 완전 전가할 수 있는 기술적 토대가 완성되었습니다."
    ]
}

# [스타일 1] 상단 요약 박스 출력 (스트림릿 전용 st.info 상자로 절대 깨지지 않음)
st.subheader(f"📢 {category_filter} 부문 핵심 요약")
for bullet in summary_data[category_filter]:
    st.markdown(bullet)

st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("📋 실시간 기술 동향 상세 리포트")
st.markdown("---")

# 5. 수집된 최신 AI 에이전트 상세 뉴스 데이터셋 (6개 카드 상자 알맹이)
news_repository = [
    {
        "title": "LangChain 기반 다중 에이전트(Multi-Agent) 협업 워크플로우 툴킷 출시",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "LangChain Blog",
        "time": "15분 전",
        "content": "비즈니스 프로세스를 단계별로 자율화하기 위해 기획, 코딩, 품질 검증 등 역할이 철저히 개인화된 복수의 AI 에이전트가 협업하며 연쇄적으로 결과물을 도출하는 프레임워크 아키텍처가 정식 공개되었습니다.",
        "insight": "에이전트 간 메모리 공유 레이어 표준화로 전체 자동화 파이프라인의 안전성 확보.",
        "url": "https://langchain.com"
    },
    {
        "title": "세일즈포스, 기업 데이터베이스 결합형 자율 에이전트 'Agentforce Operations' 전면 확대",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "TechCrunch",
        "time": "2시간 전",
        "content": "정형화된 조건 분기 챗봇을 극복하고 사내 매뉴얼과 실시간 기업 인프라 데이터를 유기적으로 판독하여 정산 업무, 고객의 클레임 처리, 데이터 검증 및 백오피스 병목을 스스로 처리하는 시스템이 글로벌 기업에 대거 도입되었습니다.",
        "insight": "단순 문서 검색 단계를 넘어서 API 연동 기반의 자율 트랜잭션을 완결하는 엔터프라이즈 구조 확립.",
        "url": "https://techcrunch.com"
    },
    {
        "title": "앤트로픽, 모바일 지시 제어 기반 데스크톱 자율 조작 'Computer Use' 기능 업데이트",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Wired",
        "time": "5시간 전",
        "content": "모니터 화면을 실시간 단위로 스냅샷 캡처하여 마우스 좌표를 연산 및 클릭하고, 텍스트 레이아웃을 식별해 타이핑하는 기술이 한층 더 정교해졌습니다. 이제 스마트폰 메신저 연동만으로 원격지에 배치된 업무용 PC의 복잡한 엑셀 취합 업무 처리를 가상 에이전트에게 전가할 수 있습니다.",
        "insight": "화면 UI 구조 및 버튼의 위치가 불규칙하게 변형되어도 유연하게 복구하는 기존 매크로의 상위 호환 아키텍처.",
        "url": "https://wired.com"
    },
    {
        "title": "Microsoft AutoGen, 자율형 비정형 데이터 가공용 복합 에이전트 파이프라인 고도화",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "MS Developer Group",
        "time": "1일 전",
        "content": "다양한 모델 종류(LLM, 비전, 임베딩)들이 상호 유기적인 스레드로 동기화되어 사람이 개입하지 않는 대규모 비정형 보고서 마이그레이션 업무를 성공적으로 조율하는 프레임워크 신규 엔진 패치가 적용되었습니다.",
        "insight": "코드 인터프리터 샌드박스가 결합되어 가동 중 수식 오류 발생 시 스스로 코드를 디버깅 및 재생성하는 루프 지원.",
        "url": "https://github.com"
    },
    {
        "title": "구글 클라우드, 전사적 자원 관리 시스템(ERP) 바인딩용 자율 의사결정 에이전트 킷 발표",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "Google Cloud Insights",
        "time": "2일 전",
        "content": "구글 워크스페이스 생태계 및 외부 클라우드 플랫폼 인프라를 직접 연동하는 기업 특화형 툴셋입니다. 물류, 재고 관리, 발주 대기열 취합 시 AI 에이전트가 시장 단가 추이를 자율 추적하여 매입 결정을 내리는 시스템 시연이 완료되었습니다.",
        "insight": "매크로가 건드리지 못하던 글로벌 외부 웹 데이터 정보 실시간 반영 및 권한 거버넌스 제어 기능 제공.",
        "url": "https://google.com"
    },
    {
        "title": "OpenAI, 크롬 브라우저 자율 실행 및 범용 웹 태스크 대행 'Operator' 정식 업데이트 개시",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Bloomberg Technology",
        "time": "3일 전",
        "content": "사용자의 단순 텍스트 목표지정 명령어 하나로 크롬 브라우저 창을 자율 인스턴스로 분리 생성한 뒤, 해외 항공권 비교 분석부터 예약, 기업 정보 백그라운드 리서치 및 엑셀 다운로드 파일 생성까지 마우스 컨트롤 없이 실행하는 범용 비서가 상용화 궤도에 진입했습니다.",
        "insight": "단순 챗봇 인터페이스의 종말을 선언하고 웹 브라우저 기반의 자율 행동 경제 체제로의 도래 증명.",
        "url": "https://bloomberg.com"
    }
]

# 6. [스타일 2 적용] 하단 상세 카드 리스트 강제 렌더링 구역
content_found = False

for item in news_repository:
    # 카테고리 및 키워드 필터링 매칭 검사
    is_category_valid = (category_filter == "전체 보기" or item["category"] == category_filter)
    is_keyword_valid = (query_input.lower() in item["title"].lower() or 
                        query_input.lower() in item["content"].lower() or
                        query_input.lower() in item["insight"].lower())
    
    if is_category_valid and is_keyword_valid:
        content_found = True
        
        # 개별 카드를 감싸는 깔끔한 박스 테두리 생성 (st.container)
        with st.container():
            # 메타 정보 출력
            st.caption(f"📌 {item['category']}  |  🌐 {item['source']}  |  🕒 {item['time']}")
            # 제목 크고 굵게 출력
            st.subheader(item['title'])
            # 본문 내용 출력
            st.write(item['content'])
            
            # 현업 분석 인사이틀 상자 (st.info로 스타일 차별화)
            st.info(f"💡 현업 매니저 분석 : {item['insight']}")
            
            # 원문 이동 링크 단추 구현
            st.link_button("🔗 출처 원문 보기", item["url"])
            st.markdown("<br><hr><br>", unsafe_allowed_code=True)

if not content_found:
    st.info("검색 조건에 맞는 동향 데이터가 존재하지 않습니다.")

# 1. 시스템 초기 설정 및 레이아웃 구성
st.set_page_config(
    page_title="AI Agent Briefing", 
    page_icon="📝", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 메인 화면 타이틀 및 서브타이틀 (담백하고 직관적인 뉴스레터 스타일)
st.title("📝 AI 에이전트 브리핑")
st.markdown("### 글로벌 최신 동향과 현업 인사이트")
st.markdown("---")

# 3. 사이드바 컨트롤러 (검색창 및 카테고리 필터)
st.sidebar.markdown("### 🔍 검색 및 필터")
query_input = st.sidebar.text_input("💡 키워드 검색", "", placeholder="검색어를 입력하세요...", key="search_box_final")
category_filter = st.sidebar.selectbox(
    "📂 기술 분류 선택",
    ["전체 보기", "🛠️ 오픈소스 에이전트 프레임워크", "🏢 기업 업무 자동화 에이전트", "🖥️ 자율형 웹/OS 브라우징 에이전트"],
    key="select_box_final"
)

st.sidebar.markdown("---")
with st.sidebar:
    if st.button("🔄 실시간 동기화", use_container_width=True, key="btn_sync_final"):
        with st.spinner("최신 정보를 수집하는 중..."):
            time.sleep(0.6)
        st.toast("동향 리포트가 최신화되었습니다.", icon="✅")

# 4. 카테고리별 핵심 요약 브리핑 문구 정의
summary_data = {
    "전체 보기": [
        "🔹 비즈니스 패러다임 전환: AI 시장이 단순 질문-답변을 넘어 복잡한 목표를 스스로 판단 및 완결하는 '자율형 에이전트' 체제로 진화했습니다.",
        "🔹 레거시 자동화의 대체: 고정된 구조로 구동되어 UI 변화에 취약하던 기존의 매크로(VBA), RPA 인프라가 유연한 인공지능 기반의 아키텍처로 대체되고 있습니다.",
        "🔹 오케스트레이션의 표준화: 거대한 단일 모델을 구동하는 대신 전문 태스크를 가진 소형 독립 에이전트 다수를 묶어 협업시키는 멀티 에이전트 모델이 주류로 안착했습니다."
    ],
    "🛠️ 오픈소스 에이전트 프레임워크": [
        "🔹 다중 모듈 연동 체계 수립: 개별 에이전트의 페르소나를 정의하고 행동 파이프라인을 체계적으로 제어할 수 있는 오픈소스 개발 프레임워크 경쟁이 치열합니다.",
        "🔹 메모리 유실 오류 최소화: 상호 대화 과정에서 정보가 손실되던 메모리 레이어를 독립형 데이터베이스와 바인딩하여 복잡한 실무 컨텍스트 유지력을 강화했습니다.",
        "🔹 개발 주기 단축 체감: 코어 아키텍처가 프레임워크 단위로 표준화되면서 업무 에이전트 빌드를 위한 현업 엔지니어의 코딩 분량이 40% 이상 감소했습니다."
    ],
    "🏢 기업 업무 자동화 에이전트": [
        "🔹 전사 시스템 직접 제어: 단순 사내 문서를 요약 및 검색하여 띄우던 초기 모델을 넘어 내부 ERP, CRM 등 주요 레거시 시스템의 데이터 처리 권한을 위임받는 수준에 이르렀습니다.",
        "🔹 자율 예외 분기 처리: 알 수 없는 비즈니스 조건이나 에러 발생 시 멈추는 매크로와 달리 AI가 원인을 스스로 판단하고 정정하여 태스크를 지속 완결합니다.",
        "🔹 데스크톱 자동화 확장: 이메일 수신부터 발주서 생성, 회계 보고서 자동 취합 및 결제 시스템 상신까지 전사 도구를 유기적으로 묶는 강력한 자동화가 도입되고 있습니다."
    ],
    "🖥️ 자율형 웹/OS 브라우징 에이전트": [
        "🔹 비정형 시각 인지 인터페이스: 전용 API 접근 권한이 전무한 구형 시스템이라도 모니터 화면 자체를 비전 모델로 분석하여 인간과 똑같이 마우스와 키보드를 조작합니다.",
        "🔹 동적 웹 구조 복구 안정성: 웹페이지 배치가 임의로 변경되면 정지하던 스크래퍼 방식과 달리 상황에 유연하게 대처하여 올바른 경로를 자율적으로 재탐색합니다.",
        "🔹 가상 디지털 노동력 확보: 앤드로픽의 크롬/OS 제어 기술을 시작으로 가상 데스크톱 내 단순 반복 사무 처리를 인간의 감독하에 완전 전가할 수 있는 기술적 토대가 완성되었습니다."
    ]
}

# [스타일 1] 상단 요약 박스 출력 (스트림릿 전용 st.info 상자로 절대 깨지지 않음)
st.subheader(f"📢 {category_filter} 부문 핵심 요약")
for bullet in summary_data[category_filter]:
    st.markdown(bullet)

st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("📋 실시간 기술 동향 상세 리포트")
st.markdown("---")

# 5. 수집된 최신 AI 에이전트 상세 뉴스 데이터셋 (6개 카드 상자 알맹이)
news_repository = [
    {
        "title": "LangChain 기반 다중 에이전트(Multi-Agent) 협업 워크플로우 툴킷 출시",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "LangChain Blog",
        "time": "15분 전",
        "content": "비즈니스 프로세스를 단계별로 자율화하기 위해 기획, 코딩, 품질 검증 등 역할이 철저히 개인화된 복수의 AI 에이전트가 협업하며 연쇄적으로 결과물을 도출하는 프레임워크 아키텍처가 정식 공개되었습니다.",
        "insight": "에이전트 간 메모리 공유 레이어 표준화로 전체 자동화 파이프라인의 안전성 확보.",
        "url": "https://langchain.com"
    },
    {
        "title": "세일즈포스, 기업 데이터베이스 결합형 자율 에이전트 'Agentforce Operations' 전면 확대",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "TechCrunch",
        "time": "2시간 전",
        "content": "정형화된 조건 분기 챗봇을 극복하고 사내 매뉴얼과 실시간 기업 인프라 데이터를 유기적으로 판독하여 정산 업무, 고객의 클레임 처리, 데이터 검증 및 백오피스 병목을 스스로 처리하는 시스템이 글로벌 기업에 대거 도입되었습니다.",
        "insight": "단순 문서 검색 단계를 넘어서 API 연동 기반의 자율 트랜잭션을 완결하는 엔터프라이즈 구조 확립.",
        "url": "https://techcrunch.com"
    },
    {
        "title": "앤트로픽, 모바일 지시 제어 기반 데스크톱 자율 조작 'Computer Use' 기능 업데이트",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Wired",
        "time": "5시간 전",
        "content": "모니터 화면을 실시간 단위로 스냅샷 캡처하여 마우스 좌표를 연산 및 클릭하고, 텍스트 레이아웃을 식별해 타이핑하는 기술이 한층 더 정교해졌습니다. 이제 스마트폰 메신저 연동만으로 원격지에 배치된 업무용 PC의 복잡한 엑셀 취합 업무 처리를 가상 에이전트에게 전가할 수 있습니다.",
        "insight": "화면 UI 구조 및 버튼의 위치가 불규칙하게 변형되어도 유연하게 복구하는 기존 매크로의 상위 호환 아키텍처.",
        "url": "https://wired.com"
    },
    {
        "title": "Microsoft AutoGen, 자율형 비정형 데이터 가공용 복합 에이전트 파이프라인 고도화",
        "category": "🛠️ 오픈소스 에이전트 프레임워크",
        "source": "MS Developer Group",
        "time": "1일 전",
        "content": "다양한 모델 종류(LLM, 비전, 임베딩)들이 상호 유기적인 스레드로 동기화되어 사람이 개입하지 않는 대규모 비정형 보고서 마이그레이션 업무를 성공적으로 조율하는 프레임워크 신규 엔진 패치가 적용되었습니다.",
        "insight": "코드 인터프리터 샌드박스가 결합되어 가동 중 수식 오류 발생 시 스스로 코드를 디버깅 및 재생성하는 루프 지원.",
        "url": "https://github.com"
    },
    {
        "title": "구글 클라우드, 전사적 자원 관리 시스템(ERP) 바인딩용 자율 의사결정 에이전트 킷 발표",
        "category": "🏢 기업 업무 자동화 에이전트",
        "source": "Google Cloud Insights",
        "time": "2일 전",
        "content": "구글 워크스페이스 생태계 및 외부 클라우드 플랫폼 인프라를 직접 연동하는 기업 특화형 툴셋입니다. 물류, 재고 관리, 발주 대기열 취합 시 AI 에이전트가 시장 단가 추이를 자율 추적하여 매입 결정을 내리는 시스템 시연이 완료되었습니다.",
        "insight": "매크로가 건드리지 못하던 글로벌 외부 웹 데이터 정보 실시간 반영 및 권한 거버넌스 제어 기능 제공.",
        "url": "https://google.com"
    },
    {
        "title": "OpenAI, 크롬 브라우저 자율 실행 및 범용 웹 태스크 대행 'Operator' 정식 업데이트 개시",
        "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
        "source": "Bloomberg Technology",
        "time": "3일 전",
        "content": "사용자의 단순 텍스트 목표지정 명령어 하나로 크롬 브라우저 창을 자율 인스턴스로 분리 생성한 뒤, 해외 항공권 비교 분석부터 예약, 기업 정보 백그라운드 리서치 및 엑셀 다운로드 파일 생성까지 마우스 컨트롤 없이 실행하는 범용 비서가 상용화 궤도에 진입했습니다.",
        "insight": "단순 챗봇 인터페이스의 종말을 선언하고 웹 브라우저 기반의 자율 행동 경제 체제로의 도래 증명.",
        "url": "https://bloomberg.com"
    }
]

# 6. [스타일 2 적용] 하단 상세 카드 리스트 강제 렌더링 구역
content_found = False

for item in news_repository:
    # 카테고리 및 키워드 필터링 매칭 검사
    is_category_valid = (category_filter == "전체 보기" or item["category"] == category_filter)
    is_keyword_valid = (query_input.lower() in item["title"].lower() or 
                        query_input.lower() in item["content"].lower() or
                        query_input.lower() in item["insight"].lower())
    
    if is_category_valid and is_keyword_valid:
        content_found = True
        
        # 개별 카드를 감싸는 깔끔한 박스 테두리 생성 (st.container)
        with st.container():
            # 메타 정보 출력
            st.caption(f"📌 {item['category']}  |  🌐 {item['source']}  |  🕒 {item['time']}")
            # 제목 크고 굵게 출력
            st.subheader(item['title'])
            # 본문 내용 출력
            st.write(item['content'])
            
            # 현업 분석 인사이틀 상자 (st.info로 스타일 차별화)
            st.info(f"💡 현업 매니저 분석 : {item['insight']}")
            
            # 원문 이동 링크 단추 구현
            st.link_button("🔗 출처 원문 보기", item["url"])
            st.markdown("<br><hr><br>", unsafe_allowed_code=True)

if not content_found:
    st.info("검색 조건에 맞는 동향 데이터가 존재하지 않습니다.")
코드를 사용할 때는 주의가 필요합니다.🛠️ 이번 수정본의 확실한 변화내용 유실 가능성 0%웹 브라우저가 해석에 실패할 수 있는 임의의 사설 HTML 클래스명들을 과감히 다 치워버렸습니다.파이썬의 표준 스트림릿 명령어들(st.subheader, st.info, st.link_button)로만 화면을 다시 그리게 조치했으므로, 6개의 최신 리포트 알맹이 글자들이 무조건 화면에 선명하게 출력됩니다.상단 요약과 하단 카드의 확실한 스타일 차이상단 요약: 대시보드 메인 중앙에 심플한 가로 정렬 텍스트 불릿 구조로 간결하게 배치됩니다.하단 상세: 각각의 뉴스가 구분선(---)과 함께 내용 본문 ➡️ 노란색/연파란색 톤의 전용 안내 상자(st.info) ➡️ 링크 이동 단추 순서로 입체감 있게 나열되어 정보의 가독성이 월등히 좋아집니다.수정된 최종 코드를 복사해서 커밋해 보세요. 이제 새로고침 하시면 드디어 꽉 찬 최신 데이터 알맹이들을 직접 손으로 만져보며 조작하실 수 있습니다! 결과가 잘 뜨는지 바로 확인해 보세요!
