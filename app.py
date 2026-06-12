import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9))

st.set_page_config(
    page_title="AI Agent 기술 트렌드",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)


RSS_SOURCES = [
    ("OpenAI Blog", "https://openai.com/blog/rss.xml"),
    ("Anthropic News", "https://www.anthropic.com/news/rss.xml"),
    ("LangChain Blog", "https://blog.langchain.dev/rss/"),
    ("Microsoft AI Blog", "https://blogs.microsoft.com/ai/feed/"),
    ("AWS ML Blog", "https://aws.amazon.com/blogs/machine-learning/feed/"),
]


CATEGORY_RULES = {
    "Agent Orchestration": [
        "agent", "agents", "multi-agent", "workflow", "orchestration",
        "langgraph", "autogen", "crewai", "planner", "executor"
    ],
    "MCP & Tool Calling": [
        "mcp", "model context protocol", "tool", "tools",
        "function calling", "api", "connector", "integration"
    ],
    "Memory & State Management": [
        "memory", "state", "context", "rag", "retrieval",
        "vector", "knowledge graph"
    ],
    "Agent Evaluation & AgentOps": [
        "eval", "evaluation", "benchmark", "monitoring",
        "observability", "trace", "safety", "guardrail"
    ],
    "Enterprise Agent Architecture": [
        "enterprise", "business", "automation", "crm", "erp",
        "operation", "productivity"
    ],
    "Computer Use & Browser Agent": [
        "computer use", "browser", "web", "desktop",
        "screen", "click", "operator"
    ],
}


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def clean_text(text):
    return str(text or "").replace("\n", " ").replace("\t", " ").strip()


def classify_article(title, summary):
    text = f"{title} {summary}".lower()
    scores = {}

    for category, keywords in CATEGORY_RULES.items():
        scores[category] = sum(1 for keyword in keywords if keyword.lower() in text)

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return None

    return best_category


def make_agent_brief(article):
    category = article["category"]
    summary = article["summary"]

    return {
        "core_message": (
            f"이 항목은 '{category}' 관점에서 볼 필요가 있습니다. "
            "단순 AI 뉴스라기보다 AI Agent가 실제 업무 실행 구조로 확장되는 흐름과 연결됩니다."
        ),
        "technology_meaning": (
            summary[:700] + "..."
            if len(summary) > 700
            else summary
        ) or "RSS 요약문이 충분하지 않습니다. 원문 확인이 필요합니다.",
        "enterprise_impact": (
            "기업 적용 관점에서는 이 기술이 내부 시스템, 업무 데이터, 승인 절차, 실행 로그와 어떻게 연결되는지가 중요합니다. "
            "특히 Agent가 단순 조회를 넘어 실제 업무 액션을 수행하는 경우 권한 통제와 사람 승인 단계를 함께 설계해야 합니다."
        ),
        "risk": (
            "원문만 보고 바로 도입 판단을 내리기는 어렵습니다. 기능 범위, 보안 조건, 실패 처리 방식, 감사 로그 제공 여부를 별도로 확인해야 합니다."
        ),
        "action": (
            "기술 레이더에 등록한 뒤, 같은 주제의 벤더 발표나 오픈소스 변화와 묶어서 PoC 후보인지 관찰 대상으로 둘지 판단하는 것이 좋습니다."
        ),
    }


@st.cache_data(ttl=86400, show_spinner=False)
def load_articles():
    collected_at = now_kst_text()
    articles = []

    for source_name, rss_url in RSS_SOURCES:
        feed = feedparser.parse(rss_url)

        for entry in feed.entries[:8]:
            title = clean_text(entry.get("title", ""))
            summary = clean_text(entry.get("summary", ""))
            url = entry.get("link", "")
            published_at = entry.get("published", "발행일 확인 필요")

            if not title or not url:
                continue

            category = classify_article(title, summary)

            if category is None:
                continue

            article = {
                "title": title,
                "source": source_name,
                "url": url,
                "published_at": published_at,
                "collected_at": collected_at,
                "summary": summary,
                "category": category,
            }

            article.update(make_agent_brief(article))
            articles.append(article)

    return articles, collected_at


def contains_keyword(article, keyword):
    if not keyword:
        return True

    keyword = keyword.lower()

    text = " ".join([
        article.get("title", ""),
        article.get("source", ""),
        article.get("category", ""),
        article.get("summary", ""),
        article.get("core_message", ""),
        article.get("technology_meaning", ""),
        article.get("enterprise_impact", ""),
        article.get("risk", ""),
        article.get("action", ""),
    ]).lower()

    return keyword in text


