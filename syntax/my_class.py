class X:
    avoids_symlink_attacks: bool
    x = 1
    print("属于类的初始化代码")
    def __init__(self):
        print("属于实例的初始化代码")

X()