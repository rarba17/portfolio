import time
from collections import defaultdict, deque

from fastapi import HTTPException

from ..core.config import settings

_contact_events: dict[str, deque[float]] = defaultdict(deque)


def check_contact_rate_limit(ip: str) -> None:
    now = time.time()
    window = settings.contact_rate_window_seconds
    max_requests = settings.contact_rate_limit

    events = _contact_events[ip]
    while events and now - events[0] > window:
        events.popleft()
    if len(events) >= max_requests:
        raise HTTPException(status_code=429, detail="Too many contact attempts. Please try again later.")
    events.append(now)
