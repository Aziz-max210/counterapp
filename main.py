from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

# Устанавливаем размер окна для тестирования
Window.size = (300, 500)

# KV-дизайн
KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(20)
    md_bg_color: 0.1, 0.1, 0.1, 1  # Темный фон

    # Градиентный фон (с использованием canvas)
    canvas.before:
        Color:
            rgba: 0.1, 0.3, 0.5, 0.7
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'gradient.png'  # Опционально: создайте градиентное изображение

    MDLabel:
        id: counter_label
        text: 'Кликов: 0'
        halign: 'center'
        font_style: 'H3'
        theme_text_color: 'Custom'
        text_color: 1, 1, 1, 1  # Белый текст для контраста
        size_hint_y: 0.4
        shadow_color: 0, 0, 0, 0.5  # Тень для текста

    MDRaisedButton:
        id: button
        text: 'Нажми!'
        pos_hint: {'center_x': 0.5}
        md_bg_color: 0, 0, 0, 1  # Черный цвет кнопки
        elevation: 10
        size_hint: 0.8, 0.3
        radius: [dp(25), dp(25), dp(25), dp(25)]  # Закругленные углы
        text_color: 1, 1, 1, 1  # Белый цвет текста
        icon: 'play-circle'  # Иконка на кнопке
        icon_color: 1, 1, 1, 1
        on_press: app.increment_counter(self)
'''


class CounterApp(MDApp):
    def __init__(self):
        super().__init__()
        self.count = 0

    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Основная палитра
        self.theme_cls.theme_style = "Dark"  # Темная тема
        return Builder.load_string(KV)

    def increment_counter(self, button):
        self.count += 1
        self.root.ids.counter_label.text = f'Кликов: {self.count}'

        # Анимация нажатия кнопки
        anim = Animation(scale_value_x=0.95, scale_value_y=0.95, duration=0.1) + \
               Animation(scale_value_x=1, scale_value_y=1, duration=0.1)
        anim.start(button)


if __name__ == '__main__':
    CounterApp().run()