import sys

with open('links.txt') as f:
    content = f.readlines()

    linklist = []
    for link in content:
        # print(link)
        link = link.split(";")
        # print(link)
        linklist.extend(link)
    linklist_ = [x.strip() for x in linklist]

    with open('output.txt', 'w') as o:
        for ftplink in linklist_:
          o.write("%s\n" % ftplink)