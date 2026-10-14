import keyboard
from win32api import Beep
from random import random, randint
from time import sleep, time 
from threading import Thread
from src.service.GetVersion import get_version
from src.common.constants import C_DEFAULT_YAML_CONFIG, C_LONG_BEEP_DURATION, C_SHORT_BEEP_DURATION, C_VERSION
from src.utils.ColorizeText import colorize_text
from src.common.settings import UserSettings
import flet as ft
import os
import asyncio
C_COLOR_HIGHLIGHT = ft.Colors.AMBER
C_COLOR_HEADER = ft.Colors.PINK
C_COLOR_WARNING = ft.Colors.YELLOW

class AntiAFKTool:
    m_is_alive = True
    m_is_running = False
    m_thread_alive = False

    m_not_running_sleep_duration = 0.2
    
    m_pressed_keys = set()
    m_new_header = ft.Column([
        ft.Text("ANTI AFK Script ©2025 - 2026 Justus Decker. All rights reserved.", color=C_COLOR_HEADER),
        ft.Row([
            ft.Text('Press \''),
            ft.Text(UserSettings.m_toggle_key.upper(), color=C_COLOR_WARNING),
            ft.Text('\' to toggle on/off the ANTI AFK SCRIPT')
        ]),
        ft.Row([
            ft.Text('Repetitive \''),
            ft.Text(UserSettings.m_left_mouse.upper(), color=C_COLOR_WARNING),
            ft.Text('\' presses for simulating the \''),
            ft.Text('LEFT CLICK', color=C_COLOR_WARNING),
            ft.Text('\'')
        ]),
        ft.Row([
            ft.Text('Time-Interval (each \''),
            ft.Text(str(UserSettings.m_sleep_duration) + 's', color=C_COLOR_WARNING),
            ft.Text('\' to \''),
            ft.Text(f'{UserSettings.m_sleep_duration + 6}s', color=C_COLOR_WARNING),
            ft.Text('\')['),
            ft.Text('random time to avoid AntiCheat-Problems', color=C_COLOR_WARNING),
            ft.Text(']'),
        ]),
        ft.Row([
            ft.Text('Press \''),
            ft.Text(UserSettings.m_stop_key.upper(), color=C_COLOR_WARNING),
            ft.Text('\' to stop the ANTI AFK Script \'['),
            ft.Text('This is for safety reasons', color=C_COLOR_WARNING),
            ft.Text(']')
        ]),
    ], spacing= 1)

    def __init__(self):
        pass

    def press(self, p_key: str):
        self.m_pressed_keys.add(p_key)
        keyboard.press(p_key)
    
    def release(self, p_key: str): 
        try:
            self.m_pressed_keys.remove(p_key)
        except:
            ...
        keyboard.release(p_key)
    
    def release_all(self): 
        for t_key in self.m_pressed_keys.copy():
            self.release(t_key)
    
    
    def toggle(self, *_):

        self.m_is_running = not self.m_is_running
        print(f"The Script is now {colorize_text('\033[32m', 'ON') if self.m_is_running else colorize_text('\033[31m', 'OFF')}")
        if self.m_is_running:
            self.beep_thread_starter(C_LONG_BEEP_DURATION)
        else:
            self.release_all()
            self.beep_thread_starter(C_SHORT_BEEP_DURATION)
    
    def stop(self, *_):
        if not self.m_is_running: return
        print(f"Escape detected - The Script is now {colorize_text('\033[31m', 'OFF')}")
        self.release_all()
        self.beep_thread_starter(C_SHORT_BEEP_DURATION)
        self.m_is_running = False
            
    
    def press_and_release(self, p_key: str, p_duration: float):
        self.press(p_key)
        sleep(p_duration)
        self.release(p_key)
    
    def play_beep(self, p_frequency: int):
        try:
            for i in range(3):
                Beep(p_frequency,200)
        except: ...
        self.m_thread_alive = False
    
    def beep_thread_starter(self, p_frequency: int):
        if self.m_thread_alive: return
        self.m_thread_alive = True
        Thread(target=self.play_beep, args=[p_frequency]).start()
    
    def get_enabled_disabled(self, val: bool) -> str:
        return [colorize_text('\033[31m','disabled'), colorize_text('\033[32m','enabled')][val]
    
    def add_keyboard_listeners(self):
        keyboard.on_press_key(UserSettings.m_toggle_key,self.toggle)
        keyboard.on_press_key(UserSettings.m_stop_key,self.stop)
    
    def run(self):
        while self.m_is_alive:
            if not self.m_is_running:
                sleep(self.m_not_running_sleep_duration)
                continue
            self.press_and_release(UserSettings.m_left_mouse, 10 + randint(1, 5) + random())
            t_random_duration = random()
            sleep(t_random_duration if t_random_duration > 0.4 else t_random_duration + 0.4)

