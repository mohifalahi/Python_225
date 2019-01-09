def two_fer(name="you"):
    user_name = input("Enter a name or leave it empty: ")
    if not user_name:
        return "One for {}, one for me.".format(name)
    else:
        return "One for {}, one for me.".format(user_name)

print(two_fer())