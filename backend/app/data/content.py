from ..models.schemas import Article, Project

PROJECTS: list[Project] = [
    Project(
        id=1,
        title="Enterprise-Rag",
        role="Lead Full-Stack Engineer",
        stack=["StreamLit", "FastAPI", "PostgreSQL", "PGVector", "LangChain", "OpenAI", "Celery-Workers", "Redis", "LLM"],
        description="A production-grade backend system for document-powered Q&A. Organizations upload PDFs, which are automatically processed into vector embeddings; users then ask natural-language questions and get LLM answers grounded strictly in their documents — no hallucination, just precise retrieval.",
        live_url="https://example.com/enterprise-rag",
        github_url="https://github.com/rarba17/enterprise-Rag",
        mood="mustard",
    ),
    Project(
        id=2,
        title="AI Onboarding Agent",
        role="Lead Full-Stack Engineer",
        stack=["StreamLit", "FastAPI", "WebSockets", "Redis", "LangGraph", "OpenAI", "Event Queues", "PostgreSQL","LLM"],
        description="An intelligent multi-agent system that monitors new user behavior, diagnoses stuck points in real-time, and delivers personalized nudges to guide users to their Aha! moment.",
        live_url="https://example.com/ai-onboarding-agent",
        github_url="https://github.com/rarba17/AI-Onboarding-Agent-for-SaaS-Products",
        mood="plum",
    ),
    Project(
        id=3,
        title="Financial-Analyst-Agent",
        role="Frontend Architect",
        stack=["StreamLit", "FastAPI", "PostgreSQL", "LangChain", "OpenAI", "LangSmith","LLM","Redis","Memory"],
        description="An agentic AI backend that acts as a real-time financial analyst for CCPL (a major FMCG consumer products company). Business users can ask natural-language questions about P&L data and receive analyst-quality insights — no SQL or data science knowledge required.",
        live_url="https://example.com/cargo-quilt",
        github_url="https://github.com/rarba17/Cargo-Quilt",
        mood="rust",
    ),
    Project(
        id=4,
        title="Artifact Room",
        role="Full-Stack Engineer",
        stack=["React", "Python", "OpenSearch", "Docker"],
        description="Converted fragmented audit data into searchable timelines for security teams, making compliance evidence retrieval near-instant.",
        live_url="https://example.com/artifact-room",
        github_url="https://github.com/yourname/artifact-room",
        mood="slate",
    ),
]

ARTICLES: list[Article] = [
    Article(
        id=1,
        title="Designing APIs People Actually Read",
        summary="A practical pattern language for naming, pagination, and error payloads in internal platforms.",
        url="https://example.com/articles/api-patterns",
        published_at="2026-01-08",
    ),
    Article(
        id=2,
        title="Shipping Motion Without Nausea",
        summary="How to build expressive micro-animations that communicate structure instead of decoration.",
        url="https://example.com/articles/motion-with-intent",
        published_at="2025-10-21",
    ),
]
