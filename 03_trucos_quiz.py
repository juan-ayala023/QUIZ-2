"""
TRUCOS Y ERRORES COMUNES — CONJUNTOS
======================================
Lo que más sale en quizzes y exámenes.
"""

# ══════════════════════════════════════════════════════════════════
# TRUCO 1: {} crea dict, NO set
# ══════════════════════════════════════════════════════════════════

malo  = {}          # esto es un diccionario vacío
bueno = set()       # así se crea un conjunto vacío

print(type(malo))   # <class 'dict'>
print(type(bueno))  # <class 'set'>


# ══════════════════════════════════════════════════════════════════
# TRUCO 2: A - B no es lo mismo que B - A
# ══════════════════════════════════════════════════════════════════

A = {1, 2, 3}
B = {2, 3, 4}

print(A - B)   # {1}    — lo de A que no está en B
print(B - A)   # {4}    — lo de B que no está en A
print(A ^ B)   # {1, 4} — cualquiera de los dos, pero no ambos


# ══════════════════════════════════════════════════════════════════
# TRUCO 3: subconjunto vs subconjunto PROPIO
# ══════════════════════════════════════════════════════════════════

X = {1, 2}
Y = {1, 2, 3}

print(X <= Y)   # True  — X ⊆ Y (subconjunto, puede ser igual)
print(X < Y)    # True  — X ⊂ Y (subconjunto propio, X ≠ Y)
print(Y <= Y)   # True  — todo conjunto es subconjunto de sí mismo
print(Y < Y)    # False — NO es subconjunto propio de sí mismo


# ══════════════════════════════════════════════════════════════════
# TRUCO 4: verificar permisos con subconjunto (caso seguridad)
# ══════════════════════════════════════════════════════════════════

permisos_usuario = {"leer", "escribir", "ver_logs"}

accion_simple    = {"leer"}
accion_multiple  = {"leer", "eliminar"}

# ¿El usuario tiene TODOS los permisos requeridos?
print(accion_simple   <= permisos_usuario)   # True  ✓
print(accion_multiple <= permisos_usuario)   # False ✗ (no tiene "eliminar")


# ══════════════════════════════════════════════════════════════════
# TRUCO 5: iterar y operar conjuntos en loops
# ══════════════════════════════════════════════════════════════════

catalogo = {
    "Matrix":      {"acción", "sci-fi"},
    "Titanic":     {"romance", "drama"},
    "Avengers":    {"acción", "aventura"},
}
favoritos = {"acción", "sci-fi"}

for pelicula, generos in catalogo.items():
    comunes = generos & favoritos               # intersección
    if comunes:
        puntaje = len(comunes) / len(favoritos) # % de coincidencia
        print(f"{pelicula}: {puntaje:.0%}")


# ══════════════════════════════════════════════════════════════════
# TRUCO 6: acumular unión de muchos conjuntos
# ══════════════════════════════════════════════════════════════════

materias = {
    "Ana":   {"Algoritmos", "Redes"},
    "Carlos": {"Algoritmos", "BD"},
    "Diana":  {"Redes", "BD"},
}

todos_los_cursos = set()
for cursos in materias.values():
    todos_los_cursos = todos_los_cursos | cursos  # ir acumulando

print(todos_los_cursos)  # {'Algoritmos', 'Redes', 'BD'}


# ══════════════════════════════════════════════════════════════════
# TRUCO 7: Jaccard — similitud entre 0 y 1
# ══════════════════════════════════════════════════════════════════
# 0.0 = nada en común, 1.0 = idénticos
# Si Jaccard > 0.6 en textos → probable copia

def jaccard(A, B):
    if not A and not B:
        return 1.0
    interseccion = len(A & B)
    union = len(A | B)
    return interseccion / union

print(jaccard({1,2,3}, {1,2,3}))    # 1.0
print(jaccard({1,2,3}, {4,5,6}))    # 0.0
print(jaccard({1,2,3}, {2,3,4}))    # 0.5


# ══════════════════════════════════════════════════════════════════
# TRUCO 8: en lista enlazada, SIEMPRE verificar pertenece() antes de agregar
# ══════════════════════════════════════════════════════════════════
# Sin esta verificación, el conjunto puede tener duplicados.
# La función pertenece() es la base de todo: agregar, unión, etc.
