"""
SEMANA 7 - CONJUNTOS EN PYTHON
================================
Operaciones fundamentales con sets nativos
"""

# ─── CREAR CONJUNTOS ──────────────────────────────────────────────────────────

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
vacio = set()          # IMPORTANTE: {} crea un dict, no un set vacío

# ─── OPERACIONES BÁSICAS ─────────────────────────────────────────────────────

print("A =", A)
print("B =", B)

# Unión: todo lo de A y B sin repetir
print("\nA | B =", A | B)          # {1, 2, 3, 4, 5, 6}

# Intersección: solo lo que está en AMBOS
print("A & B =", A & B)            # {3, 4}

# Diferencia: lo de A que NO está en B
print("A - B =", A - B)            # {1, 2}
print("B - A =", B - A)            # {5, 6}

# Diferencia simétrica: lo que está en uno pero NO en los dos
print("A ^ B =", A ^ B)            # {1, 2, 5, 6}

# ─── RELACIONES ──────────────────────────────────────────────────────────────

C = {3, 4}
print("\nC =", C)
print("C <= A (subconjunto):", C <= A)       # True
print("C < A  (subconjunto propio):", C < A) # True (C ≠ A)
print("A <= A:", A <= A)                      # True
print("A < A:", A < A)                        # False (mismo conjunto)
print("A == B:", A == B)                      # False

# ─── MÉTODOS EQUIVALENTES ────────────────────────────────────────────────────

print("\n--- Mismas ops con métodos ---")
print("union:", A.union(B))
print("intersection:", A.intersection(B))
print("difference:", A.difference(B))
print("symmetric_difference:", A.symmetric_difference(B))
print("issubset:", C.issubset(A))
print("issuperset:", A.issuperset(C))
print("isdisjoint:", A.isdisjoint({7, 8}))   # True: no comparten nada

# ─── OPERACIONES DE MODIFICACIÓN ─────────────────────────────────────────────

S = {1, 2, 3}
S.add(4)            # agrega un elemento
S.add(2)            # no hace nada (ya existe)
S.remove(1)         # elimina (error si no existe)
S.discard(99)       # elimina sin error si no existe
print("\nS modificado:", S)

# ─── ÍNDICE DE JACCARD ───────────────────────────────────────────────────────
# Mide similitud entre dos conjuntos: |A∩B| / |A∪B|
# Resultado entre 0.0 (nada en común) y 1.0 (idénticos)

def jaccard(A, B):
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)

g1 = {"acción", "thriller", "drama"}
g2 = {"acción", "thriller"}
print(f"\nJaccard({g1}, {g2}) = {jaccard(g1, g2):.2f}")  # 0.67

# ─── PERTENENCIA Y CARDINALIDAD ──────────────────────────────────────────────

print("\n3 in A:", 3 in A)     # True
print("9 in A:", 9 in A)       # False
print("|A| =", len(A))         # 4
