from requests import get
from src.common.constants import C_VERSION
def get_version() -> str:
    try:
        return get('https://raw.githubusercontent.com/justusdecker/ANTI-AFK-SKRIPT/refs/heads/main/version.json').json().get('version')
    except Exception:
        return C_VERSION