import streamlit as st
import time
from collections import Counter
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))
IS_SAMPLE_DATA = True


st.set_page_config(
    page_title="AI Agent Briefing",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


CATEGORY_ALL = "전체 보기"

CATEGORIES = [
    "🛠️ 오픈소스 에이전트 프레임워크",
    "🏢 기업 업무 자동화 에이전트",
    "🖥️ 자율형 웹/OS 브라우징 에이전트",
]

SUMMARY_DATA = {
    CATEGORY_ALL: [
        "AI Agent 시장은 단순 질의응답형 챗봇에서 벗어나, 목표를 이해하고 여러 도구를 호출하며 업무 단계를 이어가는 실행형 구조로 이동하고 있습니다.",
        "기업 적용 관점에서는 RAG, 도구 호출, 권한 관리, 평가 체계, 운영 모니터링이 함께 묶여야 실제 업무 자동화로 이어집니다.",
        "최근 구조 설계의 핵심은 하나의 거대한 에이전트가 모든 일을 처리하는 방식보다, 역할이 분리된 여러 에이전트를 오케스트레이션하는 방식에 가깝습니다.",
    ],
    "🛠️ 오픈소스 에이전트 프레임워크": [
        "LangChain, LangGraph, AutoGen 계열처럼 에이전트의 상태, 도구 호출, 분기, 재시도 흐름을 구조화하려는 프레임워크 경쟁이 계속되고 있습니다.",
        "실무에서는 단순 데모보다 상태 관리, 관찰 가능성, 평가 자동화, 실패 복구 흐름을 얼마나 안정적으로 제공하는지가 중요합니다.",
        "프레임워크 선택 시에는 기능 수보다 팀의 개발 방식, 운영 환경, 로그 추적 체계와 잘 맞는지를 우선 확인해야 합니다.",
    ],
    "🏢 기업 업무 자동화 에이전트": [
        "기업 업무 자동화 에이전트는 문서 검색 수준을 넘어 ERP, CRM, 그룹웨어, 데이터베이스, 승인 시스템과 연결되는 방향으로 확장되고 있습니다.",
        "다만 실제 업무 시스템을 조작하는 순간 권한, 감사 로그, 승인 절차, 예외 처리 기준이 반드시 필요합니다.",
        "업무 자동화 품질은 모델 성능만으로 결정되지 않고, 데이터 품질, 프로세스 정의, 운영 피드백 루프에 크게 좌우됩니다.",
    ],
    "🖥️ 자율형 웹/OS 브라우징 에이전트": [
        "웹/OS 브라우징 에이전트는 API가 없는 화면 기반 업무를 처리할 수 있다는 장점이 있지만, UI 변경과 보안 정책에 취약할 수 있습니다.",
        "사람처럼 화면을 보고 클릭하는 구조는 강력하지만, 기업 환경에서는 민감 정보 노출, 오작동, 권한 남용을 통제하는 장치가 필요합니다.",
        "실무 적용 시에는 완전 자율보다는 사람 검토 단계가 포함된 반자동 흐름으로 시작하는 편이 안전합니다.",
    ],
}


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def normalize_text(value):
    return str(value or "").casefold().strip()


def contains_keyword(article, keyword):
    keyword = normalize_text(keyword)

    if not keyword:
        return True

    searchable_text = " ".join(
        [
            article.get("title", ""),
            article.get("content", ""),
            article.get("insight", ""),
            article.get("source", ""),
            " ".join(article.get("tags", [])),
        ]
    )

    return keyword in normalize_text(searchable_text)


@st.cache_data(ttl=600, show_spinner=False)
def load_articles():
    """
    실제 크롤러가 있다면 이 함수만 교체하시면 됩니다.

    권장 반환 구조:
    [
        {
            "title": "...",
            "category": "...",
            "source": "...",
            "published_at": "...",
            "collected_at": "...",
            "content": "...",
            "insight": "...",
            "url": "...",
            "source_type": "공식 블로그 / 기술매체 / GitHub / 기타",
            "verification": "확인 완료 / 확인 필요 / 샘플 데이터",
            "tags": ["MCP", "Agent", "RAG"]
        }
    ]
    """

    collected_at = now_kst_text()

    return [
        {
            "title": "LangChain 기반 멀티 에이전트 협업 워크플로우 동향",
            "category": "🛠️ 오픈소스 에이전트 프레임워크",
            "source": "LangChain Blog",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "역할이 분리된 여러 에이전트가 기획, 실행, 검증 단계를 나누어 처리하는 구조가 확산되고 있습니다.",
            "insight": "PoC 단계에서는 멋진 데모보다 실패 시 재시도, 상태 추적, 로그 확인 구조가 더 중요합니다.",
            "url": "https://www.langchain.com",
            "source_type": "공식/벤더",
            "verification": "샘플 데이터",
            "tags": ["LangChain", "LangGraph", "Multi-Agent"],
        },
        {
            "title": "기업 업무 자동화 에이전트의 ERP·CRM 연동 확대",
            "category": "🏢 기업 업무 자동화 에이전트",
            "source": "Enterprise AI Brief",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "기업용 에이전트는 문서 요약과 검색을 넘어 내부 시스템 조회, 데이터 검증, 업무 요청 생성까지 확장되는 흐름입니다.",
            "insight": "업무 시스템을 직접 조작하려면 권한 통제, 승인 단계, 감사 로그가 설계에 포함되어야 합니다.",
            "url": "https://example.com",
            "source_type": "기술매체",
            "verification": "샘플 데이터",
            "tags": ["ERP", "CRM", "Workflow"],
        },
        {
            "title": "화면 기반 웹·OS 조작 에이전트 적용 가능성",
            "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
            "source": "AI Automation Watch",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "API가 제공되지 않는 구형 시스템에서도 화면 인식과 클릭 제어를 통해 반복 업무를 처리하려는 시도가 늘고 있습니다.",
            "insight": "초기 적용은 완전 자율보다 사람 확인 단계가 있는 반자동 방식이 더 안전합니다.",
            "url": "https://example.com",
            "source_type": "기술매체",
            "verification": "샘플 데이터",
            "tags": ["Computer Use", "Browser Agent", "RPA"],
        },
        {
            "title": "AutoGen 계열 프레임워크의 에이전트 대화·실행 구조",
            "category": "🛠️ 오픈소스 에이전트 프레임워크",
            "source": "GitHub",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "여러 에이전트가 메시지를 주고받으며 문제를 분해하고, 필요한 경우 코드 실행이나 도구 호출을 연결하는 방식이 활용되고 있습니다.",
            "insight": "실무형 에이전트는 대화 흐름보다 결과 검증, 도구 권한, 실행 제한이 더 중요합니다.",
            "url": "https://github.com",
            "source_type": "GitHub",
            "verification": "샘플 데이터",
            "tags": ["AutoGen", "Tool Use", "Orchestration"],
        },
        {
            "title": "업무 에이전트 운영을 위한 평가·모니터링 필요성",
            "category": "🏢 기업 업무 자동화 에이전트",
            "source": "AI Governance Note",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "에이전트를 운영하려면 정답률뿐 아니라 실패 유형, 지연 시간, 재시도 횟수, 사용자 개입률을 함께 추적해야 합니다.",
            "insight": "운영 대시보드가 없으면 PoC 이후 품질 개선 루프가 끊길 가능성이 큽니다.",
            "url": "https://example.com",
            "source_type": "분석/리포트",
            "verification": "샘플 데이터",
            "tags": ["Evaluation", "Monitoring", "Governance"],
        },
        {
            "title": "웹 브라우징 에이전트의 보안 통제 이슈",
            "category": "🖥️ 자율형 웹/OS 브라우징 에이전트",
            "source": "Security Review",
            "published_at": "크롤러 입력값 필요",
            "collected_at": collected_at,
            "content": "브라우저 조작형 에이전트는 계정, 쿠키, 내부 화면에 접근할 수 있어 민감 정보 통제와 실행 범위 제한이 필요합니다.",
            "insight": "사내 적용 시에는 계정 분리, 허용 도메인 제한, 작업 로그 저장을 기본값으로 두는 편이 안전합니다.",
            "url": "https://example.com",
            "source_type": "보안/리스크",
            "verification": "샘플 데이터",
            "tags": ["Security", "Browser Agent", "Audit"],
        },
    ]


def apply_filters(articles, query, selected_categories, verification_filter, source_type_filter):
    filtered = []

    for article in articles:
        category_ok = article["category"] in selected_categories
        keyword_ok = contains_keyword(article, query)

        if verification_filter == "전체":
            verification_ok = True
        else:
            verification_ok = article.get("verification") == verification_filter

        if source_type_filter == "전체":
            source_type_ok = True
        else:
            source_type_ok = article.get("source_type") == source_type_filter

        if category_ok and keyword_ok and verification_ok and source_type_ok:
            filtered.append(article)

    return filtered


def render_article_card(article, compact_mode):
    with st.container(border=True):
        meta_col, action_col = st.columns([4, 1])

        with meta_col:
            st.caption(
                f"{article['category']}  ·  {article['source']}  ·  "
                f"수집 {article['collected_at']}"
            )
            st.markdown(f"#### {article['title']}")

        with action_col:
            st.link_button("원문 보기", article["url"], width="stretch")

        if compact_mode:
            with st.expander("상세 내용 보기"):
                st.write(article["content"])
                st.info(f"현업 관점: {article['insight']}")
        else:
            st.write(article["content"])
            st.info(f"현업 관점: {article['insight']}")

        tag_text = " · ".join(article.get("tags", []))
        st.caption(
            f"출처 성격: {article.get('source_type', '미분류')}  |  "
            f"검증 상태: {article.get('verification', '미확인')}  |  "
            f"태그: {tag_text}"
        )


articles = load_articles()

with st.sidebar:
    st.markdown("### 검색 및 필터")

    query_input = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, AutoGen, RAG, ERP, Browser Agent",
    )

    selected_categories = st.multiselect(
        "기술 분류",
        options=CATEGORIES,
        default=CATEGORIES,
    )

    verification_values = ["전체"] + sorted({item["verification"] for item in articles})
    verification_filter = st.selectbox("검증 상태", verification_values)

    source_type_values = ["전체"] + sorted({item["source_type"] for item in articles})
    source_type_filter = st.selectbox("출처 성격", source_type_values)

    sort_option = st.radio(
        "정렬 기준",
        ["수집 최신순", "출처명순", "제목순"],
        horizontal=False,
    )

    compact_mode = st.checkbox("본문 접기", value=True)

    st.divider()

    if st.button("실시간 동기화", width="stretch"):
        with st.spinner("크롤링 데이터를 동기화하는 중입니다."):
            time.sleep(0.5)
            st.cache_data.clear()
        st.toast("동기화가 완료되었습니다.", icon="✅")
        st.rerun()

    st.caption("크롤러를 연결한 뒤에는 샘플 데이터 경고를 끄고 운영하시면 됩니다.")


