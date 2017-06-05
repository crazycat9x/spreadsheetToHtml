def styling(target):
    style = open("./styling/style.css","r").read()
    temp = open(target).read()
    temp = "<div><style scoped>" + style + "</style><div class = \"datagrid\">" + temp + "</div></div>"
    final = open(target, "w", encoding="utf-8")
    final.write(temp)
