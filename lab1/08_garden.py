garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
garden_set = set(garden)
meadow_set = set(meadow)
print("Все виды цветов:", garden_set | meadow_set)

print("Цветы, которые растут и в саду, и на лугу:", garden_set & meadow_set)


print("Цветы, которые растут только в саду:", garden_set - meadow_set)


print("Цветы, которые растут только на лугу:", meadow_set - garden_set)
