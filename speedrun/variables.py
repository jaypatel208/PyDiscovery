a = 10
b = 20
a, b = b, a

x = "global"
print(x)


def outer():
    x = "enclosing"
    print(x)

    def inner():
        x = "local"
        print(x)
    inner()


outer()
