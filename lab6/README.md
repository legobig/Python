# 1 ВАРИАНТ
Геометрические фигуры:<br>
-Прямоугольник<br>
-Треугольник<br>
-Трапеция<br>
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
<img width="1514" height="74" alt="image" src="https://github.com/user-attachments/assets/62407969-6bf6-49d6-a1fa-a5bd83865f9f" />






1. Генератор ```gen``` является бесконечным, что позволяет получать неограниченное количество псевдослучайных чисел<br>
2. Функция ```count_del``` выполняет полный перебор делителей, что при больших значениях n может быть неэффективным, но в рамках диапазона 1–50 работает корректно <br>





# Список использованных источников:
1. [yield в Python](https://habr.com/ru/articles/132554/)
2. [filter в Python](https://thecode.media/funkciya-filter-v-python/)
