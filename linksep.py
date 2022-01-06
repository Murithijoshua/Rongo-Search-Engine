def separatelinks():
    with open('/home/jj/projects/search/search/links.txt', 'r') as r:
        data = r.read()
        data =data.split(",")
        data = set(data)
    with open('/home/jj/projects/search/search/links.txt', 'w') as r:
        for i in data:
            r.write(i + '\n')
            
separatelinks()