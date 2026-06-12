import streamlit as st
import time
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))
IS_SAMPLE_DATA = True


st.set_page_config(
    page_title="AI Agent 기술 트렌드",
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


REPORT_SUMMARY = {
    CATEGORY_ALL: [
        {
            "title": "종합 판단",
            "body": "AI Agent 기술은 단순 챗봇이나 문서 검색 도구를 넘어, 목표를 이해하고 도구를 호출하며 업무 단계를 이어가는 실행형 구조로 이동하고 있습니다. 최근 흐름의 핵심은 모델 자체보다도 상태 관리, 도구 연동, 권한 통제, 평가 체계를 함께 묶는 운영 구조에 있습니다.",
        },
        {
            "title": "기술 구조 변화",
            "body": "단일 LLM이 모든 업무를 처리하는 방식보다는 역할이 분리된 에이전트들을 오케스트레이션하는 구조가 확산되고 있습니다. 이 과정에서 LangGraph, AutoGen 계열처럼 상태 전이, 재시도, 분기, 관찰 가능성을 지원하는 프레임워크의 중요성이 커지고 있습니다.",
        },
        {
            "title": "기업 적용 시사점",
            "body": "기업 환경에서는 RAG만으로는 충분하지 않습니다. ERP, CRM, 그룹웨어, 데이터베이스, 승인 시스템과 연결되면서 실제 업무 트랜잭션을 처리할 수 있어야 하며, 이때 감사 로그와 권한 체계가 반드시 함께 설계되어야 합니다.",
        },
        {
            "title": "리스크 및 확인사항",
            "body": "웹·OS 조작형 에이전트는 API가 없는 업무까지 자동화할 수 있다는 장점이 있지만, 화면 변경, 오작동, 민감 정보 노출 위험이 있습니다. 초기 적용은 완전 자율보다 사람 검토 단계를 포함한 반자동 구조가 현실적입니다.",
        },
    ],
    "🛠️ 오픈소스 에이전트 프레임워크": [
        {
            "title": "종합 판단",
            "body": "오픈소스 에이전트 프레임워크는 실험용 데모 수준에서 벗어나, 상태 관리와 실행 흐름을 안정적으로 제어하는 방향으로 발전하고 있습니다.",
        },
        {
            "title": "기술 구조 변화",
            "body": "최근 프레임워크의 핵심은 프롬프트 체이닝이 아니라, 에이전트 상태, 도구 호출, 실패 복구, 메모리 유지, 실행 로그를 구조적으로 관리하는 데 있습니다.",
        },
        {
            "title": "기업 적용 시사점",
            "body": "프레임워크 선택 시에는 기능 목록보다 운영 환경과의 적합성을 우선해야 합니다. 특히 로그 추적, 테스트 자동화, 버전 관리, 평가 데이터셋 연계 여부가 중요합니다.",
        },
        {
            "title": "리스크 및 확인사항",
            "body": "오픈소스 생태계는 변화 속도가 빠르기 때문에 장기 운영 관점에서는 커뮤니티 활성도, 문서 품질, 하위 호환성, 보안 업데이트 주기를 확인해야 합니다.",
        },
    ],
    "🏢 기업 업무 자동화 에이전트": [
        {
            "title": "종합 판단",
            "body": "기업 업무 자동화 에이전트는 문서 검색과 요약을 넘어, 내부 시스템을 조회하고 업무 요청을 생성하며 예외 상황을 처리하는 방향으로 확장되고 있습니다.",
        },
        {
            "title": "기술 구조 변화",
            "body": "업무 자동화형 에이전트는 LLM, RAG, API 연동, 워크플로우 엔진, 권한 체계가 결합된 구조로 설계되는 흐름입니다.",
        },
        {
            "title": "기업 적용 시사점",
            "body": "실제 업무에 적용하려면 태스크 단위가 명확해야 합니다. 단순히 AI를 붙이는 것보다 어떤 업무를 자동화하고, 어느 단계에서 사람 승인을 받을지 정의하는 것이 우선입니다.",
        },
        {
            "title": "리스크 및 확인사항",
            "body": "업무 시스템을 직접 조작하는 경우 오작동의 영향이 큽니다. 따라서 실행 전 검증, 승인 단계, 감사 로그, 롤백 절차가 반드시 필요합니다.",
        },
    ],
    "🖥️ 자율형 웹/OS 브라우징 에이전트": [
        {
            "title": "종합 판단",
            "body": "자율형 웹·OS 브라우징 에이전트는 API가 없는 구형 업무 환경까지 자동화할 수 있다는 점에서 주목받고 있습니다.",
        },
        {
            "title": "기술 구조 변화",
            "body": "기존 스크래퍼나 RPA가 DOM 구조나 고정 좌표에 의존했다면, 최근 방식은 화면을 인식하고 상황에 따라 클릭과 입력 경로를 조정하는 방향입니다.",
        },
        {
            "title": "기업 적용 시사점",
            "body": "API 연동이 어려운 레거시 시스템, 반복 입력 업무, 웹 기반 정보 수집 업무에는 적용 가능성이 있습니다. 다만 초기에는 사람 확인이 포함된 보조 자동화 형태가 적합합니다.",
        },
        {
            "title": "리스크 및 확인사항",
            "body": "화면 조작형 에이전트는 계정, 쿠키, 내부 시스템 화면에 접근할 수 있으므로 허용 도메인, 작업 범위, 계정 권한, 실행 로그를 강하게 제한해야 합니다.",
        },
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


def render_summary_block(selected_categories):
    if len(selected_categories) == len(CATEGORIES):
        summary_items = REPORT_SUMMARY[CATEGORY_ALL]
        st.markdown("#### 전체 기술 동향 요약")
        for item in summary_items:
            with st.container(border=True):
                st.markdown(f"##### {item['title']}")
                st.write(item["body"])
    else:
        for category in selected_categories:
            st.markdown(f"#### {category}")
            for item in REPORT_SUMMARY[category]:
                with st.container(border=True):
                    st.markdown(f"##### {item['title']}")
                    st.write(item["body"])
            st.write("")


def render_article_card(article):
    with st.container(border=True):
        st.caption(
            f"{article['category']}  ·  {article['source']}  ·  "
            f"수집 {article['collected_at']}"
        )

        st.markdown(f"#### {article['title']}")

        with st.expander("상세 내용 보기", expanded=True):
            st.write(article["content"])
            st.info(f"현업 관점: {article['insight']}")

            tag_text = " · ".join(article.get("tags", []))
            st.caption(
                f"출처 성격: {article.get('source_type', '미분류')}  |  "
                f"검증 상태: {article.get('verification', '미확인')}  |  "
                f"태그: {tag_text}"
            )

        st.link_button("원문 보기", article["url"], use_container_width=True)


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

    st.divider()

    if st.button("실시간 동기화", use_container_width=True):
        with st.spinner("크롤링 데이터를 동기화하는 중입니다."):
            time.sleep(0.5)
            st.cache_data.clear()
        st.toast("동기화가 완료되었습니다.", icon="✅")
        st.rerun()

    st.caption("운영 전환 시 load_articles() 함수에 실제 크롤러 결과를 연결하세요.")


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


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 갱신: {now_kst_text()} KST")
st.write("AI Agent 관련 최신 기술 흐름을 수집하고, 실무 적용 관점에서 구조화한 브리핑 리포트입니다.")

if IS_SAMPLE_DATA:
    st.caption(
        "현재는 샘플 데이터 기준입니다. 실제 운영 시에는 크롤러 수집 결과와 검증 상태를 연결하는 것을 권장합니다."
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

    if not filtered_articles:
        st.info("현재 검색 조건에 맞는 리포트가 없습니다. 검색어 또는 필터를 조정해보세요.")
    else:
        for article in filtered_articles:
            render_article_card(article)


with data_tab:
    st.markdown("#### 수집 데이터 원본")
    st.caption(
        "운영 단계에서는 관리자 점검용으로 남겨두면 제목, 출처, 검증 상태, 태그 오류를 빠르게 확인할 수 있습니다."
    )

    st.dataframe(
        filtered_articles,
        hide_index=True,
        use_container_width=True,
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
