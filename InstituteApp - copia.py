from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


# Declare Windows app size
# Window.size = (310, 600)

kv = """
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Instituto Número 1"
        
                
    MDScreen:
        MDBottomNavigation:
            # panel_color: "#eeeaea"
            # selected_color_background: "red"
            text_color_active: app.theme_cls.primary_color

            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Files'
                theme_font_styles: "H3"
                icon: 'file'
                #badge_icon: "numeric-10"

                ScrollView:
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: 10
                        size_hint: 1, None
                        height: self.minimum_height

                        MDRaisedButton:
                            text: "Documentación Util"
                            text_color: "black"
                            md_bg_color: app.theme_cls.primary_dark
                            font_size: "20sp"
                            size_hint: 1, None
                            #size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                        MDRaisedButton:
                            text: "Diseños Curriculares"
                            text_color: "black"
                            md_bg_color: "lightblue"
                            font_size: "20sp"
                            size_hint: .8, None
                            # size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                            on_release:
                                import webbrowser
                                webbrowser.open('https://drive.google.com/drive/folders/1hazeaTHs0JlcSZ_Q3WchiY0UmRIwTYfd?hl=es')
                                print('Yeaaaaaaaaah!! It Worksssssss')                            
                        MDRaisedButton:
                            text: "Resoluciones"
                            text_color: "black"
                            md_bg_color: "lightblue"
                            font_size: "20sp"
                            size_hint: .8, None
                            # size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                        MDRaisedButton:
                            text: "Instructivos"
                            text_color: "black"
                            md_bg_color: "lightblue"
                            font_size: "20sp"
                            size_hint: .8, None
                            # size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                        MDRaisedButton:
                            text: "Web DGES Corrientes"
                            text_color: "black"
                            md_bg_color: "lightblue"
                            font_size: "20sp"
                            size_hint: .8, None
                            # size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                            on_release:
                                import webbrowser
                                webbrowser.open('http://www.dgescorrientes.net/')
                        MDRaisedButton:
                            text: "A"
                            text_color: "black"
                            md_bg_color: "lightblue"
                            font_size: "20sp"
                            size_hint: .8, None
                            # size: "100dp", "80dp"
                            pos_hint: {"center_x": .5, "center_y": .5}
                                  
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Home'
                icon: 'home'
                #badge_icon: "numeric-5"

                MDLabel:
                    text: 'Home'
                    halign: 'center'

            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'News'
                icon: 'email-newsletter'

                MDLabel:
                    text: 'News'
                    halign: 'center'
"""

# Create the Window with the different screens above
class InstituteApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(kv)
    
    """def on_start(self):
        self.fps_monitor_start()"""
    
if __name__ == "__main__":
    InstituteApp().run()
