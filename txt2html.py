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
    e.write("</body></html>\n\n\n<!-- Converted to HTML by github.com/V1A0/txt2html\nCopyright © 2019 Vladimir Ageenko (V1A0)/n/nPermission is hereby granted, free of charge, to any person obtaining a copy of/nthis software and associated documentation files (the \"Software\"), to deal in/nthe Software without restriction, including without limitation the rights to/nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies/nof the Software, and to permit persons to whom the Software is furnished to do/nso, subject to the following conditions:/n/nThe above copyright notice and this permission notice shall be included in all/ncopies or substantial portions of the Software./n/nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR/nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,/nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE/nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER/nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,/nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE/nSOFTWARE./n -->")
