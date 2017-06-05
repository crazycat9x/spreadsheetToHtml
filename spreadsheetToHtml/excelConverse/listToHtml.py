def listToHtml(tbl,final):
    rows = []
    cols = []
    count = 0

    for t in range(len(tbl)):
        for i in range(len(tbl[t])):
            if isinstance(tbl[t][i],float):
                if (tbl[t][i] * 10) % 10 == 0:
                    tbl[t][i] = int(tbl[t][i]) 
            if not isinstance(tbl[t][i],str):
                tbl[t][i] = str(tbl[t][i])

         
    for t in tbl:
        if count == 0:
            cols +=["<th>{0}</th>".format("</th><th>".join([x for x in t]))]
        else:
            cols +=["<td>{0}</td>".format("</td><td>".join([x for x in t]))]
        count += 1	

    for i in range(len(cols)):
        if i == 0:
            cols[i] += "</tr></thead><tbody><tr class = \"alt\">"
        elif i % 2 == 0:
            cols[i] += "</tr><tr class = \"alt\">"
        else:
            cols[i] += "</tr><tr>"
            
    rows = "<thead><tr>{0}</tr></tbody>".format("".join(cols))
    html = "<table>{0}</table>".format(rows)
    html = html.encode('ascii','replace').decode('ascii')
    display = open(final, "w")
    display.write(html)
    display.close()
