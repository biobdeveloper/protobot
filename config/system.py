from pathlib import Path
from aiogram.types import ParseMode

project_root_dir = Path(__file__).parent.parent
DEFAULT_PROXY = "socks5://127.0.0.1:9050"  # Using tor socks-proxy against censorship

DATABASE_NAME = 'protobot_db'

# Change sql engine to any from _CONN_URLS
SQL = "sqlite"

PG_USER = "protobot_user"
PG_PASS = "protobot_pass"
PG_HOST = "127.0.0.1"
PG_PORT = 5432

_CONN_URLS = {
    'sqlite': f"sqlite:///{str(project_root_dir)}/{DATABASE_NAME}.db",
    'pg':  f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{DATABASE_NAME}"
}


CONN_URL = _CONN_URLS[SQL]
PROJECT_NAME = "ProtoBot"

DEFAULT_PARSE_MODE = ParseMode.HTML  # Currently decided to use HTML as more stable parse mode
