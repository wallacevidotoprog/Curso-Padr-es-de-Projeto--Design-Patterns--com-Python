class Singleton:
    __instance = None

    def __init__(self) -> None:
        if Singleton.__instance is None:
            print("O método init foi chamado")
            Singleton.__instance = self
        else:
            print(f"A instância já foi criada: {self.get_instance()}")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance


# Testando o Singleton
s1 = Singleton()
print(f"Obj create: {Singleton.get_instance()}")

s2 = Singleton()
