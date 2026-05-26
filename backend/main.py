try:
    from app.main import app
except ModuleNotFoundError:
    # Allows `python -c "from backend.main import app"` from repository root.
    from backend.app.main import app