if not selected_categories:
    selected_categories = CATEGORIES

filtered_articles = apply_filters(
    articles=articles,
    query=query_input,
    selected_categories=selected_categories,
    verification_filter=verification_filter,
    source_type_filter=source_type_filter,
)

if sort_option == "출처명순":
    filtered_articles = sorted(filtered_articles, key=lambda x: x["source"])
elif sort_option == "제목순":
    filtered_articles = sorted(filtered_articles, key=lambda x: x["title"])
else:
    filtered_articles = list(filtered_articles)


st.title("🧭 AI Agent Briefing")
st.caption("AI Agent 기술 동향을 수집, 분류, 요약하는 브리핑 대시보드입니다.")

if IS_SAMPLE_DATA:
    st.warning(
        "현재 화면은 샘플 데이터 기준입니다. 실제 서비스처럼 보이게 하려면 "
        "load_articles() 함수에 크롤러 결과를 연결하고, verification 값을 실제 검증 상태로 바꾸세요."
    )

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

category_counter = Counter(item["category"] for item in filtered_articles)
source_counter = Counter(item["source_type"] for item in filtered_articles)

metric_col1.metric("노출 리포트", f"{len(filtered_articles)}건", border=True)
metric_col2.metric("선택 분류", f"{len(selected_categories)}개", border=True)
metric_col3.metric("출처 유형", f"{len(source_counter)}개", border=True)
metric_col4.metric("마지막 갱신", now_kst_text(), border=True)

