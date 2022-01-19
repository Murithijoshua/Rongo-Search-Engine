def separatelinks():
    with open('../links.txt', 'r') as r:
        data = r.read()
        data =data.split(",")
        data = set(data)
    with open('../links.txt', 'w') as r:
        for i in data:
            r.write(i.strip()+'\n')
                
separatelinks()