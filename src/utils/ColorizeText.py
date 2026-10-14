from src.common.settings import UserSettings

def colorize_text(p_color: str, p_text: str):
    if UserSettings.m_color_allowed:
        return f'{p_color}{p_text}\033[0m'
    else:
        return p_text