st.divider()

summary_tab, report_tab, data_tab = st.tabs(
    ["핵심 요약", "상세 리포트", "수집 데이터"]
)

with summary_tab:
    st.subheader("브리핑 요약")

    if len(selected_categories) == len(CATEGORIES):
        summary_key = CATEGORY_ALL
        st.markdown(f"##### {CATEGORY_ALL}")
        for sentence in SUMMARY_DATA[summary_key]:
            st.write(f"• {sentence}")
    else:
        for category in selected_categories:
            st.markdown(f"##### {category}")
            for sentence in SUMMARY_DATA[category]:
                st.write(f"• {sentence}")
            st.write("")

    st.info(
        "운영용으로 전환할 때는 요약 문장도 고정 문구가 아니라, "
        "수집된 기사 본문을 기준으로 별도 요약 함수에서 생성하도록 분리하는 편이 좋습니다."
    )

with report_tab:
    st.subheader("상세 리포트")

    if query_input:
        st.caption(f"검색어: {query_input}")

    if not filtered_articles:
        st.info("현재 검색 조건에 맞는 리포트가 없습니다. 검색어 또는 필터를 조정해보세요.")
    else:
        for article in filtered_articles:
            render_article_card(article, compact_mode=compact_mode)

with data_tab:
    st.subheader("수집 데이터 원본")

    st.caption(
        "운영 단계에서는 이 표를 관리자 확인용으로 남겨두면, "
        "제목·출처·검증 상태·태그 오류를 빠르게 점검할 수 있습니다."
    )

    st.dataframe(
        filtered_articles,
        hide_index=True,
        width="stretch",
        column_order=[
            "title",
            "category",
            "source",
            "source_type",
            "verification",
            "published_at",
            "collected_at",
            "tags",
            "url",
        ],
    )
