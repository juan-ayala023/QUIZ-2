"""
═══════════════════════════════════════════════════════════════════════════════
                    HOJA DE REFERENCIA RÁPIDA — QUIZ
                    "Si el profesor dice X → tú haces Y"
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 1 — AGREGAR / INSERTAR
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "agregar", "insertar", "registrar", "inscribir", "añadir"
# → usar agregar() que llama a _pertenece() primero para no duplicar

def agregar(self, x):
    if self._pertenece(self.cabeza, x):   # <-- SIEMPRE verificar duplicado primero
        return False
    nuevo = Nodo(x)
    nuevo.siguiente = self.cabeza         # enganchar al inicio
    self.cabeza = nuevo
    return True

# Si dice: "insertar al INICIO" (preferenciales, premium, urgente, primera clase)
# → nuevo apunta a cabeza, cabeza apunta a nuevo
def _insertar_inicio(self, nuevo):
    nuevo.siguiente = self.cabeza
    self.cabeza = nuevo

# Si dice: "insertar al FINAL" (normales, básica, económica)
# → recursión hasta encontrar el último nodo
def _insertar_final(self, actual, nuevo):
    if actual.siguiente is None:          # llegamos al último
        actual.siguiente = nuevo
    else:
        self._insertar_final(actual.siguiente, nuevo)


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 2 — BUSCAR / VERIFICAR SI EXISTE
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "verificar si existe", "buscar", "pertenece", "está en el conjunto"
# → _pertenece() recursivo, retorna True/False

def _pertenece(self, actual, x):
    if actual is None:        # caso base 1: llegó al final sin encontrar
        return False
    if actual.dato == x:      # caso base 2: lo encontró
        return True
    return self._pertenece(actual.siguiente, x)

# Si dice: "verificar si el usuario PUEDE hacer algo" (permisos)
# → es_subconjunto: todos los requeridos deben estar en los del usuario
def _tiene_acceso(self, actual_requerido):
    if actual_requerido is None:                              # revisé todos → sí puede
        return True
    if not self._pertenece(self.cabeza, actual_requerido.dato):  # falta uno → no puede
        return False
    return self._tiene_acceso(actual_requerido.siguiente)


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 3 — CALCULAR / ACUMULAR ANTES DE UN ELEMENTO
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "tiempo de espera", "costo acumulado", "peso antes de",
#          "cuánto falta", "días que esperó"
# → _acumular() recursivo, suma el valor de cada nodo ANTES del buscado

def _acumular(self, actual, buscado, acum):
    if actual is None:             # caso base 1: no estaba en la lista
        return -1
    if actual.nombre == buscado:   # caso base 2: lo encontramos → retornar lo acumulado
        return acum
    return self._acumular(         # caso recursivo: sumar y seguir
        actual.siguiente,
        buscado,
        acum + actual.valor        # cambiar .valor por .tiempo / .precio / .peso / .dias
    )


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 4 — CONTAR
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "contar cuántos hay", "cardinalidad", "total de elementos"
# → _contar_rec() acumula 1 por cada nodo

def _contar_rec(self, actual):
    if actual is None:
        return 0
    return 1 + self._contar_rec(actual.siguiente)

# Si dice: "contar por tipo", "cuántos son X y cuántos son Y"
# → retorna TUPLA (tipo_A, tipo_B), dos contadores que suben por separado

def _contar_por_tipo(self, actual, cuenta_A, cuenta_B):
    if actual is None:
        return (cuenta_A, cuenta_B)             # caso base: retornar la tupla
    if actual.tipo == "tipo_A":                 # cambiar por "preferencial"/"premium"/etc.
        return self._contar_por_tipo(actual.siguiente, cuenta_A + 1, cuenta_B)
    else:
        return self._contar_por_tipo(actual.siguiente, cuenta_A, cuenta_B + 1)


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 5 — RETIRAR / ATENDER / DESPACHAR EL PRIMERO
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "atender", "despachar", "retirar", "procesar", "abordar", "resolver"
# → sacar la cabeza (NO es recursivo, son 4 líneas)

def atender_siguiente(self):
    if self.cabeza is None:
        return None
    atendido = self.cabeza                  # guardar referencia al primero
    self.cabeza = self.cabeza.siguiente     # el segundo pasa a ser el primero
    atendido.siguiente = None               # desconectar el nodo retirado
    return atendido                         # retornarlo para usarlo afuera


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 6 — OPERACIONES ENTRE DOS CONJUNTOS
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "canciones en común", "estudiantes en ambas", "permisos compartidos"
# → INTERSECCIÓN: recorrer A, guardar los que también están en B

def _interseccion_rec(self, actual, otro, resultado):
    if actual is None:
        return
    if otro._pertenece(otro.cabeza, actual.dato):   # ¿está en los dos?
        resultado.agregar(actual.dato)
    self._interseccion_rec(actual.siguiente, otro, resultado)

# Si dice: "sugerencias", "solo tiene uno", "exclusivo de A", "no está en B"
# → DIFERENCIA: recorrer A, guardar los que NO están en B

def _diferencia_rec(self, actual, otro, resultado):
    if actual is None:
        return
    if not otro._pertenece(otro.cabeza, actual.dato):   # ¿NO está en B?
        resultado.agregar(actual.dato)
    self._diferencia_rec(actual.siguiente, otro, resultado)

# Si dice: "catálogo combinado", "todos los estudiantes", "unión"
# → UNIÓN: copiar A al resultado, luego copiar B (agregar ignora duplicados)

def _copiar_rec(self, actual, destino):
    if actual is None:
        return
    destino.agregar(actual.dato)
    self._copiar_rec(actual.siguiente, destino)

# uso: self._copiar_rec(A.cabeza, resultado)
#      self._copiar_rec(B.cabeza, resultado)


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 7 — MÁXIMO Y MÍNIMO (si los datos son numéricos)
# ═══════════════════════════════════════════════════════════════════════════════

# Si dice: "el mayor", "el más caro", "el más pesado", "el máximo"
def _maximo_rec(self, actual, maximo_hasta_ahora):
    if actual is None:
        return maximo_hasta_ahora
    nuevo_max = actual.dato if actual.dato > maximo_hasta_ahora else maximo_hasta_ahora
    return self._maximo_rec(actual.siguiente, nuevo_max)
# llamar con: self._maximo_rec(self.cabeza, self.cabeza.dato)

# Si dice: "el menor", "el más barato", "el más liviano", "el mínimo"
def _minimo_rec(self, actual, minimo_hasta_ahora):
    if actual is None:
        return minimo_hasta_ahora
    nuevo_min = actual.dato if actual.dato < minimo_hasta_ahora else minimo_hasta_ahora
    return self._minimo_rec(actual.siguiente, nuevo_min)
# llamar con: self._minimo_rec(self.cabeza, self.cabeza.dato)


# ═══════════════════════════════════════════════════════════════════════════════
# BLOQUE 8 — TABLA RESUMEN: qué cambia entre parcial y parcial
# ═══════════════════════════════════════════════════════════════════════════════

"""
┌─────────────────────┬──────────────────┬───────────────┬──────────────────────┐
│ Contexto            │ Nodo (elemento)  │ Tipo A→inicio │ Valor acumulado      │
├─────────────────────┼──────────────────┼───────────────┼──────────────────────┤
│ Banco               │ Cliente          │ preferencial  │ .tiempo (min)        │
│ Hospital            │ Paciente         │ urgente       │ .gravedad            │
│ Gimnasio            │ Turno            │ premium       │ .duracion (min)      │
│ Aeropuerto          │ Pasajero         │ primera       │ .peso (kg)           │
│ Restaurante         │ Pedido           │ express       │ .precio ($)          │
│ Soporte técnico     │ Ticket           │ critica       │ .costo ($)           │
│ Biblioteca          │ Libro            │ digital       │ .dias                │
├─────────────────────┼──────────────────┼───────────────┼──────────────────────┤
│ Spotify             │ Cancion          │ (no aplica)   │ intersección/dif     │
│ Universidad         │ Estudiante       │ (no aplica)   │ intersección/dif     │
│ Seguridad           │ Permiso          │ (no aplica)   │ subconjunto          │
└─────────────────────┴──────────────────┴───────────────┴──────────────────────┘

LO QUE NUNCA CAMBIA (memorizar una vez):
  - Estructura del Nodo: dato(s) + self.siguiente = None
  - Estructura de la Lista/Cola/Conjunto: self.cabeza = None
  - _insertar_final: if actual.siguiente is None → insertar, else → recursión
  - _acumular: if None → -1, if encontrado → acum, else → acum + valor
  - _contar_por_tipo: if None → (a, b), if tipo_A → (a+1, b), else → (a, b+1)
  - atender_siguiente: 4 líneas, NUNCA recursivo
"""
