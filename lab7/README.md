# 1 ВАРИАНТ
Перепишите свой вариант ЛР №6 с использованием классов и объектов. Задание то же, вариант GUI фреймворка возьмите следующий по списку. Для успешной сдачи в коде должны присутствовать:

- использование абстрактного базового класса и соотвествующих декораторов для методов,
- иерархия наследования,
- managed - атрибуты,
- минимум 2 dunder-метода у каждого класса.


# Результаты вычислений:
```python
import math
from report.report_generator import save_doc, save_xls
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from geometry_pkg.praym import Praym
from geometry_pkg.treug import Treug
from geometry_pkg.trapez import Trapez

class Main(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.current_shape = None

        
        self.input_a = TextInput(hint_text="Сторона a", multiline=False)
        self.input_b = TextInput(hint_text="Сторона b", multiline=False)
        self.input_c = TextInput(hint_text="c / h", multiline=False)

        self.add_widget(self.input_a)
        self.add_widget(self.input_b)
        self.add_widget(self.input_c)

        
        self.add_widget(Button(text="Прямоугольник", on_press=self.calc_rectangle))
        self.add_widget(Button(text="Треугольник", on_press=self.calc_triangle))
        self.add_widget(Button(text="Трапеция", on_press=self.calc_trapezoid))

        
        self.add_widget(Button(text="Сохранить в Word", on_press=self.save_doc_file))
        self.add_widget(Button(text="Сохранить в Excel", on_press=self.save_xls_file))

        
        self.result = Label(text="Результат", size_hint_y=2)
        self.add_widget(self.result)


    def show(self, shape):
        self.current_shape = shape
        self.result.text = ( f"{shape.__str__()}\n"
                             f"Площадь: {shape.s()}\n"
                             f"R описанной: {shape.opis_radius()}\n"
                             f"r вписанной: {shape.vpis_radius()}" )

    def calc_rectangle(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            shape = Praym(a, b)
            self.show(shape)
        except:
            self.result.text = "Ошибка ввода"

    def calc_triangle(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            c = float(self.input_c.text)
            shape = Treug(a, b, c)
            self.show(shape)
        except:
            self.result.text = "Ошибка ввода"

    def calc_trapezoid(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            h = float(self.input_c.text)
            shape = Trapez(a, b, h)
            self.show(shape)
        except:
            self.result.text = "Ошибка ввода"

    def save_doc_file(self, instance):
        if self.current_shape:
            save_doc(self.current_shape)
            self.result.text = "Сохранено в report.docx"
        else:
            self.result.text = "Сначала выполните расчёт"

    def save_xls_file(self, instance):
        if self.current_shape:
            save_xls(self.current_shape)
            self.result.text = "Сохранено в report.xlsx"
        else:
            self.result.text = "Сначала выполните расчёт"


class MyApp(App):
    def build(self):
        return Main()


if __name__ == "__main__":
    MyApp().run()

```
<img width="802" height="632" alt="image" src="https://github.com/user-attachments/assets/39af275b-a5e3-4d9e-a13a-bca86eaf760f" />








1. Абстрактный базовый класс Shape задаёт общий интерфейс для всех геометрических фигур <br>
2. Managed-атрибут name через @property обеспечивает контролируемый доступ к данным объекта <br>
3. Каждый расчёт создаёт новый объект фигуры и заменяет предыдущий результат <br>






# Список использованных источников:
1. [Kivy — Python](https://sky.pro/wiki/python/kivy-razrabotka-krossplatformennyh-prilozhenij-na-python/)
2. [Kivy - Quick Guide](https://translated.turbopages.org/proxy_u/en-ru.ru.25080973-69dfbad0-696d39e5-74722d776562/https/www.tutorialspoint.com/kivy/kivy-quick-guide.htm)
