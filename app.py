import streamlit as st
import time
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))


st.set_page_config(
    page_title="AI Agent 기술 트렌드",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


CATEGORY_ALL = "전체 보기"

CATEGORIES = [
    "에이전트 오케스트레이션",
    "도구 호출·프로토콜",
    "메모리·상태관리",
    "평가·운영관리",
    "기업 업무 자동화",
    "웹·OS 실행 에이전트",
]


REPORT_SUMMARY = {
    CATEGORY_ALL: [
        {
            "title": "종합 판단",
            "body": "AI Agent 기술의 중심은 더 이상 단순 챗봇, 문서 요약, 검색 증강 생성에 머물러 있지 않습니다. 최근 흐름은 사용자의 목표를 업무 단위로 분해하고, 필요한 도구를 호출하며, 중간 결과를 검증한 뒤 다음 행동으로 이어가는 실행형 아키텍처로 이동하고 있습니다. 즉, AI Agent의 경쟁력은 모델 성능 하나가 아니라 오케스트레이션, 상태 관리, 도구 연동, 평가 체계, 운영 통제의 결합 수준에서 결정됩니다.",
        },
        {
            "title": "기술 구조 변화",
            "body": "초기 AI Agent는 하나의 LLM이 여러 프롬프트를 순차적으로 처리하는 구조에 가까웠지만, 현재는 역할이 분리된 에이전트, 명시적인 상태 그래프, 외부 도구 호출, 장기 실행 워크플로우, 결과 검증 루프를 갖춘 구조로 발전하고 있습니다. 특히 LangGraph, AutoGen, CrewAI, MCP 계열의 흐름은 에이전트를 단순 대화 인터페이스가 아니라 업무 실행 런타임으로 다루려는 변화로 볼 수 있습니다.",
        },
        {
            "title": "기업 적용 시사점",
            "body": "기업 환경에서 AI Agent를 적용하려면 RAG만으로는 부족합니다. 실제 업무에서는 권한이 있는 시스템에 접근하고, 데이터를 조회·변경하며, 예외 상황을 처리하고, 처리 결과를 남겨야 합니다. 따라서 ERP, CRM, 그룹웨어, 데이터베이스, 승인 시스템과 연결되는 순간부터는 보안, 감사 로그, 사용자 승인, 롤백 절차가 핵심 설계 요소가 됩니다.",
        },
        {
            "title": "리스크 및 확인사항",
            "body": "AI Agent는 자동화 범위를 크게 넓힐 수 있지만, 동시에 오작동의 영향도 커집니다. 특히 웹·OS 조작형 에이전트는 사람이 보는 화면을 그대로 조작할 수 있기 때문에 계정 권한, 허용 도메인, 민감 정보 노출, 실행 로그, 사람 승인 단계를 명확히 설계해야 합니다. 초기 도입은 완전 자율형보다 사람 검토가 포함된 반자동 구조가 현실적입니다.",
        },
    ]
}


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def normalize_text(value):
    return str(value or "").casefold().strip()


def contains_keyword(item, keyword):
    keyword = normalize_text(keyword)

    if not keyword:
        return True

    searchable_text = " ".join(
        [
            item.get("title", ""),
            item.get("category", ""),
            item.get("core_message", ""),
            item.get("technology_context", ""),
            item.get("architecture_point", ""),
            item.get("enterprise_impact", ""),
            item.get("risk_point", ""),
            item.get("manager_message", ""),
            item.get("recommended_action", ""),
            " ".join(item.get("tags", [])),
        ]
    )

    return keyword in normalize_text(searchable_text)


@st.cache_data(ttl=600, show_spinner=False)
def load_trend_items():
    collected_at = now_kst_text()

    return [
        {
            "title": "상태 그래프 기반 Agentic Workflow가 에이전트 구조의 중심으로 이동",
            "category": "에이전트 오케스트레이션",
            "technology_layer": "Workflow Orchestration",
            "maturity": "실무 적용 확대",
            "collected_at": collected_at,
            "core_message": "AI Agent의 핵심은 더 이상 프롬프트를 길게 쓰는 방식이 아니라, 업무 흐름을 상태 단위로 쪼개고 각 단계의 책임과 전이 조건을 명확히 설계하는 방향으로 이동하고 있습니다.",
            "technology_context": "기존 체인 방식은 한 번의 실행 흐름이 실패하면 어느 지점에서 문제가 발생했는지 파악하기 어렵습니다. 반면 상태 그래프 기반 구조는 계획, 실행, 검증, 재시도, 종료 조건을 노드와 엣지로 분리해 관리할 수 있습니다. 이 구조에서는 에이전트가 단순히 답변을 생성하는 것이 아니라, 현재 상태를 기준으로 다음 행동을 선택하고 필요한 도구를 호출합니다.",
            "architecture_point": "설계 관점에서는 Planner, Executor, Evaluator, Tool Router를 분리하고, 각 단계의 입력과 출력을 명시적으로 남기는 것이 중요합니다. 특히 장기 실행 업무에서는 중간 상태 저장, 실패 시 재개, 사람 승인 후 다음 단계 진행 같은 제어 흐름이 필요합니다.",
            "enterprise_impact": "기업 업무에서는 견적 검토, 보고서 작성, 고객 응대, 심사 보조처럼 여러 단계를 거치는 업무에 적합합니다. 업무 단계가 명확할수록 에이전트의 자율성을 높일 수 있고, 반대로 예외가 많거나 책임 소재가 큰 업무는 승인 단계를 넣어야 합니다.",
            "risk_point": "상태 전이가 명확하지 않으면 에이전트가 같은 작업을 반복하거나, 잘못된 중간 결과를 기준으로 다음 업무를 진행할 수 있습니다. 따라서 종료 조건, 재시도 횟수, 실패 시 사람에게 넘기는 기준이 반드시 필요합니다.",
            "manager_message": "현업 관점에서는 ‘AI가 알아서 한다’가 아니라 ‘어떤 상태에서 어떤 판단을 하고 어디까지 자동으로 진행할지’를 정의하는 것이 핵심입니다.",
            "recommended_action": "PoC에서는 먼저 하나의 업무를 5~7개 상태로 나누고, 각 상태별 입력값, 출력값, 검증 기준, 실패 처리 방식을 정의하는 방식으로 시작하는 것이 좋습니다.",
            "reference_name": "LangGraph / AutoGen / CrewAI",
            "url": "https://github.com/langchain-ai/langgraph",
            "tags": ["State Graph", "Workflow", "Multi-Agent", "Orchestration"],
        },
        {
            "title": "MCP와 Tool Calling이 에이전트의 외부 시스템 연결 표준으로 부상",
            "category": "도구 호출·프로토콜",
            "technology_layer": "Tool Interface",
            "maturity": "표준화 진행",
            "collected_at": collected_at,
            "core_message": "AI Agent의 실무 가치는 외부 도구와 시스템을 얼마나 안전하고 일관되게 호출할 수 있는지에 달려 있습니다. MCP와 Tool Calling 계열의 흐름은 에이전트가 외부 기능을 사용하는 방식을 표준화하려는 움직임으로 볼 수 있습니다.",
            "technology_context": "초기에는 모델이 API 호출 코드를 직접 생성하거나, 애플리케이션 내부에 도구 호출 로직을 임의로 붙이는 방식이 많았습니다. 최근에는 도구의 이름, 입력 스키마, 반환값, 권한 범위, 실패 응답을 명시적으로 정의하고, 에이전트가 이 계약을 기준으로 도구를 선택하게 하는 구조가 중요해지고 있습니다.",
            "architecture_point": "도구 호출 구조에서는 Tool Registry, Schema Validation, Permission Check, Execution Log가 핵심입니다. 에이전트가 어떤 도구를 왜 호출했는지 기록해야 하며, 입력 파라미터가 잘못된 경우 실행 전에 차단할 수 있어야 합니다.",
            "enterprise_impact": "기업 내부 시스템과 연결할 때는 단순 조회 도구와 변경 도구를 분리해야 합니다. 예를 들어 고객정보 조회, 주문 상태 확인, 결재 문서 생성, 데이터 수정은 위험도가 다르므로 권한과 승인 수준도 달라야 합니다.",
            "risk_point": "도구 호출 권한을 넓게 열어두면 모델의 오판이 실제 데이터 변경으로 이어질 수 있습니다. 특히 삭제, 송금, 승인, 외부 발송 같은 액션은 사람 승인 또는 2단계 확인이 필요합니다.",
            "manager_message": "Agent 도입의 핵심 질문은 ‘모델이 똑똑한가’보다 ‘모델에게 어떤 도구를 어디까지 허용할 것인가’입니다.",
            "recommended_action": "도구 목록을 먼저 위험도 기준으로 조회형, 생성형, 변경형, 외부발송형으로 나누고, 변경형 이상에는 승인 게이트를 두는 구조가 적합합니다.",
            "reference_name": "MCP / Function Calling / Tool Registry",
            "url": "https://modelcontextprotocol.io",
            "tags": ["MCP", "Tool Calling", "API", "Permission"],
        },
        {
            "title": "단기 대화 메모리에서 업무 상태 메모리로 확장",
            "category": "메모리·상태관리",
            "technology_layer": "Memory Architecture",
            "maturity": "설계 고도화",
            "collected_at": collected_at,
            "core_message": "AI Agent의 메모리는 단순히 이전 대화를 기억하는 기능이 아니라, 업무 목표, 진행 상태, 사용자 의사결정, 참조 문서, 실행 이력을 유지하는 구조로 확장되고 있습니다.",
            "technology_context": "일반 챗봇의 메모리는 사용자 선호나 이전 대화 요약을 저장하는 수준에 머무는 경우가 많습니다. 하지만 업무형 Agent에서는 현재 태스크가 어디까지 진행됐는지, 어떤 근거로 결론을 냈는지, 어떤 도구를 호출했는지, 다음 단계가 무엇인지가 중요합니다. 이 때문에 벡터DB, 관계형DB, 그래프DB, 캐시 저장소를 목적별로 조합하는 구조가 필요합니다.",
            "architecture_point": "메모리 계층은 Conversation Memory, Task State, Long-term Knowledge, Execution History로 나누는 것이 좋습니다. 대화 내용과 업무 상태를 섞어 저장하면 검색 정확도와 감사 가능성이 떨어지므로, 저장 목적에 따라 구조를 분리해야 합니다.",
            "enterprise_impact": "장기 업무를 처리하는 Agent에서는 메모리 설계가 품질을 좌우합니다. 예를 들어 심사 보조, 제안서 작성, 고객 응대, 장애 처리처럼 여러 차례 대화와 문서 검토가 이어지는 업무에서는 상태 메모리가 없으면 매번 처음부터 다시 설명해야 합니다.",
            "risk_point": "잘못된 메모리가 누적되면 Agent가 오래된 정보나 잘못된 사용자 의도를 기준으로 판단할 수 있습니다. 따라서 메모리의 유효기간, 삭제 기준, 사용자 수정 가능성, 출처 추적이 필요합니다.",
            "manager_message": "메모리는 ‘많이 저장하는 것’이 아니라 ‘업무 판단에 필요한 상태를 정확히 남기는 것’이 중요합니다.",
            "recommended_action": "초기 설계에서는 메모리를 대화 요약, 업무 상태, 참조 지식, 실행 로그로 분리하고, 각 메모리의 보존 기간과 검색 방식을 다르게 정의하는 것이 좋습니다.",
            "reference_name": "Vector DB / Graph DB / State Store",
            "url": "https://github.com/langchain-ai/langgraph",
            "tags": ["Memory", "State", "Vector DB", "Graph DB"],
        },
        {
            "title": "Agent 평가는 정답률보다 실행 품질과 실패 통제가 중요",
            "category": "평가·운영관리",
            "technology_layer": "Evaluation & Observability",
            "maturity": "운영 필수 요소",
            "collected_at": collected_at,
            "core_message": "AI Agent 평가는 단순히 답변이 맞는지를 보는 수준에서 벗어나, 계획이 적절했는지, 도구 호출이 타당했는지, 중간 결과를 검증했는지, 실패 시 안전하게 중단했는지를 함께 평가해야 합니다.",
            "technology_context": "RAG 평가에서는 검색 정확도, 응답 정합성, 근거 충실성이 중요했다면 Agent 평가에서는 태스크 성공률, 도구 선택 정확도, 실행 단계 누락 여부, 재시도 횟수, 지연 시간, 사람 개입률이 함께 중요합니다. Agent는 답변 생성뿐 아니라 행동을 수행하기 때문에 평가 기준도 실행 중심으로 바뀌어야 합니다.",
            "architecture_point": "운영 구조에는 Trace Log, Step Evaluation, Golden Task Set, Human Review Queue, Failure Taxonomy가 필요합니다. 각 실행 단계별 입력, 판단, 도구 호출, 출력, 오류를 남겨야 개선 포인트를 찾을 수 있습니다.",
            "enterprise_impact": "기업에서는 PoC 성공보다 운영 중 품질 개선이 더 중요합니다. 실제 사용자가 에이전트를 쓰기 시작하면 예외 케이스가 계속 나오기 때문에, 이를 골든셋에 반영하고 반복 평가하는 구조가 있어야 합니다.",
            "risk_point": "평가 체계 없이 Agent를 운영하면 실패 원인을 알 수 없습니다. 모델 문제인지, 데이터 문제인지, 도구 스키마 문제인지, 업무 프로세스 정의 문제인지 구분하지 못하면 개선이 불가능합니다.",
            "manager_message": "Agent 운영의 핵심은 ‘출시’가 아니라 ‘실패 유형을 수집하고 개선 루프를 돌릴 수 있는가’입니다.",
            "recommended_action": "초기부터 업무별 골든 태스크 30~50개를 만들고, 실행 성공률, 단계 누락률, 도구 호출 오류율, 사용자 개입률을 지표로 잡는 것이 좋습니다.",
            "reference_name": "LangSmith / OpenTelemetry / Agent Eval",
            "url": "https://smith.langchain.com",
            "tags": ["Evaluation", "Tracing", "Golden Set", "Monitoring"],
        },
        {
            "title": "기업 업무 Agent는 자동화보다 통제 가능한 위임 구조가 핵심",
            "category": "기업 업무 자동화",
            "technology_layer": "Enterprise Agent",
            "maturity": "도입 검토 확대",
            "collected_at": collected_at,
            "core_message": "기업 업무 Agent는 모든 업무를 완전 자동화하는 도구가 아니라, 사람이 하던 판단과 실행 일부를 통제 가능한 범위 안에서 위임하는 구조로 봐야 합니다.",
            "technology_context": "기업 환경에서 Agent는 문서 검색, 내부 시스템 조회, 보고서 생성, 고객 응대, 승인 요청, 데이터 검증 같은 업무를 연결합니다. 하지만 업무 시스템을 조작하는 순간부터는 권한, 승인, 감사, 보안, 예외 처리 문제가 함께 발생합니다.",
            "architecture_point": "Enterprise Agent 구조에서는 User Role, Data Permission, Action Boundary, Approval Gate, Audit Log가 기본 요소입니다. 특히 조회와 변경 액션을 분리하고, 변경 액션에는 사전 확인과 사후 로그를 남겨야 합니다.",
            "enterprise_impact": "현업 적용 시 가장 효과적인 영역은 규칙이 어느 정도 정해져 있고, 반복성이 높으며, 사람 검토가 필요한 업무입니다. 예를 들어 보고서 초안 작성, 고객 문의 분류, 내부 지식 검색, 발주 데이터 검증, 계약서 체크리스트 검토 같은 영역이 적합합니다.",
            "risk_point": "업무 책임이 불명확한 상태에서 Agent를 도입하면 현업은 결과를 신뢰하지 못하고, IT는 장애 원인을 추적하기 어렵습니다. 따라서 Agent가 수행한 일과 사람이 승인한 일을 명확히 구분해야 합니다.",
            "manager_message": "기업형 Agent는 ‘자동 처리율’을 높이는 것보다 ‘안전하게 위임 가능한 업무 범위’를 넓히는 방식으로 접근해야 합니다.",
            "recommended_action": "처음부터 핵심 업무 전체를 자동화하기보다, 조회·분류·초안 작성처럼 위험도가 낮은 업무부터 시작하고 이후 승인 기반 실행 업무로 확장하는 것이 좋습니다.",
            "reference_name": "ERP / CRM / Groupware Agent",
            "url": "https://www.salesforce.com/agentforce/",
            "tags": ["Enterprise", "Governance", "ERP", "CRM"],
        },
        {
            "title": "웹·OS 실행 Agent는 RPA의 상위 호환이 아니라 별도 통제 영역",
            "category": "웹·OS 실행 에이전트",
            "technology_layer": "Computer Use",
            "maturity": "초기 상용화",
            "collected_at": collected_at,
            "core_message": "웹·OS 실행 Agent는 화면을 인식하고 클릭, 입력, 탐색을 수행할 수 있다는 점에서 기존 RPA보다 유연하지만, 그만큼 예측 불가능성과 보안 리스크도 큽니다.",
            "technology_context": "기존 RPA는 고정된 UI 좌표나 DOM 구조에 의존하는 경우가 많아 화면이 조금만 바뀌어도 실패할 수 있습니다. 반면 Computer Use 계열의 Agent는 화면을 시각적으로 해석하고 다음 행동을 선택할 수 있어 API가 없는 시스템에서도 자동화 가능성을 제공합니다.",
            "architecture_point": "이 구조에서는 Screen Parser, Action Planner, Click Executor, Safety Guard, Human Confirmation이 필요합니다. 특히 로그인, 결제, 삭제, 외부 전송 같은 고위험 액션은 반드시 차단하거나 사람 확인을 거쳐야 합니다.",
            "enterprise_impact": "API가 없는 구형 웹 시스템, 반복 입력 업무, 관리자 페이지 조회, 외부 사이트 정보 수집에는 활용 가능성이 있습니다. 다만 운영 업무에 적용할 때는 전용 계정, 제한된 권한, 허용 URL, 세션 기록이 필요합니다.",
            "risk_point": "화면 기반 Agent는 사용자의 세션과 동일한 권한으로 움직일 수 있습니다. 따라서 잘못된 클릭, 민감 정보 노출, 외부 전송, 보안 정책 위반 가능성을 반드시 통제해야 합니다.",
            "manager_message": "웹·OS Agent는 ‘사람처럼 클릭할 수 있다’가 장점이지만, 기업 적용에서는 ‘사람처럼 실수할 수 있다’는 점까지 함께 봐야 합니다.",
            "recommended_action": "초기 적용은 읽기 전용 업무나 내부 테스트 환경에서 시작하고, 실행 로그와 화면 캡처 이력을 남기는 방식으로 검증하는 것이 안전합니다.",
            "reference_name": "Computer Use / Browser Agent / RPA Extension",
            "url": "https://www.anthropic.com/news/3-5-models-and-computer-use",
            "tags": ["Computer Use", "Browser Agent", "RPA", "Security"],
        },
    ]


def apply_filters(items, query, selected_categories, maturity_filter, layer_filter):
    filtered = []

    for item in items:
        category_ok = item["category"] in selected_categories
        keyword_ok = contains_keyword(item, query)

        if maturity_filter == "전체":
            maturity_ok = True
        else:
            maturity_ok = item.get("maturity") == maturity_filter

        if layer_filter == "전체":
            layer_ok = True
        else:
            layer_ok = item.get("technology_layer") == layer_filter

        if category_ok and keyword_ok and maturity_ok and layer_ok:
            filtered.append(item)

    return filtered


def render_summary_block(selected_categories):
    st.markdown("#### Executive Summary")

    for item in REPORT_SUMMARY[CATEGORY_ALL]:
        with st.container(border=True):
            st.markdown(f"##### {item['title']}")
            st.write(item["body"])

    st.markdown("#### 기술 관점 요약")

    if len(selected_categories) == len(CATEGORIES):
        st.write(
            "현재 트렌드는 에이전트 오케스트레이션, 도구 호출 표준화, 상태 메모리, 실행 평가, 기업 거버넌스, 웹·OS 조작 자동화로 나누어 볼 수 있습니다. "
            "이 중 실무 도입에서 가장 먼저 점검해야 할 영역은 도구 권한, 실행 로그, 사람 승인 단계, 실패 복구 구조입니다."
        )
    else:
        selected_text = ", ".join(selected_categories)
        st.write(
            f"현재 선택된 영역은 {selected_text}입니다. 이 영역은 단순 기능 구현보다 운영 안정성과 통제 구조가 중요합니다. "
            "특히 Agent가 실제 시스템을 조회하거나 변경하는 경우에는 기술 검토와 업무 권한 설계를 함께 진행해야 합니다."
        )


def render_trend_card(item):
    with st.container(border=True):
        st.caption(
            f"{item['category']}  ·  {item['technology_layer']}  ·  "
            f"{item['maturity']}"
        )

        st.markdown(f"#### {item['title']}")

        with st.expander("상세 내용 보기", expanded=True):
            st.markdown("##### 핵심 메시지")
            st.write(item["core_message"])

            st.markdown("##### 기술 구조")
            st.write(item["technology_context"])

            st.markdown("##### 아키텍처 포인트")
            st.write(item["architecture_point"])

            st.markdown("##### 기업 적용 시사점")
            st.write(item["enterprise_impact"])

            st.markdown("##### 리스크 및 확인사항")
            st.write(item["risk_point"])

            st.info(f"현업 메시지: {item['manager_message']}")

            st.markdown("##### 다음 액션")
            st.write(item["recommended_action"])

            tag_text = " · ".join(item.get("tags", []))
            st.caption(
                f"참고 영역: {item.get('reference_name', '미분류')}  |  "
                f"태그: {tag_text}"
            )

        st.link_button("원문 보기", item["url"], use_container_width=True)


trend_items = load_trend_items()


with st.sidebar:
    st.markdown("### 검색 및 필터")

    query_input = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, 평가, 메모리, ERP, Computer Use",
    )

    selected_categories = st.multiselect(
        "기술 분류",
        options=CATEGORIES,
        default=CATEGORIES,
    )

    maturity_values = ["전체"] + sorted({item["maturity"] for item in trend_items})
    maturity_filter = st.selectbox("성숙도", maturity_values)

    layer_values = ["전체"] + sorted({item["technology_layer"] for item in trend_items})
    layer_filter = st.selectbox("기술 레이어", layer_values)

    sort_option = st.radio(
        "정렬 기준",
        ["기본 정렬", "기술 분류순", "제목순"],
        horizontal=False,
    )

    st.divider()

    if st.button("실시간 동기화", use_container_width=True):
        with st.spinner("기술 트렌드 데이터를 동기화하는 중입니다."):
            time.sleep(0.5)
            st.cache_data.clear()
        st.toast("동기화가 완료되었습니다.", icon="✅")
        st.rerun()


