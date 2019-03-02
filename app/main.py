from app.lib import *
if __name__ == '__main__':
     width_of_wallpaper = float (input('Какая ширина у обоев? '))
     print(width_of_wallpaper)

     data = strip_of_wallpaper(perimeter, width_of_wallpaper )#
     data = round( perimeter / width_of_wallpaper)
     print(data)
     print(strip_of_wallpaper(22, 1.06))

     total = canvas_of_wallpaper(lengh_of_wallpaper, ceiling_heigt)#
     total = round(lengh_of_wallpaper / (ceiling_heigt + 0.10))
     print(total)
     print(canvas_of_wallpaper(10, 2.75))

     number_of_wallpapers(data, total)#k
     value = round(data / total)
     print (value)
     print(number_of_wallpapers)
