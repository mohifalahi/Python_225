def abbreviate(words = 'Massachusets institute of technology'):
    x = words.split()
    l = "".join(e[0] for e in x)
    u = l.upper()
    return u

print(abbreviate())
