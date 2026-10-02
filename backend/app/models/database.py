from __future__ import annotations

import os
from pathlib import Path


class DatabaseManager:
    def __init__(self) -> None:
        database_url = os.getenv("DATABASE_URL", "sqlite:///./retail_quality.db")
        self.database_url = database_url
        self.local_path = Path("./retail_quality.db")

    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")

    def get_connection_string(self) -> str:
        return self.database_url
