def perimeter (lengh_of_room, width_of_room):
    result = (lengh_of_room + width_of_room) * 2
    return result
print(perimeter (5, 6))

def strip_of_wallpaper (perimeter, width_of_wallpaper):
    data = round(perimeter / width_of_wallpaper)
    return data
print(strip_of_wallpaper(22, 1.06))

def canvas_of_wallpaper (lengh_of_wallpaper, ceiling_heigt):
    total = round(lengh_of_wallpaper / ( ceiling_heigt + 0.10 ))
    return total
print(canvas_of_wallpaper(10, 2.75))

def number_of_wallpapers (data, total):
    value = data /total
    return value
