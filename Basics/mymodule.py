def greeting(name):
    print("Hello, " + name)


def stringify(name, age, country, hobbies):
    return "{}".format({
        "name": name,
        "age": age,
        "country": country,
        "hobbies": hobbies
    })
