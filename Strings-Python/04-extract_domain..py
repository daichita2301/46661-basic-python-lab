line = input().strip()
atpos = line.find('@')
if atpos != -1:
    sp = line.find(' ', atpos)
    if sp == -1:
        domain = line[atpos+1:]
    else:
        domain = line[atpos+1:sp]
    print(domain)