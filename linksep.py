with open('/home/jj/projects/search/search/links.txt', 'r') as r:
    data = r.read()
    data =set(data.split(","))
with open('/home/jj/projects/search/search/links.txt', 'w') as r:
    for i in data:
        r.write(i + '\n')