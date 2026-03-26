"""
SEMANA 7 - CONJUNTO CON LISTA ENLAZADA
=========================================
Implementación desde cero usando nodos encadenados.
Los conjuntos NO permiten duplicados.
"""


# ─── NODO ────────────────────────────────────────────────────────────────────

class Nodo:
    """Bloque básico de la lista: guarda un dato y apunta al siguiente."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None   # por defecto apunta a nada (None = fin de lista)


# ─── CONJUNTO ────────────────────────────────────────────────────────────────

class Conjunto:

    def __init__(self, elementos=None):
        self.cabeza = None   # primer nodo de la cadena
        self.tamaño = 0

        # Si nos pasan una lista inicial, agregamos cada elemento
        if elementos:
            for e in elementos:
                self.agregar(e)

    # ── OPERACIONES BÁSICAS ──────────────────────────────────────────────────

    def pertenece(self, x):
        """Recorre la lista buscando x. O(n)"""
        actual = self.cabeza
        while actual:                      # mientras no lleguemos al None final
            if actual.dato == x:
                return True
            actual = actual.siguiente      # avanzar al siguiente nodo
        return False

    def agregar(self, x):
        """Inserta x al inicio de la lista (solo si no existe)."""
        if self.pertenece(x):
            return False                   # ya está → nada que hacer
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza      # nuevo apunta al que era primero
        self.cabeza = nuevo                # ahora el nuevo ES el primero
        self.tamaño += 1
        return True

    def eliminar(self, x):
        """Quita x de la lista. Caso especial: si está en la cabeza."""
        if self.esta_vacio():
            return False

        # Caso especial: el elemento está en la cabeza
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True

        # Caso general: buscar nodo anterior al que queremos borrar
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente  # saltar el nodo
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False                       # no encontrado

    def esta_vacio(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamaño

    # ── OPERACIONES ENTRE CONJUNTOS ──────────────────────────────────────────

    def union(self, otro):
        """A ∪ B — agrega todos los de A, luego los de B (sin repetir)."""
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)   # agregar ya ignora duplicados
            actual = actual.siguiente

        return resultado

    def interseccion(self, otro):
        """A ∩ B — solo los que están en los dos."""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):  # ¿también está en B?
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia(self, otro):
        """A − B — los de A que NO están en B."""
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):  # ¿NO está en B?
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia_simetrica(self, otro):
        """A △ B = (A−B) ∪ (B−A) — lo que tiene uno pero no el otro."""
        return self.diferencia(otro).union(otro.diferencia(self))

    # ── RELACIONES ───────────────────────────────────────────────────────────

    def es_subconjunto(self, otro):
        """¿self ⊆ otro? — ¿todos los elementos de self están en otro?"""
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False              # encontramos uno que no está → NO es subconjunto
            actual = actual.siguiente
        return True                       # todos estaban → SÍ es subconjunto

    def es_igual(self, otro):
        """¿self == otro? — mismos elementos."""
        if self.tamaño != otro.tamaño:
            return False
        return self.es_subconjunto(otro)  # mismo tamaño + subconjunto = iguales

    # ── UTILIDADES ───────────────────────────────────────────────────────────

    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"

    def __len__(self):
        return self.tamaño

    def __contains__(self, x):   # permite usar: x in conjunto
        return self.pertenece(x)


# ─── DEMO ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 4, 5, 6])

    print(f"A = {A}")
    print(f"B = {B}")

    print(f"\nA ∪ B = {A.union(B)}")
    print(f"A ∩ B = {A.interseccion(B)}")
    print(f"A − B = {A.diferencia(B)}")
    print(f"A △ B = {A.diferencia_simetrica(B)}")

    C = Conjunto([3, 4])
    print(f"\nC = {C}")
    print(f"C ⊆ A: {C.es_subconjunto(A)}")   # True
    print(f"A ⊆ C: {A.es_subconjunto(C)}")   # False

    print(f"\n3 in A: {3 in A}")              # True (usa __contains__)
    print(f"len(A): {len(A)}")                # 4

    # Iterar con el método a_lista
    print("\nElementos de A:")
    for x in A.a_lista():
        print(f"  {x}")
