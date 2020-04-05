"""
Главный экран приложеня
"""
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.config import Config

from app import MDApp
from news import news
from login import login
from greetings import greetings
from sidebar_screen import sidebar

Window.minimum_height = 500
Window.minimum_width = 500
Config.set('graphics', 'resizable', 0)
Window.fullsize = 'auto'
Window.release_all_keyboards()
print(Window.size)


for kvfile in ['EchoKamGU.kv',
               'news/news.kv',
               'login/login.kv',
               'greetings/greetings.kv',
               'sidebar_screen/sidebar.kv']:
    with open(kvfile, encoding='utf8') as f:
        Builder.load_string(f.read())


class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current = 'sidebar_screen'


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Green"

    def build(self):
        return MainScreenManager()


MainApp().run()
