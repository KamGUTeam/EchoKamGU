from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage

from kivy.app import App
from kivy.properties import ObjectProperty
from app import MDApp
from kivymd.toast import toast

import libs.database as db
import libs.ztweaks as ztweaks


class LogInScreen(Screen):
    from kivy.uix.behaviors.focus import FocusBehavior
    login_button_pressed = False
    # login_field = ObjectProperty(None)
    # password_field = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        # self.ids.login.is_focusable = True
        # self.ids.login.is_focusable = StopIteration
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        # print(self.ids.login.focus)
        if self.ids.login.focus and keycode[1] == 'tab':
            # self.ids.login.focused = True
            # print(self.ids.login.is_focused)
            # print(FocusBehavior.focus)
            from kivymd.toast import toast
            toast('Hello')

    def login_press(self):
        login = self.ids.login.text
        password = self.ids.password.text
        check_password_res = self.check_password(login, password)
        if check_password_res:
            with db.LocalDB() as localdb:
                localdb.set_startscreen(2)
                localdb.save_usertoken(check_password_res[0], check_password_res[1])
            self.main_manager.current = "news_screen"
            '''
            app = MDApp.get_running_app()
            if login == "Luna":
                app.theme_cls.primary_palette = "Blue"
            elif login == "Harry":
                app.theme_cls.primary_palette = "Red"
                app.theme_cls.primary_hue = "600"
            elif login == "Lord":
                app.theme_cls.primary_palette = "Green"
            elif login == "Cedric":
                app.theme_cls.primary_palette = "Orange"
            elif login == "Sybill":
                app.theme_cls.primary_palette = "DeepPurple"
            '''

    def check_password(self, login, password):
        if db.check_internet_connection():
            if ztweaks.GlobalVars().meme_mode:
                if not self.login_button_pressed:
                    self.login_button_pressed = True
                    from kivy.core.audio import SoundLoader
                    sound = SoundLoader.load("login/end.mp3")
                    sound.play()
            else:
                #  real mode, ea >B-)
                loginfunc_res = db.LoginFunc(login, password)
                if loginfunc_res:
                    return loginfunc_res[0], loginfunc_res[1]
                ztweaks.invalidlogin_notify()
                return None
        else:
            ztweaks.nointernet_notify()
