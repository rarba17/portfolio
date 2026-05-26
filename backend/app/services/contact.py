import smtplib
from email.message import EmailMessage

from fastapi import Request

from ..core.config import settings


def client_ip(request: Request) -> str:
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def send_contact_email(name: str, email: str, message: str) -> None:
    if not settings.smtp_user or not settings.smtp_password or not settings.contact_to_email:
        # Local/dev fallback: accept request when SMTP is not configured.
        return

    msg = EmailMessage()
    msg["Subject"] = f"Portfolio contact from {name}"
    msg["From"] = settings.contact_from_email or settings.smtp_user
    msg["To"] = settings.contact_to_email
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=20) as smtp:
        smtp.starttls()
        smtp.login(settings.smtp_user, settings.smtp_password)
        smtp.send_message(msg)
