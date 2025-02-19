import colorgram

colors = colorgram.extract("hirst.jpg", 101)
tuple_colors = []

for color in colors:
    tuple_colors.append(tuple(color.rgb))

print(tuple_colors)
