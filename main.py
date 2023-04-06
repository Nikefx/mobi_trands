from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from translator_logic import makeSomething, command, translateText


class MainApp(App):

    def __init__(self):
        super().__init__()
        self.text_out = TextInput(text='')
        self.text_in = TextInput(text='')

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout_hor2 = BoxLayout(orientation='horizontal')
        layout_hor1 = BoxLayout(orientation='horizontal')

        button_on = Button(text='Голосовой переводчик')
        button_on.bind(on_press=self.on_pressed_button_on)
        button_on1 = Button(text='Перевести')
        button_on1.bind(on_press=self.on_pressed_button_translate)

        label_on = Label(text='Перевести')
        label_out = Label(text='Переведено')

        layout.add_widget(button_on)

        layout_hor1.add_widget(label_on)
        layout_hor1.add_widget(label_out)
        layout_hor2.add_widget(self.text_in)
        layout_hor2.add_widget(self.text_out)

        layout.add_widget(layout_hor1)
        layout.add_widget(layout_hor2)
        layout.add_widget(button_on1)

        return layout

    def on_pressed_button_on(self, instance):
        list_translate = makeSomething(command())

        self.text_out.text = list_translate[1]
        self.text_in.text = list_translate[0]

    def on_pressed_button_translate(self, instance):
        text_for_translate = self.text_in.text
        text_in_translate = translateText(self.text_in.text)

        self.text_out.text = text_in_translate
        self.text_in.text = text_for_translate

        print(text_for_translate)
        print(text_in_translate)


if __name__ == '__main__':
    app = MainApp()
    app.run()