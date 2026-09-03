# Operaciones con pilas
# Programa con menú para crear pila, mostrar, contar elementos, push, pop, peek, isEmpty e isFull

class Pila:
    def __init__(self, capacidad=None):
        self.elementos = []
        self.capacidad = capacidad

    def push(self, valor):
        if self.isFull():
            return False
        self.elementos.append(valor)
        return True

    def pop(self):
        if self.isEmpty():
            return None
        return self.elementos.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.elementos[-1]

    def isEmpty(self):
        return len(self.elementos) == 0

    def isFull(self):
        if self.capacidad is None:
            return False
        return len(self.elementos) >= self.capacidad

    def size(self):
        return len(self.elementos)

    def mostrar(self):
        if self.isEmpty():
            print("La pila está vacía")
        else:
            print("Pila (de la base a la cima):")
            for i, v in enumerate(self.elementos):
                if i == len(self.elementos) - 1:
                    print(f"  {v}  <-- cima")
                else:
                    print(f"  {v}")


def menu():
    print("\n----- MENÚ PILA -----")
    print("1. Crear pila")
    print("2. Imprimir pila")
    print("3. Cantidad de elementos")
    print("4. Push")
    print("5. Pop")
    print("6. Peek")
    print("7. isEmpty")
    print("8. isFull")
    print("0. Salir")
    print("--------------------")


def main():
    pila = None

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "0":
            print("Saliendo...")
            break

        if op == "1":
            cap = input("Capacidad (dejar vacío si no quieres límite): ").strip()
            if cap == "":
                pila = Pila()
            else:
                try:
                    pila = Pila(int(cap))
                except:
                    print("Capacidad inválida")
                    continue
            print("Pila creada")
            continue

        if pila is None:
            print("Primero crea una pila (opción 1)")
            continue

        if op == "2":
            pila.mostrar()

        elif op == "3":
            print("Cantidad de elementos:", pila.size())

        elif op == "4":
            valor = input("Valor a apilar: ")
            if pila.push(valor):
                print("Se apiló correctamente")
            else:
                print("La pila está llena")

        elif op == "5":
            valor = pila.pop()
            if valor is None:
                print("La pila está vacía")
            else:
                print("Se desapiló:", valor)

        elif op == "6":
            valor = pila.peek()
            if valor is None:
                print("La pila está vacía")
            else:
                print("Cima:", valor)

        elif op == "7":
            if pila.isEmpty():
                print("Sí, está vacía")
            else:
                print("No, tiene elementos")

        elif op == "8":
            if pila.isFull():
                print("Sí, está llena")
            else:
                print("No está llena")

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()