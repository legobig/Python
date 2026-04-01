# 1 ВАРИАНТ
Геометрические фигуры:<br>
 - Прямоугольник<br>
 - Треугольник<br>
 - Трапеция

Расчёт площади, радусов описанной и вписанной окружности.


# Результаты вычислений:
```python
import tkinter as tk

from geometry_pkg import praym, treug, trapez
from report.report_generator import save_doc, save_xls

results = {}

def calc_praym():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        results.clear()
        results["Фигура"] = "Прямоугольник"
        results["Площадь"] = praym.s(a, b)
        results["R описанной"] = praym.opis_radius(a, b)
        results["r вписанной"] = praym.vpis_radius(a, b)

        show_results()

    except ValueError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Ошибка: введите числа")
def calc_treug():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        results.clear()
        results["Фигура"] = "Треугольник"
        results["Площадь"] = treug.s(a, b, c)
        results["R описанной"] = treug.opis_radius(a, b, c)
        results["r вписанной"] = treug.vpis_radius(a, b, c)

        show_results()

    except ValueError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Ошибка: введите числа")
def calc_trapez():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        h = float(entry3.get())
        results.clear()
        results["Фигура"] = "Трапеция"
        results["Площадь"] = trapez.s(a, b, h)
        results["r вписанной"] = trapez.vpis_radius(a, b, h)

        show_results()

    except ValueError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Ошибка: введите числа")

def show_results():
    text.delete(1.0, tk.END)
    for k, v in results.items():
        text.insert(tk.END, f"{k}: {v}\n")


root = tk.Tk()
root.title("Геометрические фигуры")
root.geometry("950x800")


tk.Label(root, text="Сторона a:").pack()
entry1 = tk.Entry(root)
entry1.pack()


tk.Label(root, text="Сторона b:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="c или h:").pack()
entry3 = tk.Entry(root)
entry3.pack()


tk.Button(root,
          text="Рассчитать прямоугольник",
          command=calc_praym).pack(pady=5)
tk.Button(root,
          text="Рассчитать треугольник",
          command=calc_treug).pack(pady=5)
tk.Button(root,
          text="Рассчитать трапецию",
          command=calc_trapez).pack(pady=5)

text = tk.Text(root, height=30, width=100)
text.pack()

tk.Button(root,
          text="Сохранить в Word",
          command=lambda: save_doc(results)).pack(pady=2)

tk.Button(root,
          text="Сохранить в Excel",
          command=lambda: save_xls(results)).pack(pady=2)

root.mainloop()

```
<img width="950" height="800" alt="image" src="https://github.com/user-attachments/assets/754a6304-4d26-42d5-8219-ca4f12d92813" />







1. Приложение является универсальным инструментом для вычисления параметров геометрических фигур, что позволяет пользователю быстро получать площадь и радиусы для различных фигур и сохранять результаты в удобные форматы.<br>
2. Использование отдельных модулей для вычислений делает код структурированным и расширяемым <br>
3. Результаты вычислений можно сохранять в форматы Word и Excel, что повышает практическую ценность программы.<br>
4. Обработка ошибок ввода обеспечивает стабильную работу приложения и предотвращает некорректные расчёты.<br>





# Список использованных источников:
1. [tkinter](https://docs.python.org/3/library/tkinter.html)
2. [tkinter](https://thecode.media/biblioteka-tkinter-v-python/)
