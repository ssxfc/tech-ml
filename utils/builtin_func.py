class A:
    def __init__(self) -> None:
        print("A class initialized")

    def __call__(self):
        print("__call__")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
