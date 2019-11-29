from pathlib import Path
from aiogram.types import ParseMode

project_root_dir = Path(__file__).parent.parent
DEFAULT_PROXY = "socks5://127.0.0.1:9050"  # Using tor socks-proxy against censorship
DATABASE_NAME = "protobot_base.db"
PROJECT_NAME = "ProtoBot"
DEFAULT_PARSE_MODE = ParseMode.HTML  # Currently decided to use HTML as more stable parse mode