def main(p_page: ft.Page):
    LC_TITLE = 'ANTI AFK Tool ©2025 - 2026 Justus Decker. All rights reserved.'
    p_page.title = f"(OFF) " + LC_TITLE
    p_page.window.width = 650
    p_page.window.height = 200
    p_page.window.resizable = False
    p_page.window.maximizable = False
    p_page.window.always_on_top = True
    
    t_current_dir = os.path.dirname(os.path.abspath(__file__))
    t_icon_path = os.path.join(t_current_dir, "src","assets", "icon.ico")
    p_page.window.icon = t_icon_path
    
    AAT = AntiAFKTool()
    AAT.add_keyboard_listeners()
    l_aat_running_thread = Thread(target=AAT.run)
    l_aat_running_thread.start()
    def run():
        AAT.toggle()
    l_run_btn = ft.IconButton(ft.icons.Icons.RUN_CIRCLE, on_click=run, icon_color=ft.Colors.GREEN)
    
    async def check_is_running(p_page: ft.Page):
        
        while AAT.m_is_alive:
            p_page.title = f"({'ON' if AAT.m_is_running else 'OFF'}) " + LC_TITLE
            p_page.bgcolor = ft.Colors.GREEN_ACCENT_700 if AAT.m_is_running else ft.Colors.RED_ACCENT_700
            l_run_btn.icon_color = ft.Colors.RED_ACCENT_700 if AAT.m_is_running else ft.Colors.GREEN_ACCENT_700
            l_run_btn.icon = ft.icons.Icons.STOP_CIRCLE if AAT.m_is_running else ft.icons.Icons.RUN_CIRCLE
            try:
                p_page.update()
            except Exception as E: print(E)
            await asyncio.sleep(0.25)
    p_page.run_task(check_is_running, p_page)
    def open_settings():
        os.system(f'start {t_current_dir}\\settings.yml')
    
    def openDownloadPage():
        os.system('start https://github.com/justusdecker/ANTI-AFK-SKRIPT/releases')
    
    
    l_settings_btn = ft.IconButton(ft.icons.Icons.SETTINGS, on_click=open_settings, icon_color=ft.Colors.AMBER)
    
    l_download_newest_version_btn = ft.IconButton(ft.icons.Icons.UPDATE if get_version() != C_VERSION else ft.icons.Icons.UPDATE_DISABLED, on_click=openDownloadPage, icon_color=ft.Colors.GREEN if get_version() != C_VERSION else ft.Colors.GREY )
    
    
    l_button_column = ft.Column([l_run_btn, l_settings_btn, l_download_newest_version_btn])
    
    l_main_container = ft.Container(
        content=ft.Row([l_button_column, AAT.m_new_header]),    
        bgcolor=ft.Colors.BLACK_87,
        border_radius=ft.BorderRadius.all(5),
        
    )
    p_page.add(l_main_container)

if __name__ == '__main__':
    ft.run(main)