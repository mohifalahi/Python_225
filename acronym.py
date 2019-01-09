def abbreviate(words = 'Massachusets institute of technology'):
    e = words.split()
    return "".join(_[0] for _ in e).upper()

print(abbreviate())

