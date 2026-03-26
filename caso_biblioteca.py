"""
═══════════════════════════════════════════════════════════════════════════════
                    POSIBLE PARCIAL — Biblioteca Digital
                    Lista de Préstamos de Libros
═══════════════════════════════════════════════════════════════════════════════
PUNTO 1: Nodo = Libro | Lista = ColaPrestamos
         Atributos: titulo, categoria (digital/fisico), dias_prestamo
PUNTO 2: digitales → inicio | fisicos → final (RECURSIVO)
PUNTO 3: dias acumulados antes de un libro (RECURSIVO)
PUNTO 4: entregar el primer libro de la lista
PUNTO 5: contar por categoria (RECURSIVO) → tupla (digitales, fisicos)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, titulo, categoria, dias):
        self.titulo    = titulo
        self.categoria = categoria   # "digital" o "fisico"
        self.dias      = dias        # días de préstamo
        self.siguiente = None

class ColaPrestamos:
    def __init__(self):
        self.cabeza = None

    # ── PUNTO 2: agregar libro ────────────────────────────────────────────────
    def agregar_libro(self, titulo, categoria, dias):
        nuevo = Nodo(titulo, categoria, dias)
        if categoria == "digital":
            if self.cabeza is None or self.cabeza.categoria == "fisico":
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                self._tras_digitales(self.cabeza, nuevo)
        else:
            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                self._al_final(self.cabeza, nuevo)

    def _tras_digitales(self, actual, nuevo):
        if actual.siguiente is None or actual.siguiente.categoria == "fisico":
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._tras_digitales(actual.siguiente, nuevo)

    def _al_final(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._al_final(actual.siguiente, nuevo)

    # ── PUNTO 3: días acumulados antes del libro ──────────────────────────────
    def dias_espera(self, titulo):
        return self._acumular(self.cabeza, titulo, 0)

    def _acumular(self, actual, titulo, acum):
        if actual is None:
            return -1
        if actual.titulo == titulo:
            return acum
        return self._acumular(actual.siguiente, titulo, acum + actual.dias)

    # ── PUNTO 4: entregar el primero ──────────────────────────────────────────
    def entregar_siguiente(self):
        if self.cabeza is None:
            return None
        entregado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        entregado.siguiente = None
        return entregado

    # ── PUNTO 5: contar por categoría ────────────────────────────────────────
    def contar_por_categoria(self):
        return self._contar(self.cabeza, 0, 0)

    def _contar(self, actual, digitales, fisicos):
        if actual is None:
            return (digitales, fisicos)
        if actual.categoria == "digital":
            return self._contar(actual.siguiente, digitales + 1, fisicos)
        else:
            return self._contar(actual.siguiente, digitales, fisicos + 1)

    def mostrar(self):
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  {i}. {actual.titulo:<25} | {actual.categoria:<8} | {actual.dias} dias")
            actual = actual.siguiente
            i += 1

if __name__ == "__main__":
    cola = ColaPrestamos()
    cola.agregar_libro("Harry Potter",       "fisico",  14)
    cola.agregar_libro("Python Crash Course","digital",  7)
    cola.agregar_libro("El Principito",      "fisico",  10)
    cola.agregar_libro("Clean Code",         "digital",  5)
    cola.agregar_libro("Don Quijote",        "fisico",  21)

    print("Cola de préstamos:")
    cola.mostrar()

    print(f"\nDias de espera de 'El Principito': {cola.dias_espera('El Principito')}")
    print(f"Dias de espera de 'Don Quijote':   {cola.dias_espera('Don Quijote')}")
    print(f"Libro inexistente:                 {cola.dias_espera('Inexistente')}")

    dig, fis = cola.contar_por_categoria()
    print(f"\nDigitales: {dig}, Físicos: {fis}")

    print(f"\nEntregando: {cola.entregar_siguiente().titulo}")
    print(f"Entregando: {cola.entregar_siguiente().titulo}")
    print("\nCola restante:")
    cola.mostrar()
