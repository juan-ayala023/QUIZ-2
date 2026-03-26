"""
═══════════════════════════════════════════════════════════════════════════════
                    POSIBLE PARCIAL — Aeropuerto
                    Sistema de Abordaje de Vuelo
═══════════════════════════════════════════════════════════════════════════════
PUNTO 1: Nodo = Pasajero | Lista = FilaAbordaje
         Atributos: nombre, clase ("primera"/"economica"), peso_equipaje (kg)
PUNTO 2: primera clase → inicio | economica → final (RECURSIVO)
PUNTO 3: peso acumulado de equipaje antes de un pasajero (RECURSIVO)
PUNTO 4: abordar al siguiente pasajero
PUNTO 5: contar por clase (RECURSIVO) → tupla (primera, economica)
═══════════════════════════════════════════════════════════════════════════════
"""

class Nodo:
    def __init__(self, nombre, clase, peso):
        self.nombre = nombre
        self.clase  = clase    # "primera" o "economica"
        self.peso   = peso     # kg de equipaje
        self.siguiente = None

class FilaAbordaje:
    def __init__(self):
        self.cabeza = None

    # ── PUNTO 2: registrar pasajero ───────────────────────────────────────────
    def registrar_pasajero(self, nombre, clase, peso):
        nuevo = Nodo(nombre, clase, peso)
        if clase == "primera":
            if self.cabeza is None or self.cabeza.clase == "economica":
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
            else:
                self._tras_primera(self.cabeza, nuevo)
        else:
            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                self._al_final(self.cabeza, nuevo)

    def _tras_primera(self, actual, nuevo):
        if actual.siguiente is None or actual.siguiente.clase == "economica":
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._tras_primera(actual.siguiente, nuevo)

    def _al_final(self, actual, nuevo):
        if actual.siguiente is None:
            actual.siguiente = nuevo
        else:
            self._al_final(actual.siguiente, nuevo)

    # ── PUNTO 3: peso acumulado antes del pasajero ────────────────────────────
    def peso_antes(self, nombre):
        return self._acumular(self.cabeza, nombre, 0)

    def _acumular(self, actual, nombre, acum):
        if actual is None:
            return -1
        if actual.nombre == nombre:
            return acum
        return self._acumular(actual.siguiente, nombre, acum + actual.peso)

    # ── PUNTO 4: abordar al primero ───────────────────────────────────────────
    def abordar_siguiente(self):
        if self.cabeza is None:
            return None
        abordado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        abordado.siguiente = None
        return abordado

    # ── PUNTO 5: contar por clase ─────────────────────────────────────────────
    def contar_por_clase(self):
        return self._contar(self.cabeza, 0, 0)

    def _contar(self, actual, primera, economica):
        if actual is None:
            return (primera, economica)
        if actual.clase == "primera":
            return self._contar(actual.siguiente, primera + 1, economica)
        else:
            return self._contar(actual.siguiente, primera, economica + 1)

    def mostrar(self):
        actual = self.cabeza
        i = 1
        while actual:
            print(f"  {i}. {actual.nombre:<12} | {actual.clase:<10} | {actual.peso} kg")
            actual = actual.siguiente
            i += 1

if __name__ == "__main__":
    fila = FilaAbordaje()
    fila.registrar_pasajero("Carlos",   "economica", 23)
    fila.registrar_pasajero("Isabella", "primera",   32)
    fila.registrar_pasajero("Diego",    "economica", 18)
    fila.registrar_pasajero("Valentina","primera",   28)
    fila.registrar_pasajero("Santiago", "economica", 20)

    print("Fila de abordaje:")
    fila.mostrar()

    print(f"\nPeso antes de Diego:    {fila.peso_antes('Diego')} kg")
    print(f"Peso antes de Santiago: {fila.peso_antes('Santiago')} kg")
    print(f"Pasajero inexistente:   {fila.peso_antes('Nadie')}")

    pri, eco = fila.contar_por_clase()
    print(f"\nPrimera clase: {pri}, Económica: {eco}")

    print(f"\nAbordando: {fila.abordar_siguiente().nombre}")
    print(f"Abordando: {fila.abordar_siguiente().nombre}")
    print("\nFila restante:")
    fila.mostrar()
