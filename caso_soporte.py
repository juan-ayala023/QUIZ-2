"""
═══════════════════════════════════════════════════════════════════════════════
                    POSIBLE PARCIAL — Centro de Soporte Técnico
                    Sistema de Tickets de Soporte
═══════════════════════════════════════════════════════════════════════════════
PUNTO 1: Nodo = Ticket | Lista = ColaTickets
         Atributos: codigo, prioridad ("critica"/"normal"), costo_hora
PUNTO 2: critica → inicio | normal → final (RECURSIVO)
PUNTO 3: costo acumulado antes de un ticket (RECURSIVO)
PUNTO 4: resolver el primer ticket
PUNTO 5: contar por prioridad (RECURSIVO) → tupla (criticos, normales)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, codigo, prioridad, costo):
        self.codigo    = codigo
        self.prioridad = prioridad   # "critica" o "normal"
        self.costo     = costo       # costo por hora de atención
        self.siguiente = None

class ColaTickets:
    def __init__(self):
        self.cabeza = None

    # ── PUNTO 2: crear ticket ─────────────────────────────────────────────────
    def crear_ticket(self, codigo, prioridad, costo):
        nuevo = Nodo(codigo, prioridad, costo)
        if prioridad == "critica":
            if self.cabeza is None or self.cabeza.prioridad == "normal":
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                self._tras_criticos(self.cabeza, nuevo)
        else:
            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                self._al_final(self.cabeza, nuevo)

    def _tras_criticos(self, actual, nuevo):
        if actual.siguiente is None or actual.siguiente.prioridad == "normal":
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._tras_criticos(actual.siguiente, nuevo)

    def _al_final(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._al_final(actual.siguiente, nuevo)

    # ── PUNTO 3: costo acumulado antes del ticket ─────────────────────────────
    def costo_antes(self, codigo):
        return self._acumular(self.cabeza, codigo, 0)

    def _acumular(self, actual, codigo, acum):
        if actual is None:
            return -1
        if actual.codigo == codigo:
            return acum
        return self._acumular(actual.siguiente, codigo, acum + actual.costo)

    # ── PUNTO 4: resolver el primero ──────────────────────────────────────────
    def resolver_siguiente(self):
        if self.cabeza is None:
            return None
        resuelto = self.cabeza
        self.cabeza = self.cabeza.siguiente
        resuelto.siguiente = None
        return resuelto

    # ── PUNTO 5: contar por prioridad ─────────────────────────────────────────
    def contar_por_prioridad(self):
        return self._contar(self.cabeza, 0, 0)

    def _contar(self, actual, criticos, normales):
        if actual is None:
            return (criticos, normales)
        if actual.prioridad == "critica":
            return self._contar(actual.siguiente, criticos + 1, normales)
        else:
            return self._contar(actual.siguiente, criticos, normales + 1)

    def mostrar(self):
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  {i}. {actual.codigo:<10} | {actual.prioridad:<8} | ${actual.costo}/hr")
            actual = actual.siguiente
            i += 1

if __name__ == "__main__":
    cola = ColaTickets()
    cola.crear_ticket("TK-001", "normal",   80000)
    cola.crear_ticket("TK-002", "critica", 150000)
    cola.crear_ticket("TK-003", "normal",   60000)
    cola.crear_ticket("TK-004", "critica", 200000)
    cola.crear_ticket("TK-005", "normal",   90000)

    print("Cola de tickets:")
    cola.mostrar()

    print(f"\nCosto antes de TK-003: ${cola.costo_antes('TK-003'):,}")
    print(f"Costo antes de TK-005: ${cola.costo_antes('TK-005'):,}")
    print(f"Ticket inexistente:    {cola.costo_antes('TK-999')}")

    crit, norm = cola.contar_por_prioridad()
    print(f"\nCríticos: {crit}, Normales: {norm}")

    print(f"\nResolviendo: {cola.resolver_siguiente().codigo}")
    print(f"Resolviendo: {cola.resolver_siguiente().codigo}")
    print("\nCola restante:")
    cola.mostrar()
