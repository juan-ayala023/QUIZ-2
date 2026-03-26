"""
═══════════════════════════════════════════════════════════════════════════════
                    POSIBLE PARCIAL — Gimnasio FitLife
                    Lista de Espera para Máquinas
═══════════════════════════════════════════════════════════════════════════════
PUNTO 1: Nodo = Turno | Lista = ListaEspera
         Atributos: nombre, membresia (premium/basica), duracion (minutos)
PUNTO 2: premium → inicio | basica → final (RECURSIVO)
PUNTO 3: minutos acumulados antes de un usuario (RECURSIVO)
PUNTO 4: asignar la máquina al primero de la lista
PUNTO 5: contar por membresía (RECURSIVO) → tupla (premium, basica)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, nombre, membresia, duracion):
        self.nombre    = nombre
        self.membresia = membresia   # "premium" o "basica"
        self.duracion  = duracion    # minutos en máquina
        self.siguiente = None

class ListaEspera:
    def __init__(self):
        self.cabeza = None

    # ── PUNTO 2: agregar turno ────────────────────────────────────────────────
    def agregar_turno(self, nombre, membresia, duracion):
        nuevo = Nodo(nombre, membresia, duracion)
        if membresia == "premium":
            if self.cabeza is None or self.cabeza.membresia == "basica":
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                self._tras_premium(self.cabeza, nuevo)
        else:
            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                self._al_final(self.cabeza, nuevo)

    def _tras_premium(self, actual, nuevo):
        if actual.siguiente is None or actual.siguiente.membresia == "basica":
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._tras_premium(actual.siguiente, nuevo)

    def _al_final(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._al_final(actual.siguiente, nuevo)

    # ── PUNTO 3: minutos de espera antes del usuario ──────────────────────────
    def minutos_espera(self, nombre):
        return self._acumular(self.cabeza, nombre, 0)

    def _acumular(self, actual, nombre, acum):
        if actual is None:
            return -1
        if actual.nombre == nombre:
            return acum
        return self._acumular(actual.siguiente, nombre, acum + actual.duracion)

    # ── PUNTO 4: asignar máquina al primero ───────────────────────────────────
    def asignar_maquina(self):
        if self.cabeza is None:
            return None
        asignado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        asignado.siguiente = None
        return asignado

    # ── PUNTO 5: contar por membresía ─────────────────────────────────────────
    def contar_por_membresia(self):
        return self._contar(self.cabeza, 0, 0)

    def _contar(self, actual, premium, basica):
        if actual is None:
            return (premium, basica)
        if actual.membresia == "premium":
            return self._contar(actual.siguiente, premium + 1, basica)
        else:
            return self._contar(actual.siguiente, premium, basica + 1)

    def mostrar(self):
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  {i}. {actual.nombre:<12} | {actual.membresia:<8} | {actual.duracion} min")
            actual = actual.siguiente
            i += 1

if __name__ == "__main__":
    lista = ListaEspera()
    lista.agregar_turno("Pedro",   "basica",   30)
    lista.agregar_turno("Sofia",   "premium",  45)
    lista.agregar_turno("Miguel",  "basica",   20)
    lista.agregar_turno("Laura",   "premium",  60)
    lista.agregar_turno("Andres",  "basica",   25)

    print("Lista de espera:")
    lista.mostrar()

    print(f"\nEspera de Miguel:  {lista.minutos_espera('Miguel')} min")
    print(f"Espera de Andres:  {lista.minutos_espera('Andres')} min")
    print(f"Usuario inexistente: {lista.minutos_espera('Nadie')}")

    pre, bas = lista.contar_por_membresia()
    print(f"\nPremium: {pre}, Básica: {bas}")

    print(f"\nAsignando máquina a: {lista.asignar_maquina().nombre}")
    print("\nLista restante:")
    lista.mostrar()
