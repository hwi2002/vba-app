import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))

st.set_page_config(
    page_title="AI Agent 기술 트렌드",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


RSS_SOURCES = [
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml",
    },
    {
        "name": "Anthropic News",
        "url": "https://www.anthropic.com/news/rss.xml",
    },
    {
        "name": "LangChain Blog",
        "url": "https://blog.langchain.dev/rss/",
    },
    {
        "name": "Microsoft AI Blog",
        "url": "https://blogs.microsoft.com/ai/feed/",
    },
    {
        "name": "AWS Machine Learning Blog",
        "url": "https://aws.amazon.com/blogs/machine-learning/feed/",
    },
    {
        "name": "Google Cloud Blog",
        "url": "https://cloud.google.com/blog/rss",
    },
]


CATEGORY_RULES = {
    "에이전트 오케스트레이션": [
        "agent", "agents", "multi-agent", "workflow", "orchestration",
        "langgraph", "autogen", "crewai", "planner", "executor"
    ],
    "도구 호출·프로토콜": [
        "tool", "tools", "function calling", "mcp", "model context protocol",
        "api", "connector", "integration"
    ],
    "메모리·상태관리": [
        "memory", "state", "context", "long-term", "retrieval", "rag",
        "vector", "knowledge graph"
    ],
    "평가·운영관리": [
        "eval", "evaluation", "monitoring", "observability", "trace",
        "benchmark", "safety", "guardrail"
    ],
    "기업 업무 자동화": [
        "enterprise", "business", "workflow", "automation", "crm", "erp",
        "salesforce", "operation", "productivity"
    ],
    "웹·OS 실행 에이전트": [
        "computer use", "browser", "web", "desktop", "screen", "click",
        "operator", "automation"
    ],
}


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def clean_text(text):
    if not text:
        return ""

    return (
        text.replace("\n", " ")
        .replace("\t", " ")
        .replace("  ", " ")
        .strip()
    )


def classify_category(title, summary):
    text = f"{title} {summary}".lower()

    scores = {}

    for category, keywords in CATEGORY_RULES.items():
        score = sum(1 for keyword in keywords if keyword.lower() in text)
        scores[category] = score

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return None

    return best_category


def make_report_fields(title, summary, category, source_name):
    base_summary = clean_text(summary)

    if len(base_summary) > 600:
        base_summary = base_summary[:600] + "..."

    return {
        "core_message": f"이 글은 {category} 관점에서 볼 필요가 있습니다. 단순 AI 뉴스라기보다 Agent 구조가 실제 업무 실행 체계로 확장되는 흐름과 연결됩니다.",
        "technology_context": base_summary if base_summary else "원문 요약 정보가 충분하지 않습니다. 원문을 열어 세부 내용을 확인해야 합니다.",
        "architecture_point": "아키텍처 관점에서는 이 내용이 Agent의 어떤 레이어에 해당하는지 구분해야 합니다. 예를 들어 오케스트레이션, 도구 호출, 메모리, 평가, 권한 통제 중 어디에 영향을 주는지 확인하는 것이 중요합니다.",
        "enterprise_impact": "기업 적용 관점에서는 기술 자체보다 업무 시스템과 연결했을 때의 통제 구조가 중요합니다. 내부 데이터 접근, 승인 단계, 실행 로그, 실패 시 사람 개입 기준을 함께 설계해야 합니다.",
        "risk_point": "검증되지 않은 자동 실행은 운영 리스크가 큽니다. 실제 업무 적용 전에는 원문 내용, 기능 범위, 보안 조건, 실패 처리 방식을 별도로 확인해야 합니다.",
        "manager_message": f"{source_name}에서 나온 단일 기사로 끝내기보다, 같은 주제의 다른 벤더 발표나 오픈소스 변화와 함께 묶어 기술 테마로 관리하는 것이 좋습니다.",
        "recommended_action": "이 항목은 기술 레이더에 등록한 뒤, 관련 프레임워크·제품·레퍼런스를 추가 수집해 PoC 후보인지 관찰 대상으로만 둘지 판단하는 것이 적합합니다.",
    }


@st.cache_data(ttl=3600, show_spinner=False)
def crawl_trend_items():
    collected_at = now_kst_text()
    items = []

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        for entry in feed.entries[:10]:
            title = clean_text(entry.get("title", ""))
            summary = clean_text(entry.get("summary", ""))
            link = entry.get("link", "")

            if not title or not link:
                continue

            category = classify_category(title, summary)

            if category is None:
                continue

            report_fields = make_report_fields(
                title=title,
                summary=summary,
                category=category,
                source_name=source["name"],
            )

            items.append(
                {
                    "title": title,
                    "category": category,
                    "source": source["name"],
                    "published_at": entry.get("published", "발행일 확인 필요"),
                    "collected_at": collected_at,
                    "url": link,
                    "tags": [category, source["name"]],
                    **report_fields,
                }
            )

    return items, collected_at


