from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"

        btn_flat = MDFlatButton(text='Show',
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn_flat)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = "Please Enter USERNAME"
        else:
            check_string = self.username.text
        close_button = MDFlatButton(text='Close', on_release=self.close_diloguebox)
        more_button = MDFlatButton(text='More')
        self.dilogue = MDDialog(title='Username check',
                           text=check_string,
                           size_hint=(0.7,1),
                           buttons=[close_button, more_button])
        self.dilogue.open()

    def close_diloguebox(self, obj):
        self.dilogue.dismiss()

DemoApp().run()
