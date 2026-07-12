from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser

Window.clearcolor = (0.05, 0.05, 0.05, 1)

class FinnDevApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=24, spacing=16)

        label = Label(
            text='Finn Dev',
            font_size='52sp',
            bold=True,
            color=(1, 1, 1, 1)
        )

        btn = Button(
            text='View Github Profile',
            size_hint=(1, None),
            height='56dp',
            background_color=(0.23, 0.36, 1, 1),
            font_size='16sp',
            bold=True
        )
        btn.bind(on_press=lambda x: webbrowser.open('https://github.com/finndev62'))

        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    FinnDevApp().run()
