from os.path import isfile
from src.common.constants import C_DEFAULT_YAML_CONFIG
from yaml import safe_load

class UserSettings:
    m_color_allowed = True
    m_stop_key_enabled = True
    m_sleep_duration = 10
    m_left_mouse = 'ä'
    m_toggle_key = 'F12'
    m_stop_key = 'escape'
    
def update_user_settings():
    if not isfile('./settings.yml'):
        with open('./settings.yml',encoding='utf-8', mode= 'x') as f:
            f.write(C_DEFAULT_YAML_CONFIG)
    with open('./settings.yml',encoding='utf-8', mode = 'r') as f:
        g_settings = safe_load(f)
        for t_setting in g_settings:
            setattr(UserSettings, t_setting, g_settings[t_setting])