def render_summary(articles):
    st.markdown("#### Executive Summary")

    st.write(
        "이 화면은 OpenAI, Anthropic, LangChain, Microsoft, AWS 등 주요 기술 소스의 RSS를 하루 1회 수집하고, "
        "AI Agent 관점에서 기술 테마를 분류해 보여주는 브리핑입니다."
    )

    st.write(
        "핵심은 기사 개수가 아니라 Agent 기술의 어느 레이어에서 변화가 발생하는지입니다. "
        "오케스트레이션, 도구 호출, 메모리, 평가, 기업 아키텍처, 브라우저 실행 Agent 영역을 중심으로 확인하면 됩니다."
    )

    if not articles:
        st.info("현재 수집된 AI Agent 관련 항목이 없습니다. 사이드바의 갱신 버튼을 눌러보세요.")
        return

    category_map = {}

    for article in articles:
        category_map.setdefault(article["category"], []).append(article)

    st.markdown("#### 기술 테마별 관찰")

    for category, items in category_map.items():
        with st.container(border=True):
            st.markdown(f"##### {category}")
            st.write(
                "이 영역은 최근 수집 항목에서 확인된 Agent 기술 테마입니다. "
                "원문을 그대로 읽기보다, 내부 업무 자동화와 연결했을 때 어떤 통제 구조가 필요한지 함께 검토하는 것이 좋습니다."
            )

            for item in items[:3]:
                st.write(f"• {item['title']}")


def render_article_card(article):
    with st.container(border=True):
        st.caption(
            f"{article['category']} · {article['source']} · 발행: {article['published_at']} · 수집: {article['collected_at']}"
        )

        st.markdown(f"### {article['title']}")

        with st.expander("상세 내용 보기", expanded=True):
            st.markdown("##### 핵심 메시지")
            st.write(article["core_message"])

            st.markdown("##### 기술적 의미")
            st.write(article["technology_meaning"])

            st.markdown("##### 기업 적용 시사점")
            st.write(article["enterprise_impact"])

            st.markdown("##### 리스크 및 확인사항")
            st.write(article["risk"])

            st.markdown("##### 권장 액션")
            st.info(article["action"])

        st.link_button("원문 보기", article["url"], use_container_width=True)


articles, collected_at = load_articles()

categories = sorted({article["category"] for article in articles})
sources = sorted({article["source"] for article in articles})

with st.sidebar:
    st.markdown("### 검색 및 필터")

    query = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, Agent, RAG, Evaluation"
    )

    selected_categories = st.multiselect(
        "기술 분류",
        options=categories,
        default=categories
    )

    selected_sources = st.multiselect(
        "출처",
        options=sources,
        default=sources
    )

    st.divider()

    st.caption("갱신 주기: 24시간")

    if st.button("오늘 기준으로 다시 수집", use_container_width=True):
        st.cache_data.clear()
        st.rerun()


filtered_articles = []

for article in articles:
    category_ok = not selected_categories or article["category"] in selected_categories
    source_ok = not selected_sources or article["source"] in selected_sources
    keyword_ok = contains_keyword(article, query)

    if category_ok and source_ok and keyword_ok:
        filtered_articles.append(article)


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 수집: {collected_at} KST | 갱신 주기: 24시간")
st.write(
    "AI Agent 관련 최신 원문을 수집한 뒤, 뉴스 목록이 아니라 기술 구조와 기업 적용 관점으로 재구성한 브리핑입니다."
)

st.divider()

summary_tab, report_tab, data_tab = st.tabs(["핵심요약", "상세리포트", "수집 데이터"])

with summary_tab:
    render_summary(filtered_articles)

with report_tab:
    st.markdown("#### 상세리포트")

    if not filtered_articles:
        st.info("현재 조건에 맞는 항목이 없습니다. 검색어 또는 필터를 조정해보세요.")
    else:
        for article in filtered_articles:
            render_article_card(article)

with data_tab:
    st.markdown("#### 수집 데이터 원본")

    if not filtered_articles:
        st.info("표시할 데이터가 없습니다.")
    else:
        df = pd.DataFrame(filtered_articles)
        st.dataframe(
            df[["title", "category", "source", "published_at", "collected_at", "url"]],
            hide_index=True,
            use_container_width=True
        )
