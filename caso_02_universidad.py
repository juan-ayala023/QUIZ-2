"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 2: UNIVERSIDAD - CRUCE DE HORARIOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad necesita un sistema para analizar la matrícula de estudiantes.
Dados los estudiantes inscritos en diferentes materias, el sistema debe:

1. Encontrar estudiantes que cursan ambas materias (para evitar cruces)
2. Encontrar estudiantes que solo cursan una materia
3. Total de estudiantes únicos entre todas las materias
4. Verificar si todos los de una materia están en otra
5. Encontrar estudiantes que cursan las 3 materias

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Ivan"
}

bases_datos = {
    "Carlos", "Diana", "Juan", "Karen",
    "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen",
    "Natalia", "Oscar", "Ivan"
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   UNIVERSIDAD - CRUCE DE HORARIOS")
print("=" * 60)

print(f"\nAlgoritmos ({len(algoritmos)}): {sorted(algoritmos)}")
print(f"Bases de Datos ({len(bases_datos)}): {sorted(bases_datos)}")
print(f"Redes ({len(redes)}): {sorted(redes)}")

# 1. Estudiantes en Algoritmos Y Bases de Datos (posible cruce)
cruce_alg_bd = algoritmos & bases_datos
print(f"\n1. Cursan Algoritmos Y Bases de Datos: {sorted(cruce_alg_bd)}")

cruce_alg_redes = algoritmos & redes
print(f"   Cursan Algoritmos Y Redes: {sorted(cruce_alg_redes)}")

cruce_bd_redes = bases_datos & redes
print(f"   Cursan Bases de Datos Y Redes: {sorted(cruce_bd_redes)}")

# 2. Estudiantes que SOLO cursan una materia
solo_algoritmos = algoritmos - bases_datos - redes
solo_bd = bases_datos - algoritmos - redes
solo_redes = redes - algoritmos - bases_datos

print(f"\n2. Solo Algoritmos: {sorted(solo_algoritmos)}")
print(f"   Solo Bases de Datos: {sorted(solo_bd)}")
print(f"   Solo Redes: {sorted(solo_redes)}")

# 3. Total de estudiantes únicos
todos = algoritmos | bases_datos | redes
print(f"\n3. Total estudiantes únicos: {len(todos)}")
print(f"   Estudiantes: {sorted(todos)}")

# 4. ¿Todos los de Algoritmos están en Bases de Datos?
print(f"\n4. ¿Algoritmos ⊆ Bases de Datos? {algoritmos <= bases_datos}")
print(f"   ¿Cruce Alg-BD ⊆ Algoritmos? {cruce_alg_bd <= algoritmos}")

# 5. Estudiantes en las 3 materias
en_las_tres = algoritmos & bases_datos & redes
print(f"\n5. Cursan las 3 materias: {sorted(en_las_tres)}")

# Bonus: Resumen por estudiante
print("\n" + "=" * 60)
print("RESUMEN POR ESTUDIANTE")
print("=" * 60)
for estudiante in sorted(todos):
    materias = []
    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in bases_datos:
        materias.append("BD")
    if estudiante in redes:
        materias.append("Redes")
    print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")
