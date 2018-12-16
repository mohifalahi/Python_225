# d = {"name": "ali", "family": "kalan", "age": 10}
# for k, v in d.items():
# print(d.get("name"))

def get_freq(str):
    d = {}
    for _ in str:
        keys = d.keys()
        if _ in keys:
            d[_] += 1
        else:
            d[_] = 1
    return d

print(get_freq("Mohi Falahi"))


