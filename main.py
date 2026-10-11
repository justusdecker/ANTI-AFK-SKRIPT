import keyboard
from win32api import Beep
from random import randint
from time import sleep, time 
from threading import Thread
from requests import get
C_VERSION = '0.2'
C_SHORT_BEEP_DURATION = 200
C_LONG_BEEP_DURATION = 400

def get_version() -> str:
    try:
        return get('https://raw.githubusercontent.com/justusdecker/ANTI-AFK-SKRIPT/refs/heads/main/version.json').json().get('version')
    except Exception:
        return C_VERSION
class AntiAFKTool:
    m_is_running = False
    m_thread_alive = False
    
    m_left_mouse = 'ö'
    m_toggle_key = 'F12'
    
    m_times_until_press_and_release = 1
    
    m_not_running_sleep_duration = 0.2
    m_random_sleep_time_from = 1
    m_random_sleep_time_to = 3
    m_sleep_time_multiplier = 1.5
    
    m_pressed_keys = set()
    
    m_header = f"""\033[35mANTI AFK Script ©2025 - 2026 Justus Decker. All rights reserved.\033[0m
{'\033[33mA new Update is avaiable! Get it from https://github.com/justusdecker/ANTI-AFK-SKRIPT/releases\033[0m' if get_version() != C_VERSION else ''}
Help:
    Press '\033[35m{m_toggle_key}\033[0m' to toggle on/off the ANTI AFK SCRIPT(you will hear 3 beeps after that)
    Repetitive '\033[35mÖ\033[0m' presses for simulating the '\033[35mLEFT CLICK\033[0m'
    [\033[32m@will-be-added\033[0m] German Translation
    [\033[32m@will-be-added\033[0m] Mouse Support
    [\033[32m@will-be-added\033[0m] Create your own custom scripts
"""
    
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
        print(f"The Script is now {'\033[32mON' if self.m_is_running else '\033[31mOFF'}\033[0m")
        if self.m_is_running:
            self.beep_thread_starter(C_LONG_BEEP_DURATION)
        else:
            self.release_all()
            self.beep_thread_starter(C_SHORT_BEEP_DURATION)
            
    
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
    
    def run(self):
        keyboard.on_press_key(self.m_toggle_key,self.toggle)
        print(self.m_header)
        while 1:
            if not self.m_is_running:
                sleep(self.m_not_running_sleep_duration)
                continue
            #self.press_and_release(self.m_jump_button, self.m_jump_sleep_duration)
            self.press_and_release(self.m_left_mouse, 10)
            for i in range(self.m_times_until_press_and_release):
                if not self.m_is_running: break
                sleep(1) # randint(self.m_random_sleep_time_from, self.m_random_sleep_time_to) * self.m_sleep_time_multiplier


if __name__ == '__main__':
    AntiAFKTool().run()