import colorgram

colors = colorgram.extract('colorgram.jpg', 12)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_extracted = (r,g,b)
    rgb_colors.append(colors_extracted)


print(rgb_colors)

