import webbrowser as wb
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
wb.register('chrome',
        None,
        wb.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


class MainLay(GridLayout):

    def __init__(self, **kwargs):

        super(MainLay, self).__init__(**kwargs)

        Button.background_color = 1, .3, .4, .85
        # Button.background_down = 1, 0, 0, 0

        self.rows = 2
        self.cols = 1
        self.link = TextInput(multiline=True)
        self.add_widget(self.link)
        # self.link.text = "Enter Your Link Here"

        self.Search = Button(text="Search", font_size=40)
        self.Search.bind(on_press=self.pressed)
        self.add_widget(self.Search)

    def pressed(self, instance):
        wb.get("chrome").open(self.link.text)

    

class SearchApp(App):
    def build(self):
        a = MainLay()
        return a


if __name__ == '__main__':
    SearchApp().run()