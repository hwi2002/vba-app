import re
from datetime import datetime, timedelta, timezone

import feedparser
import streamlit as st


KST = timezone(timedelta(hours=9))
WEEKLY_CACHE_SECONDS = 604800


st.set_page_config(
    page_title="AI Agent 기술 트렌드",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


RSS_SOURCES = [
    {"name": "OpenAI", "url": "https://openai.com/news/rss.xml"},
    {"name": "Anthropic", "url": "https://www.anthropic.com/news/rss.xml"},
    {"name": "LangChain", "url": "https://blog.langchain.com/rss/"},
    {"name": "Microsoft AI", "url": "https://blogs.microsoft.com/ai/feed/"},
    {"name": "AWS Machine Learning", "url": "https://aws.amazon.com/blogs/machine-learning/feed/"},
]


TREND_SECTIONS = {
    "Loop Engineering": {
        "keywords": [
            "loop", "feedback loop", "reflection", "self-correction", "iteration",
            "retry", "critic", "review", "human feedback", "closed loop",
        ],
        "summary": "Loop Engineering은 Agent가 실행 결과를 평가하고 다시 계획을 조정하는 반복 구조를 설계하는 영역입니다.",
        "changes": [
            "Agent가 한 번의 응답으로 끝나는 구조에서 벗어나 계획, 실행, 평가, 수정의 반복 루프를 갖추는 방향으로 발전하고 있습니다.",
            "Reflection, Critic, Reviewer 역할을 별도로 두어 중간 결과를 검토하고 실패 시 재시도하거나 다른 도구를 선택하는 패턴이 늘고 있습니다.",
            "사람 피드백을 루프 안에 넣어 자동화 수준을 단계적으로 높이고, 고위험 업무에서는 승인 기반 루프를 유지하는 설계가 중요해지고 있습니다.",
            "루프별 품질 기준과 실패 원인을 기록해 다음 실행에서 더 나은 판단을 하도록 만드는 운영 설계가 중요해지고 있습니다.",
            "비용과 지연 시간을 관리하기 위해 무한 반복을 막고, 루프 깊이와 재시도 전략을 업무 위험도에 맞게 조정하는 흐름이 강화되고 있습니다.",
        ],
        "meaning": "기술적으로는 Agent 품질을 모델 성능 하나에 맡기기보다, 실행 후 검증하고 다시 보정하는 운영 구조로 끌어올린다는 의미입니다.",
        "architecture": "아키텍처 관점에서는 Plan, Execute, Evaluate, Revise, Escalate 단계를 명확히 분리해야 합니다. 각 루프에는 종료 조건, 재시도 한도, 실패 분류, 사람 개입 조건이 필요합니다.",
        "enterprise": "기업 업무에서는 보고서 초안 작성, 코드 리뷰, 심사 보조, 고객 응대처럼 결과 검토가 필요한 업무에 적합합니다. 사람이 최종 책임을 갖되 반복 검토를 Agent가 보조하는 구조가 현실적입니다.",
        "risk": "루프의 종료 조건이 없으면 불필요한 재시도와 비용 증가가 발생하고, 잘못된 평가 기준이 들어가면 오류를 더 강화할 수 있습니다.",
        "action": "초기에는 최대 반복 횟수, 품질 기준, 사람 승인 조건을 먼저 정의하고 작은 업무 단위에서 루프 품질을 측정하는 것이 좋습니다.",
        "checklist": [
            "각 루프 단계의 입력, 출력, 책임을 분리했는가",
            "재시도 한도와 종료 조건이 명확한가",
            "사람 검토가 필요한 위험 구간을 정의했는가",
            "실패 사유가 로그로 남고 다음 실행에 반영되는가",
        ],
        "maturity": "성숙도는 단순 재시도, 기준 기반 검토, 사람 피드백 반영, 자동 개선 루프 순서로 높아집니다.",
    },
    "LoopCraft": {
        "keywords": [
            "loopcraft", "loop craft", "prompt loop", "agent loop", "workflow design",
            "iteration design", "task loop", "quality loop", "review loop",
        ],
        "summary": "LoopCraft는 반복형 Agent 워크플로우를 업무 목적에 맞게 조립하고 운영 가능한 형태로 다듬는 실무 설계 관점입니다.",
        "changes": [
            "Agent 워크플로우는 단순 자동화 흐름보다 업무별 반복 패턴을 세밀하게 조립하는 방향으로 고도화되고 있습니다.",
            "자료 수집, 초안 작성, 검토, 보완, 승인처럼 반복이 필요한 업무에서 루프 단위를 재사용 가능한 템플릿으로 만드는 접근이 중요해지고 있습니다.",
            "프롬프트, 도구, 검증 기준, 사람 승인 지점을 함께 설계해야 실제 운영에서 안정적인 결과를 만들 수 있습니다.",
            "업무별 Loop Template을 축적해 반복 업무를 빠르게 설계하고, 조직 내 공통 운영 패턴으로 재사용하려는 흐름이 나타나고 있습니다.",
            "템플릿 변경 이력과 성과 지표를 함께 관리해 어떤 루프 설계가 실제 업무 품질을 높였는지 추적하는 방식이 중요해지고 있습니다.",
        ],
        "meaning": "기술적으로는 Agent 루프를 즉흥적으로 연결하는 것이 아니라, 업무 목적과 품질 기준에 맞게 설계 자산으로 관리한다는 의미입니다.",
        "architecture": "아키텍처 관점에서는 Loop Template, Role Prompt, Tool Policy, Quality Gate, Approval Step을 한 묶음으로 관리하는 구조가 필요합니다. 같은 루프를 여러 업무에 재사용하려면 입력 스키마와 산출물 형식도 표준화해야 합니다.",
        "enterprise": "기업에서는 반복 보고, 시장 조사, 제안서 작성, 내부 검토 프로세스처럼 비슷한 절차가 반복되는 지식 업무에 적용하기 좋습니다.",
        "risk": "업무 맥락을 반영하지 않은 범용 루프는 그럴듯한 산출물을 만들 수 있지만, 실제 의사결정 기준이나 승인 기준과 어긋날 수 있습니다.",
        "action": "자주 반복되는 업무를 골라 Loop Template으로 정의하고, 산출물 기준과 승인 조건을 함께 문서화하는 것이 좋습니다.",
        "checklist": [
            "업무별 반복 패턴을 템플릿으로 분리했는가",
            "프롬프트, 도구, 검증 기준을 하나의 운영 단위로 관리하는가",
            "산출물 형식과 승인 기준이 표준화되어 있는가",
            "템플릿 변경 이력과 성과 지표를 추적하는가",
        ],
        "maturity": "성숙도는 개별 루프 작성, 템플릿화, 업무별 재사용, 성과 기반 개선 순서로 높아집니다.",
    },
    "Agent Orchestration": {
        "keywords": [
            "agent", "agents", "multi-agent", "workflow", "orchestration",
            "langgraph", "autogen", "crewai", "planner", "executor", "deep agents",
        ],
        "summary": "AI Agent는 단일 챗봇 구조에서 벗어나 여러 역할을 가진 에이전트가 협업하는 구조로 이동하고 있습니다.",
        "changes": [
            "단순 프롬프트 체이닝 중심의 구조에서 벗어나 상태와 단계를 관리하는 워크플로우 기반 Agent 설계가 증가하고 있습니다.",
            "Planner, Executor, Evaluator처럼 역할을 분리하고, 각 Agent가 맡은 책임을 명확히 정의하는 구조가 중요해지고 있습니다.",
            "복잡한 업무를 한 번에 처리하기보다 계획, 실행, 검증, 재시도, 종료 조건을 분리해 안정적으로 운영하는 방향으로 발전하고 있습니다.",
        ],
        "meaning": "기술적으로는 Agent가 단순히 답변을 생성하는 수준을 넘어, 업무 단계를 이해하고 다음 행동을 선택하는 실행 구조로 발전하고 있다는 의미입니다.",
        "architecture": "아키텍처 관점에서는 Agent를 하나의 거대한 블랙박스로 두기보다, 계획 수립, 실행, 검증, 재시도, 종료 조건을 명확히 분리해야 합니다. 장기 실행 업무에서는 중간 상태 저장과 실패 시 재개 구조가 특히 중요합니다.",
        "enterprise": "기업 업무에서는 보고서 작성, 심사 보조, 고객 응대, 장애 처리처럼 여러 단계가 있는 업무에 적용 가능성이 큽니다. 다만 각 단계의 책임과 승인 기준을 명확히 해야 합니다.",
        "risk": "상태 전이 조건이 불명확하면 Agent가 같은 작업을 반복하거나, 잘못된 판단을 기준으로 다음 업무를 계속 진행할 수 있습니다.",
        "action": "초기 PoC에서는 업무를 5~7개 단계로 나누고, 각 단계별 입력값, 출력값, 검증 기준, 실패 처리 방식을 먼저 정의하는 것이 좋습니다.",
    },
    "MCP & Tool Calling": {
        "keywords": [
            "mcp", "model context protocol", "tool", "tools", "function calling",
            "api", "connector", "integration", "server", "tool use",
        ],
        "summary": "AI Agent의 실무 가치는 외부 시스템과 도구를 얼마나 안전하게 연결하느냐에 따라 결정되고 있습니다.",
        "changes": [
            "Agent가 외부 API, 데이터베이스, 업무 시스템을 호출하는 구조가 확대되면서 Tool Calling 설계가 핵심 요소로 부상하고 있습니다.",
            "MCP와 같은 표준화 흐름은 Agent와 외부 도구를 연결하는 방식을 일관되게 만들고, 시스템 연동 비용을 줄이는 방향으로 작용하고 있습니다.",
            "단순히 도구를 많이 연결하는 것보다 도구별 입력값, 반환값, 권한 범위, 실패 응답을 명확히 정의하는 방식이 중요해지고 있습니다.",
        ],
        "meaning": "기술적으로는 Agent가 단순 대화 인터페이스가 아니라 외부 시스템을 호출하는 실행 주체로 바뀌고 있다는 뜻입니다.",
        "architecture": "아키텍처 관점에서는 Tool Registry, Schema Validation, Permission Check, Execution Log가 핵심입니다. Agent가 어떤 도구를 왜 호출했는지 남겨야 하며, 잘못된 입력값은 실행 전에 차단할 수 있어야 합니다.",
        "enterprise": "기업에서는 조회형 도구와 변경형 도구를 반드시 구분해야 합니다. 고객 정보 조회와 데이터 수정, 승인, 외부 발송은 위험 수준이 다르기 때문입니다.",
        "risk": "도구 호출 권한을 넓게 열어두면 모델의 오판이 실제 데이터 변경이나 외부 발송으로 이어질 수 있습니다.",
        "action": "Tool 목록을 조회형, 생성형, 변경형, 외부발송형으로 나누고 변경형 이상에는 사람 승인 단계를 두는 것이 적합합니다.",
    },
    "Memory & State Management": {
        "keywords": [
            "memory", "state", "context", "rag", "retrieval", "vector",
            "knowledge graph", "long-term", "context engineering",
        ],
        "summary": "AI Agent의 메모리는 단순 대화 기억이 아니라 업무 상태를 유지하는 구조로 확장되고 있습니다.",
        "changes": [
            "단기 대화 이력 저장을 넘어 현재 업무가 어느 단계까지 진행됐는지 관리하는 Task State의 중요성이 커지고 있습니다.",
            "Vector DB, RDB, Graph DB를 목적별로 조합해 대화, 지식, 업무 상태, 실행 로그를 분리 관리하려는 흐름이 나타나고 있습니다.",
            "장기 업무 처리형 Agent에서는 이전 판단 근거와 실행 이력을 함께 남겨야 후속 검증과 감사가 가능해집니다.",
        ],
        "meaning": "기술적으로는 Agent가 매번 처음부터 답변하는 구조가 아니라, 이전 단계의 판단과 실행 상태를 이어받아 업무를 지속하는 구조로 발전하고 있습니다.",
        "architecture": "아키텍처 관점에서는 Conversation Memory, Business State, Reference Knowledge, Execution Log를 분리하는 것이 좋습니다. 대화 내용과 업무 상태를 섞어 저장하면 검색 정확도와 감사 가능성이 떨어집니다.",
        "enterprise": "제안서 작성, 심사 보조, 고객 상담, 장애 처리처럼 여러 번의 대화와 문서 검토가 이어지는 업무에서는 메모리 구조가 품질을 좌우합니다.",
        "risk": "잘못된 메모리가 누적되면 오래된 정보나 잘못된 사용자 의도를 기준으로 판단할 수 있습니다.",
        "action": "Conversation Memory, Business State, Reference Knowledge, Execution Log를 분리해서 설계하는 것이 좋습니다.",
    },
    "Agent Evaluation & AgentOps": {
        "keywords": [
            "eval", "evals", "evaluation", "benchmark", "monitoring",
            "observability", "trace", "tracing", "safety", "guardrail", "langsmith",
        ],
        "summary": "AI Agent 평가는 정답률보다 실행 과정의 품질과 실패 통제가 더 중요해지고 있습니다.",
        "changes": [
            "Agent는 여러 단계를 수행하기 때문에 최종 답변의 정답 여부뿐 아니라 계획, 도구 호출, 중간 검증, 재시도 과정까지 평가해야 합니다.",
            "Golden Dataset과 루브릭 기반 평가를 통해 업무별 성공 기준을 명확히 하고, 반복 개선 가능한 구조를 만드는 흐름이 강화되고 있습니다.",
            "운영 단계에서는 Trace Log와 실행 이력을 남겨 실패 원인이 모델, 데이터, 도구, 프로세스 중 어디에 있는지 추적하는 것이 중요해지고 있습니다.",
        ],
        "meaning": "기술적으로는 Agent가 결과만 내는 시스템이 아니라 여러 단계를 수행하는 시스템이기 때문에, 평가도 과정 중심으로 바뀌어야 한다는 의미입니다.",
        "architecture": "아키텍처 관점에서는 Trace Log, Step Evaluation, Golden Task Set, Human Review Queue, Failure Taxonomy가 필요합니다. 각 실행 단계별 입력, 판단, 도구 호출, 출력, 오류를 남겨야 개선 포인트를 찾을 수 있습니다.",
        "enterprise": "기업 운영에서는 사용자가 틀렸다고 느끼는 결과보다, 왜 틀렸는지 추적할 수 없는 구조가 더 큰 문제입니다. 실행 로그와 평가 체계가 없으면 개선이 어렵습니다.",
        "risk": "평가 체계 없이 운영하면 모델 문제인지, 데이터 문제인지, 도구 호출 문제인지, 업무 프로세스 문제인지 구분할 수 없습니다.",
        "action": "초기부터 업무별 골든셋과 루브릭을 만들고, 실행 성공률, 단계 누락률, 도구 호출 오류율, 사용자 개입률을 함께 관리하는 것이 좋습니다.",
    },
    "Enterprise Agent Architecture": {
        "keywords": [
            "enterprise", "business", "automation", "crm", "erp", "operation",
            "productivity", "salesforce", "workflow automation", "back office",
        ],
        "summary": "기업형 AI Agent는 자동화 도구라기보다 통제 가능한 업무 위임 구조로 설계해야 합니다.",
        "changes": [
            "기업형 Agent는 문서 검색과 요약을 넘어 ERP, CRM, 그룹웨어, 데이터베이스와 연결되는 업무 실행 계층으로 확장되고 있습니다.",
            "조회, 추천, 생성, 실행을 구분하고 각 단계마다 권한과 승인 조건을 다르게 두는 설계가 중요해지고 있습니다.",
            "Agent가 실제 업무 시스템에 접근하는 순간부터 보안, 감사 로그, 사용자 승인, 롤백 절차가 핵심 설계 요소가 됩니다.",
        ],
        "meaning": "기술적으로는 Agent가 단순 정보 제공자가 아니라 실제 업무 시스템과 연결되는 업무 실행 계층으로 이동하고 있다는 뜻입니다.",
        "architecture": "아키텍처 관점에서는 User Role, Data Permission, Action Boundary, Approval Gate, Audit Log가 기본 요소입니다. 특히 조회와 변경 액션을 분리하고, 변경 액션에는 사전 확인과 사후 로그를 남겨야 합니다.",
        "enterprise": "기업에서는 모든 업무를 완전 자동화하기보다, 사람이 검토해야 할 부분과 Agent에게 위임할 수 있는 부분을 나누는 방식이 현실적입니다.",
        "risk": "업무 책임이 불명확한 상태에서 Agent를 도입하면 현업은 결과를 신뢰하지 못하고 IT는 장애 원인을 추적하기 어렵습니다.",
        "action": "조회 업무부터 시작해 추천, 초안 생성, 승인 기반 실행 순서로 점진적으로 확장하는 방식이 적합합니다.",
    },
    "Computer Use & Browser Agent": {
        "keywords": [
            "computer use", "browser", "web", "desktop", "screen", "click",
            "operator", "rpa", "ui automation",
        ],
        "summary": "웹·OS 실행 Agent는 API가 없는 업무까지 자동화할 수 있지만, 보안과 통제 설계가 매우 중요합니다.",
        "changes": [
            "화면을 인식하고 클릭, 입력, 탐색을 수행하는 Agent 기술이 발전하면서 API가 없는 업무까지 자동화 범위가 확장되고 있습니다.",
            "기존 RPA가 고정된 화면 구조와 좌표에 취약했다면, Browser Agent는 화면 맥락을 해석해 보다 유연하게 대응할 가능성이 있습니다.",
            "다만 사람이 보는 화면을 그대로 조작할 수 있기 때문에 계정 권한, 허용 도메인, 실행 로그, 사람 확인 단계가 함께 설계되어야 합니다.",
        ],
        "meaning": "기술적으로는 Agent가 API 호출뿐 아니라 사람이 보는 화면을 직접 조작하는 방향으로 확장되고 있다는 의미입니다.",
        "architecture": "아키텍처 관점에서는 Screen Parser, Action Planner, Click Executor, Safety Guard, Human Confirmation이 필요합니다. 로그인, 결제, 삭제, 외부 전송 같은 고위험 액션은 반드시 차단하거나 사람 확인을 거쳐야 합니다.",
        "enterprise": "API가 없는 구형 웹 시스템, 반복 입력 업무, 관리자 페이지 조회, 외부 사이트 정보 수집에는 활용 가능성이 있습니다.",
        "risk": "화면 기반 Agent는 사용자의 계정 권한으로 움직일 수 있기 때문에 잘못된 클릭, 민감 정보 노출, 외부 전송 위험이 있습니다.",
        "action": "초기에는 읽기 전용 업무나 테스트 환경에서 시작하고, 허용 URL, 전용 계정, 실행 로그, 사람 확인 단계를 반드시 두는 것이 안전합니다.",
    },
}


def now_kst_text():
    return datetime.now(KST).strftime("%Y-%m-%d %H:%M")


def strip_html(value):
    text = str(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def match_categories(title, summary):
    text = f"{title} {summary}".lower()
    matched = []

    for category, config in TREND_SECTIONS.items():
        score = sum(1 for keyword in config["keywords"] if keyword.lower() in text)

        if score > 0:
            matched.append((category, score))

    matched.sort(key=lambda x: x[1], reverse=True)
    return [category for category, _ in matched[:2]]


@st.cache_data(ttl=WEEKLY_CACHE_SECONDS, show_spinner=False)
def collect_articles():
    collected_at = now_kst_text()
    articles_by_category = {category: [] for category in TREND_SECTIONS.keys()}
    raw_articles = []

    for source in RSS_SOURCES:
        try:
            feed = feedparser.parse(source["url"])
            entries = feed.entries[:12]
        except Exception:
            entries = []

        for entry in entries:
            title = strip_html(entry.get("title", ""))
            summary = strip_html(entry.get("summary", ""))
            url = entry.get("link", "")
            published_at = entry.get("published", "발행일 확인 필요")

            if not title or not url:
                continue

            matched_categories = match_categories(title, summary)

            article = {
                "title": title,
                "summary": summary,
                "source": source["name"],
                "url": url,
                "published_at": published_at,
                "collected_at": collected_at,
                "categories": matched_categories,
            }

            raw_articles.append(article)

            for category in matched_categories:
                if len(articles_by_category[category]) < 5:
                    articles_by_category[category].append(article)

    return articles_by_category, raw_articles, collected_at


def extract_dynamic_signal(category, articles):
    config = TREND_SECTIONS[category]

    if not articles:
        return {
            "article_count": 0,
            "sources": [],
            "keywords": [],
            "latest_titles": [],
        }

    source_counts = {}
    keyword_counts = {}

    for article in articles:
        source = article.get("source", "Unknown")
        source_counts[source] = source_counts.get(source, 0) + 1

        text = f"{article.get('title', '')} {article.get('summary', '')}".lower()

        for keyword in config["keywords"]:
            if keyword.lower() in text:
                keyword_counts[keyword] = keyword_counts.get(keyword, 0) + 1

    top_sources = sorted(source_counts, key=source_counts.get, reverse=True)[:3]
    top_keywords = sorted(keyword_counts, key=keyword_counts.get, reverse=True)[:5]
    latest_titles = [article["title"] for article in articles[:3]]

    return {
        "article_count": len(articles),
        "sources": top_sources,
        "keywords": top_keywords,
        "latest_titles": latest_titles,
    }


def make_dynamic_interpretation(category, signal):
    if signal["article_count"] == 0:
        return (
            "이번 수집 기준으로 직접 매칭된 원문은 많지 않습니다. "
            "다만 이 영역은 AI Agent 아키텍처의 핵심 구성요소이므로 지속 관찰이 필요합니다."
        )

    source_text = ", ".join(signal["sources"]) if signal["sources"] else "주요 기술 소스"
    keyword_text = ", ".join(signal["keywords"]) if signal["keywords"] else "관련 키워드"

    return (
        f"이번 수집 기준으로 {category} 영역에서 {signal['article_count']}건의 관련 원문이 확인되었습니다. "
        f"주요 출처는 {source_text}이며, 주요 키워드는 {keyword_text}입니다. "
        "단일 기사 하나의 의미보다, 같은 기술 주제가 여러 출처에서 반복적으로 등장하는지를 중심으로 보는 것이 좋습니다."
    )


def make_dynamic_action(category, signal):
    if signal["article_count"] == 0:
        return (
            "이번 수집 기준으로는 직접적인 원문 매칭이 적으므로, "
            "기존 아키텍처 검토 항목으로 유지하면서 후속 원문 증가 여부를 관찰하는 것이 적합합니다."
        )

    if signal["article_count"] >= 4:
        return (
            f"{category} 영역은 이번 수집 기준으로 관련 원문이 반복 확인됩니다. "
            "단순 관찰 대상이 아니라 PoC 후보 또는 내부 검토 과제로 올려볼 필요가 있습니다."
        )

    if signal["article_count"] >= 2:
        return (
            f"{category} 영역은 관련 원문이 일부 확인됩니다. "
            "추가 원문을 확인하면서 내부 업무 적용 가능성과 리스크 항목을 함께 정리하는 것이 좋습니다."
        )

    return (
        f"{category} 영역은 현재 1건 수준의 참고 원문이 확인되었습니다. "
        "기술 레이더에 등록하고, 같은 키워드가 반복 등장하는지 관찰하는 것이 적합합니다."
    )


def contains_keyword(category, keyword):
    if not keyword:
        return True

    keyword = keyword.lower()
    config = TREND_SECTIONS[category]

    searchable_text = " ".join(
        [
            category,
            config["summary"],
            config["meaning"],
            config["architecture"],
            config["enterprise"],
            config["risk"],
            config["action"],
            config.get("maturity", ""),
            " ".join(config["changes"]),
            " ".join(config.get("checklist", [])),
        ]
    ).lower()

    return keyword in searchable_text


def render_executive_summary(selected_categories, articles_by_category):
    st.markdown("#### Executive Summary")

    st.write(
        "AI Agent 기술은 단순 챗봇이나 뉴스성 AI 기능을 넘어, 업무 목표를 이해하고 도구를 호출하며 실행 결과를 검증하는 구조로 이동하고 있습니다. "
        "핵심 변화는 Loop Engineering, LoopCraft, Agent Orchestration, MCP & Tool Calling, Memory & State Management, Agent Evaluation, Enterprise Architecture, Computer Use 영역에서 동시에 나타나고 있습니다."
    )

    st.write(
        "기업 적용 관점에서는 모델 성능보다 통제 가능한 실행 구조가 중요합니다. "
        "즉, 어떤 도구를 호출할 수 있는지, 어떤 데이터에 접근할 수 있는지, 어느 단계에서 사람 승인이 필요한지, 실패했을 때 어떻게 중단하거나 복구할지를 먼저 정의해야 합니다."
    )

    st.markdown("#### 기술 테마별 요약")

    for category in selected_categories:
        config = TREND_SECTIONS[category]
        related_articles = articles_by_category.get(category, [])
        signal = extract_dynamic_signal(category, related_articles)

        with st.container(border=True):
            st.markdown(f"##### {category}")
            st.write(config["summary"])
            st.caption(f"최근 수집 원문: {signal['article_count']}건")

            if related_articles:
                st.caption("최근 수집 원문에서 관련 흐름이 확인된 영역입니다.")
            else:
                st.caption("현재 수집 원문에서는 직접 매칭된 항목이 적지만, Agent 아키텍처상 계속 관찰해야 할 영역입니다.")


def render_reference_articles(articles):
    if not articles:
        st.caption("이번 수집 기준으로 직접 매칭된 참고 원문은 없습니다.")
        return

    with st.expander("원문 링크 보기", expanded=False):
        for article in articles:
            st.markdown(f"**{article['title']}**")
            st.caption(f"{article['source']} · {article['published_at']}")
            st.link_button("원문 열기", article["url"])
            st.divider()


def render_trend_card(category, articles):
    config = TREND_SECTIONS[category]
    signal = extract_dynamic_signal(category, articles)

    with st.container(border=True):
        st.markdown(f"### {category}")

        st.write(config["summary"])

        st.markdown("##### 주요 변화")
        for change in config["changes"]:
            st.write(f"• {change}")

        st.markdown("##### 기술적 의미")
        st.write(config["meaning"])

        st.markdown("##### 관련 동향 및 참고 원문")
        st.write(f"• 최근 수집 원문: {signal['article_count']}건")

        if signal["sources"]:
            st.write(f"• 주요 출처: {', '.join(signal['sources'])}")

        if signal["keywords"]:
            st.write(f"• 주요 키워드: {', '.join(signal['keywords'])}")

        if signal["latest_titles"]:
            for title in signal["latest_titles"]:
                st.write(f"• {title}")

        st.markdown("##### 최근 동향 해석")
        st.write(make_dynamic_interpretation(category, signal))

        st.markdown("##### 아키텍처 관점")
        st.write(config["architecture"])

        st.markdown("##### 기업 적용 시사점")
        st.write(config["enterprise"])

        st.markdown("##### 리스크 및 확인사항")
        st.write(config["risk"])

        if config.get("checklist"):
            st.markdown("##### 적용 체크리스트")
            for item in config["checklist"]:
                st.write(f"• {item}")

        if config.get("maturity"):
            st.markdown("##### 성숙도 관점")
            st.write(config["maturity"])

        st.markdown("##### 권장 액션")
        st.info(make_dynamic_action(category, signal))

        render_reference_articles(articles)


def render_raw_articles(raw_articles):
    st.markdown("#### 수집 원문")

    if not raw_articles:
        st.info("현재 수집된 원문이 없습니다. 사이드바의 다시 수집 버튼을 눌러보세요.")
        return

    rows = []

    for article in raw_articles:
        rows.append(
            {
                "title": article["title"],
                "source": article["source"],
                "published_at": article["published_at"],
                "categories": ", ".join(article["categories"]) if article["categories"] else "미분류",
                "url": article["url"],
            }
        )

    st.dataframe(rows, hide_index=True, use_container_width=True)


articles_by_category, raw_articles, collected_at = collect_articles()

all_categories = list(TREND_SECTIONS.keys())

with st.sidebar:
    st.markdown("### 검색 및 필터")

    query = st.text_input(
        "키워드 검색",
        placeholder="예: MCP, 평가, 메모리, ERP, Browser",
    )

    selected_categories = st.multiselect(
        "기술 분류",
        options=all_categories,
        default=all_categories,
    )

    st.divider()

    st.caption("갱신 주기: Weekly")
    st.caption("RSS 원문은 참고자료로만 사용하고, 화면은 기술 브리핑 형식으로 재구성합니다.")

    if st.button("최신 트렌드 다시 수집", use_container_width=True):
        st.cache_data.clear()
        st.rerun()


if not selected_categories:
    selected_categories = all_categories

filtered_categories = [
    category for category in selected_categories if contains_keyword(category, query)
]


st.title("AI Agent 기술 트렌드")
st.caption(f"최근 수집: {collected_at} KST | Weekly AI Agent Technology Briefing")
st.write(
    "AI Agent 관련 최신 원문을 참고자료로 수집하되, 화면은 뉴스 목록이 아니라 아키텍처, 기업 적용, 운영 통제 관점의 기술 브리핑으로 재구성합니다."
)

st.divider()


summary_tab, report_tab, raw_tab = st.tabs(
    ["핵심요약", "상세리포트", "수집 원문"]
)


with summary_tab:
    render_executive_summary(filtered_categories, articles_by_category)


with report_tab:
    st.markdown("#### 상세리포트")

    if not filtered_categories:
        st.info("현재 검색 조건에 맞는 기술 트렌드가 없습니다.")
    else:
        for category in filtered_categories:
            render_trend_card(category, articles_by_category.get(category, []))


with raw_tab:
    render_raw_articles(raw_articles)
