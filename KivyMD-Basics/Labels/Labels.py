from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        # theme_text_color='Error'=====Red color
        # theme_text_color='Secondary'==Grey
        # theme_text_color='Custom'===text_color=(0,1,0,1)
        label = MDLabel(text="Hello World", halign='center', theme_text_color='Custom',
                        text_color=(0, 1, 0, 1),
                        font_style='H1')

        icon_label = MDIcon(icon = "language-python", halign='center')

        return icon_label


DemoApp().run()
