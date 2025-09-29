import fitz 



pdf = input("Nazwa pliku pdf do zmodyfikowania:\n")
doc = fitz.open(pdf)
page = doc[-1]
prompt=input("Tekst do wstrzyknięcia:\n")
fontsize = 1
page_width, page_height = page.rect.width, page.rect.height
x = 5 
y = 10
y2 = page_height - 10
pix = page.get_pixmap()
bg_color = pix.pixel(5, pix.height - 5)
r, g, b  = bg_color
r /= 255
g /= 255
b /= 255

output = input("Nazwa zmodyfikowanego pliku:\n")

page.insert_text((x,y), prompt, fontsize=fontsize, color=(r,g,b))
page.insert_text((x, y2), prompt, fontsize=fontsize, color=(r,g,b))
doc.save(output)