if not selected_categories:
    selected_categories = CATEGORIES


filtered_items = apply_filters(
    items=trend_items,
    query=query_input,
    selected_categories=selected_categories,
    maturity_filter=maturity_filter,
    layer_filter=layer_filter,
)

if sort_option == "기술 분류순":
    filtered_items = sorted(filtered_items, key=lambda x: x["category"])
elif sort_option == "제목순":
    filtered_items = sorted(filtered_items, key=lambda x: x["title"])
else:
    filtered_items = list(filtered_items)


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 갱신: {now_kst_text()} KST")
st.write(
    "AI Agent 기술을 단순 뉴스 단위가 아니라, 아키텍처 변화와 기업 적용 관점에서 정리한 기술 브리핑입니다."
)

st.divider()


summary_tab, report_tab, data_tab = st.tabs(
    ["핵심요약", "상세리포트", "수집 데이터"]
)


with summary_tab:
    render_summary_block(selected_categories)


with report_tab:
    st.markdown("#### 상세리포트")

    if query_input:
        st.caption(f"검색어: {query_input}")

    if not filtered_items:
        st.info("현재 검색 조건에 맞는 기술 트렌드가 없습니다. 검색어 또는 필터를 조정해보세요.")
    else:
        for item in filtered_items:
            render_trend_card(item)


with data_tab:
    st.markdown("#### 수집 데이터 원본")
    st.caption(
        "관리자 점검용 화면입니다. 실제 운영에서는 크롤러가 수집한 원문 제목, 출처, 발행일, 요약, 태그, 검증 상태를 이 영역에서 확인할 수 있습니다."
    )

    st.dataframe(
        filtered_items,
        hide_index=True,
        use_container_width=True,
        column_order=[
            "title",
            "category",
            "technology_layer",
            "maturity",
            "core_message",
            "reference_name",
            "collected_at",
            "tags",
            "url",
        ],
    )
