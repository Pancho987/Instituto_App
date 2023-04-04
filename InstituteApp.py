from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

# Declare Windows app size
Window.size = (310, 580)

kv = """
#:import NoTransition kivy.uix.screenmanager.NoTransition
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Instituto Número 1"
        
    ScreenManager:
        id: scr
        transition: NoTransition()

        MDScreen:
            name: "home"

            MDLabel:
                text: "Home"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "files"
            MDLabel:
                text: "Files"
                pos_hint: {"center_y": .5}
                halign: "center"
        MDScreen:
            name: "info"
            MDLabel:
                text: "Info"
                pos_hint: {"center_y": .5}
                halign: "center"

    NavBar:
        size_hint: .85, .1
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 0
        md_bg_color: 1, 0, 0, 0
        radius: [16]
        MDGridLayout:
            cols: 3
            size_hint_x: .9
            spacing: 37
            pos_hint: {"center_x": .5, "center_y": .8}
            MDIconButton:
                id: nav_icon1
                icon: "file"
                riple_scale: 0
                icon_size: "30sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "files"

            MDIconButton:
                id: nav_icon2
                icon: "home"
                riple_scale: 0
                icon_size: "30sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "home"
            MDIconButton:
                id: nav_icon3
                icon: "email-newsletter"
                riple_scale: 0
                icon_size: "30sp"
                theme_icon_color: "Custom"
                icon_color: app.theme_cls.primary_color
                on_release:
                    scr.current = "info"      
"""
# Create Nav Bar at the bottom
class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

# Create the Window with the different screens above
class InstituteApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_string(kv)
    
    def on_start(self):
        self.fps_monitor_start()
    
if __name__ == "__main__":
    InstituteApp().run()
