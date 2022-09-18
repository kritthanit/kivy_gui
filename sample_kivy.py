from kivy.app import App
from kivy.uix.label import Label


class MyNameApp(App):
    def build(self):
        lb = Label(text='Hello World...')
        return lb


if __name__ == '__main__':
    app = MyNameApp()
    app.run()

