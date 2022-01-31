from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello World',
                                pos_hint={'center_x':0.5, 'center_y':0.5})
        icon_btn = MDIconButton(icon='motorbike',
                                pos_hint={'center_x':.8, 'center_y':0.5})
        icon_btn1 = MDFloatingActionButton(icon='android',
                                pos_hint={'center_x': .6, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        screen.add_widget(icon_btn1)
        return screen


DemoApp().run()