def contains_keyword(item, keyword):
    if not keyword:
        return True

    keyword = keyword.lower()

    text = " ".join(
        [
            item.get("title", ""),
            item.get("category", ""),
            item.get("source", ""),
            item.get("core_message", ""),
            item.get("technology_context", ""),
            item.get("architecture_point", ""),
            item.get("enterprise_impact", ""),
            item.get("risk_point", ""),
            item.get("manager_message", ""),
            item.get("recommended_action", ""),
        ]
    ).lower()

    return keyword in text


def render_summary(items):
    st.markdown("#### Executive Summary")

    st.write(
        "이번 브리핑은 단순 AI 뉴스 모음이 아니라, 수집된 원문을 AI Agent 기술 구조 관점에서 재분류한 결과입니다. "
        "핵심 관찰 포인트는 에이전트 오케스트레이션, 도구 호출 표준화, 메모리·상태관리, 평가·운영관리, 기업 업무 자동화, 웹·OS 실행 에이전트입니다."
    )

    if not items:
        st.info("현재 수집된 AI Agent 관련 항목이 없습니다. 동기화 버튼을 누르거나 RSS 소스를 추가해보세요.")
        return

    category_counts = {}

    for item in items:
        category_counts[item["category"]] = category_counts.get(item["category"], 0) + 1

    st.markdown("#### 기술 테마별 해석")

    for category, count in category_counts.items():
        with st.container(border=True):
            st.markdown(f"##### {category}")
            st.write(
                f"이번 수집 결과에서 이 영역은 {count}개 항목으로 확인됩니다. "
                "단순 기사 개수보다 중요한 것은 이 주제가 Agent 구조의 어느 레이어에 영향을 주는지입니다. "
                "실무 적용 전에는 관련 원문을 확인하고, 내부 업무 시스템과 연결될 때 필요한 권한·로그·검증 구조를 함께 검토해야 합니다."
            )


def render_card(item):
    with st.container(border=True):
        st.caption(
            f"{item['category']} · {item['source']} · 발행 {item['published_at']} · 수집 {item['collected_at']}"
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

        st.link_button("원문 보기", item["url"], use_container_width=True)


items, last_collected_at = crawl_trend_items()

categories = sorted({item["category"] for item in items})
sources = sorted({item["source"] for item in items})

with st.sidebar:
    st.markdown("### 검색 및 필터")

    query = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, Agent, RAG, Computer Use, Evaluation",
    )

    selected_categories = st.multiselect(
        "기술 분류",
        options=categories,
        default=categories,
    )

    selected_sources = st.multiselect(
        "출처",
        options=sources,
        default=sources,
    )

    st.divider()

    if st.button("실시간 동기화", use_container_width=True):
        with st.spinner("AI Agent 기술 동향을 다시 수집하는 중입니다."):
            st.cache_data.clear()
        st.toast("동기화가 완료되었습니다.", icon="✅")
        st.rerun()


filtered_items = []

for item in items:
    category_ok = not selected_categories or item["category"] in selected_categories
    source_ok = not selected_sources or item["source"] in selected_sources
    keyword_ok = contains_keyword(item, query)

    if category_ok and source_ok and keyword_ok:
        filtered_items.append(item)


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 수집: {last_collected_at} KST")
st.write(
    "AI Agent 관련 원문을 수집한 뒤, 단순 뉴스 목록이 아니라 기술 구조와 기업 적용 관점으로 재분류한 브리핑입니다."
)

st.divider()

summary_tab, report_tab, data_tab = st.tabs(
    ["핵심요약", "상세리포트", "수집 데이터"]
)

with summary_tab:
    render_summary(filtered_items)

with report_tab:
    st.markdown("#### 상세리포트")

    if not filtered_items:
        st.info("현재 조건에 맞는 항목이 없습니다. 검색어 또는 필터를 조정해보세요.")
    else:
        for item in filtered_items:
            render_card(item)

with data_tab:
    st.markdown("#### 수집 데이터 원본")

    df = pd.DataFrame(filtered_items)

    if df.empty:
        st.info("표시할 데이터가 없습니다.")
    else:
        st.dataframe(
            df[
                [
                    "title",
                    "category",
                    "source",
                    "published_at",
                    "collected_at",
                    "url",
                ]
            ],
            hide_index=True,
            use_container_width=True,
        )
