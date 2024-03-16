from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Interpase(FloatLayout):
    def Display(self):
        data=self.ids.textinput.text
        self.ids.label.text=data
class myapp(App):
    pass
myapp().run()