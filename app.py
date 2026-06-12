import streamlit as st
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))


st.set_page_config(
    page_title="AI Agent 기술 트렌드",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d")


@st.cache_data(ttl=86400)
def load_trends():
    return [
        {
            "category": "Agent Orchestration",
            "summary": "AI Agent는 단일 챗봇 구조에서 벗어나 여러 역할을 가진 에이전트가 협업하는 구조로 이동하고 있습니다.",
            "changes": [
                "상태 그래프 기반 워크플로우 설계가 확산되고 있습니다.",
                "Planner, Executor, Evaluator처럼 역할을 나누는 구조가 증가하고 있습니다.",
                "단순 프롬프트 체이닝보다 업무 단계별 제어 구조가 중요해지고 있습니다."
            ],
            "meaning": "기술적으로는 Agent가 단순히 답변을 생성하는 수준을 넘어, 업무 단계를 이해하고 다음 행동을 선택하는 실행 구조로 발전하고 있다는 의미입니다.",
            "enterprise": "기업 업무에서는 보고서 작성, 심사 보조, 고객 응대, 장애 처리처럼 여러 단계가 있는 업무에 적용 가능성이 큽니다. 다만 각 단계의 책임과 승인 기준을 명확히 해야 합니다.",
            "risk": "상태 전이 조건이 불명확하면 Agent가 같은 작업을 반복하거나 잘못된 판단을 이어갈 수 있습니다.",
            "action": "초기 PoC에서는 업무를 5~7개 단계로 나누고, 각 단계별 입력값, 출력값, 검증 기준, 실패 처리 방식을 먼저 정의하는 것이 좋습니다."
        },
        {
            "category": "MCP & Tool Calling",
            "summary": "AI Agent의 실무 가치는 외부 시스템과 도구를 얼마나 안전하게 연결하느냐에 따라 결정되고 있습니다.",
            "changes": [
                "MCP와 Tool Calling 구조가 Agent 연동 방식의 핵심으로 부상하고 있습니다.",
                "도구의 이름, 입력값, 반환값, 권한 범위를 명확히 정의하는 방식이 중요해지고 있습니다.",
                "Agent가 API, 데이터베이스, 업무 시스템을 직접 호출하는 사례가 늘고 있습니다."
            ],
            "meaning": "기술적으로는 Agent가 단순 대화 인터페이스가 아니라 외부 시스템을 호출하는 실행 주체로 바뀌고 있다는 뜻입니다.",
            "enterprise": "기업에서는 조회형 도구와 변경형 도구를 반드시 구분해야 합니다. 고객 정보 조회와 데이터 수정, 승인, 외부 발송은 위험 수준이 다르기 때문입니다.",
            "risk": "도구 호출 권한을 넓게 열어두면 모델의 오판이 실제 데이터 변경이나 외부 발송으로 이어질 수 있습니다.",
            "action": "Tool 목록을 조회형, 생성형, 변경형, 외부발송형으로 나누고 변경형 이상에는 사람 승인 단계를 두는 것이 적합합니다."
        },
        {
            "category": "Memory & State Management",
            "summary": "AI Agent의 메모리는 단순 대화 기억이 아니라 업무 상태를 유지하는 구조로 확장되고 있습니다.",
            "changes": [
                "단기 대화 메모리보다 업무 진행 상태를 저장하는 Task State가 중요해지고 있습니다.",
                "Vector DB, RDB, Graph DB를 목적별로 조합하는 구조가 늘고 있습니다.",
                "장기 업무 처리형 Agent에서는 실행 이력과 참조 근거를 함께 남기는 방식이 중요합니다."
            ],
            "meaning": "기술적으로는 Agent가 매번 처음부터 답변하는 구조가 아니라, 이전 단계의 판단과 실행 상태를 이어받아 업무를 지속하는 구조로 발전하고 있습니다.",
            "enterprise": "제안서 작성, 심사 보조, 고객 상담, 장애 처리처럼 여러 번의 대화와 문서 검토가 이어지는 업무에서는 메모리 구조가 품질을 좌우합니다.",
            "risk": "잘못된 메모리가 누적되면 오래된 정보나 잘못된 사용자 의도를 기준으로 판단할 수 있습니다.",
            "action": "Conversation Memory, Business State, Reference Knowledge, Execution Log를 분리해서 설계하는 것이 좋습니다."
        },
        {
            "category": "Agent Evaluation & AgentOps",
            "summary": "AI Agent 평가는 정답률보다 실행 과정의 품질과 실패 통제가 더 중요해지고 있습니다.",
            "changes": [
                "Golden Dataset 기반 평가가 중요해지고 있습니다.",
                "Agent 실행 과정을 추적하는 Trace Log의 필요성이 커지고 있습니다.",
                "정답 여부뿐 아니라 도구 호출, 단계 누락, 재시도, 실패 처리까지 평가하는 흐름입니다."
            ],
            "meaning": "기술적으로는 Agent가 결과만 내는 시스템이 아니라 여러 단계를 수행하는 시스템이기 때문에, 평가도 과정 중심으로 바뀌어야 한다는 의미입니다.",
            "enterprise": "기업 운영에서는 사용자가 틀렸다고 느끼는 결과보다, 왜 틀렸는지 추적할 수 없는 구조가 더 큰 문제입니다. 실행 로그와 평가 체계가 없으면 개선이 어렵습니다.",
            "risk": "평가 체계 없이 운영하면 모델 문제인지, 데이터 문제인지, 도구 호출 문제인지, 업무 프로세스 문제인지 구분할 수 없습니다.",
            "action": "초기부터 업무별 골든셋과 루브릭을 만들고, 실행 성공률, 단계 누락률, 도구 호출 오류율, 사용자 개입률을 함께 관리하는 것이 좋습니다."
        },
        {
            "category": "Enterprise Agent Architecture",
            "summary": "기업형 AI Agent는 자동화 도구라기보다 통제 가능한 업무 위임 구조로 설계해야 합니다.",
            "changes": [
                "문서 검색 중심에서 ERP, CRM, 그룹웨어 연동 구조로 확장되고 있습니다.",
                "조회, 추천, 생성, 실행을 구분하는 업무 설계가 중요해지고 있습니다.",
                "권한, 승인, 감사 로그가 Agent 아키텍처의 핵심 요소가 되고 있습니다."
            ],
            "meaning": "기술적으로는 Agent가 단순 정보 제공자가 아니라 실제 업무 시스템과 연결되는 업무 실행 계층으로 이동하고 있다는 뜻입니다.",
            "enterprise": "기업에서는 모든 업무를 완전 자동화하기보다, 사람이 검토해야 할 부분과 Agent에게 위임할 수 있는 부분을 나누는 방식이 현실적입니다.",
            "risk": "업무 책임이 불명확한 상태에서 Agent를 도입하면 현업은 결과를 신뢰하지 못하고 IT는 장애 원인을 추적하기 어렵습니다.",
            "action": "조회 업무부터 시작해 추천, 초안 생성, 승인 기반 실행 순서로 점진적으로 확장하는 방식이 적합합니다."
        },
        {
            "category": "Computer Use & Browser Agent",
            "summary": "웹·OS 실행 Agent는 API가 없는 업무까지 자동화할 수 있지만, 보안과 통제 설계가 매우 중요합니다.",
            "changes": [
                "화면을 인식하고 클릭, 입력, 탐색을 수행하는 Agent 기술이 발전하고 있습니다.",
                "기존 RPA보다 UI 변화에 유연하게 대응할 가능성이 있습니다.",
                "브라우저 기반 업무 자동화와 레거시 시스템 자동화에 대한 관심이 높아지고 있습니다."
            ],
            "meaning": "기술적으로는 Agent가 API 호출뿐 아니라 사람이 보는 화면을 직접 조작하는 방향으로 확장되고 있다는 의미입니다.",
            "enterprise": "API가 없는 구형 웹 시스템, 반복 입력 업무, 관리자 페이지 조회, 외부 사이트 정보 수집에는 활용 가능성이 있습니다.",
            "risk": "화면 기반 Agent는 사용자의 계정 권한으로 움직일 수 있기 때문에 잘못된 클릭, 민감 정보 노출, 외부 전송 위험이 있습니다.",
            "action": "초기에는 읽기 전용 업무나 테스트 환경에서 시작하고, 허용 URL, 전용 계정, 실행 로그, 사람 확인 단계를 반드시 두는 것이 안전합니다."
        }
    ]


def contains_keyword(item, keyword):
    if not keyword:
        return True

    text = " ".join([
        item["category"],
        item["summary"],
        item["meaning"],
        item["enterprise"],
        item["risk"],
        item["action"],
        " ".join(item["changes"])
    ]).lower()

    return keyword.lower() in text


def render_summary(trends):
    st.markdown("#### Executive Summary")

    st.write(
        "AI Agent 기술은 단순 챗봇이나 뉴스성 AI 기능을 넘어, 업무 목표를 이해하고 도구를 호출하며 실행 결과를 검증하는 구조로 이동하고 있습니다. "
        "핵심 변화는 Agent Orchestration, MCP & Tool Calling, Memory & State Management, Agent Evaluation, Enterprise Architecture, Computer Use 영역에서 동시에 나타나고 있습니다."
    )

    st.write(
        "기업 적용 관점에서는 모델 성능보다 통제 가능한 실행 구조가 중요합니다. "
        "즉, 어떤 도구를 호출할 수 있는지, 어떤 데이터에 접근할 수 있는지, 어느 단계에서 사람 승인이 필요한지, 실패했을 때 어떻게 중단하거나 복구할지를 먼저 정의해야 합니다."
    )

    st.markdown("#### 기술 테마별 요약")

    for item in trends:
        with st.container(border=True):
            st.markdown(f"##### {item['category']}")
            st.write(item["summary"])


def render_trend_card(item):
    with st.container(border=True):
        st.markdown(f"### {item['category']}")

        st.write(item["summary"])

        with st.expander("상세 내용 보기", expanded=True):
            st.markdown("##### 주요 변화")
            for change in item["changes"]:
                st.write(f"• {change}")

            st.markdown("##### 기술적 의미")
            st.write(item["meaning"])

            st.markdown("##### 기업 적용 시사점")
            st.write(item["enterprise"])

            st.markdown("##### 리스크 및 확인사항")
            st.write(item["risk"])

            st.markdown("##### 권장 액션")
            st.info(item["action"])


trends = load_trends()


with st.sidebar:
    st.markdown("### 검색 및 필터")

    query = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, 평가, 메모리, ERP, Browser"
    )

    categories = [item["category"] for item in trends]

    selected_categories = st.multiselect(
        "기술 분류",
        options=categories,
        default=categories
    )

    st.divider()

    st.caption("갱신 주기: 24시간 캐시")

    if st.button("화면 새로고침", use_container_width=True):
        st.cache_data.clear()
        st.rerun()


filtered_trends = []

for item in trends:
    category_ok = item["category"] in selected_categories
    keyword_ok = contains_keyword(item, query)

    if category_ok and keyword_ok:
        filtered_trends.append(item)


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 갱신: {now_kst_text()} | 갱신 주기: 24시간")
st.write(
    "AI Agent 관련 기술 흐름을 뉴스 목록이 아니라 아키텍처, 기업 적용, 운영 통제 관점으로 재구성한 브리핑입니다."
)

st.divider()


summary_tab, report_tab = st.tabs(["핵심요약", "상세리포트"])


with summary_tab:
    render_summary(filtered_trends)


with report_tab:
    st.markdown("#### 상세리포트")

    if not filtered_trends:
        st.info("현재 검색 조건에 맞는 기술 트렌드가 없습니다.")
    else:
        for item in filtered_trends:
            render_trend_card(item)
