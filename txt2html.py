print('Enter file name: ')
a = input()
print('Enter title: ')
b = input()
contents = open(a, 'r')
with open("txt2html.html", "w") as e:
    e.write("<html>\n  <head><meta charset=\"UTF-8\">\n  <title>" + b + "</title>\n  <link href=\"/style.css\" rel=\"stylesheet\" type=\"text/css\" media=\"all\"></head><body>")
with open("txt2html.html", "a") as e:
    for lines in contents.readlines():
        e.write(lines + "<br>\n")
with open("txt2html.html", "a") as e:
    e.write("</body></html>\n\n\n<!-- Converted to HTML by github.com/V1A0/txt2html -->")
