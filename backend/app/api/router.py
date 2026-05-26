import mimetypes

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse

from ..core.config import FRONTEND_DIST_DIR, RESUME_FILE
from ..data.content import ARTICLES, PROJECTS
from ..models.schemas import Article, Project
from ..services.contact import client_ip, send_contact_email
from ..services.rate_limit import check_contact_rate_limit

api_router = APIRouter(prefix="/api")
web_router = APIRouter()


@api_router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@api_router.get("/projects", response_model=list[Project])
def get_projects() -> list[Project]:
    return PROJECTS


@api_router.get("/articles", response_model=list[Article])
def get_articles() -> list[Article]:
    return ARTICLES


@api_router.post("/contact")
def submit_contact(
    request: Request,
    name: str = Form(..., min_length=2, max_length=80),
    email: str = Form(..., min_length=5, max_length=120),
    message: str = Form(..., min_length=10, max_length=2500),
) -> JSONResponse:
    check_contact_rate_limit(client_ip(request))
    try:
        send_contact_email(name=name, email=email, message=message)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {exc}") from exc
    return JSONResponse({"status": "ok", "message": "Message received."})


@api_router.get("/resume")
def download_resume() -> FileResponse:
    if not RESUME_FILE.exists():
        raise HTTPException(status_code=404, detail="Resume not found.")
    return FileResponse(
        path=RESUME_FILE,
        media_type="application/pdf",
        filename="resume.pdf",
    )


if FRONTEND_DIST_DIR.exists():
    @web_router.get("/")
    def serve_index() -> FileResponse:
        return FileResponse(FRONTEND_DIST_DIR / "index.html")


    @web_router.get("/{full_path:path}")
    def serve_spa(full_path: str) -> FileResponse:
        if full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="Not found")
        candidate = FRONTEND_DIST_DIR / full_path
        if candidate.exists() and candidate.is_file():
            media_type, _ = mimetypes.guess_type(str(candidate))
            return FileResponse(candidate, media_type=media_type)
        return FileResponse(FRONTEND_DIST_DIR / "index.html")
