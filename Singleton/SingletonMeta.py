class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Cria e armazena a instância única
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Instância criada")


# Testando o Singleton
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Deve exibir True, pois ambas as variáveis referenciam a mesma instância
