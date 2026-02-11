my_family = ['папа', 'мама', 'брат', 'бабушка']

my_family_height = [
    ['папа', 180],
    ['мама', 165],
    ['сестра', 170],
    ['бабушка', 160],
]

print(f"Рост отца - {my_family_height[0][1]} см")
height = 0
for person in my_family_height:
    height += person[1]
print(f"Общий рост моей семьи - {height} см")
