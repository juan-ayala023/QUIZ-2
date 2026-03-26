catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"romance", "drama", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}

peliculas_con_generos_en_comun = []
peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]

        if len(comunes) >= 2:
            peliculas_con_generos_en_comun.append((p1, p2, sorted(comunes)))

print(peliculas_con_generos_en_comun)

favoritos = {"acción", "crimen", "aventura"}
recomendaciones=[]

for pelicula, generos in catalogo.items():
    generos_comunes= favoritos.intersection(generos)
    if generos_comunes:
        porcentaje_similitud=(len(generos_comunes)/len(favoritos))*100
        recomendaciones.append(pelicula, porcentaje_similitud)

def obtener_porcentaje(elemento):
    return elemento[1]

recomendaciones.sort(key=obtener_porcentaje, reverse=True)
print(recomendaciones)

generos_unicos = set()

for generos in catalogo.values():
    generos_unicos = genero_unicos.union(generos)

generos_ordenados = sorted(generos_unicos)

print(generos_ordenados)



peliculas_por_genero= {}

for pelicula, generos in catalogo.items():
    for genero in generos:
        if genero not in peliculas_por_genero:
            peliculas_por_genero[genero] = set()

        peliculas_por_genero[genero].add(pelicula)
print(peliculas_por_genero)

#Metodo que reciba dos películas
#Devuelva el índice de similitud Jaccard 
def calcular_indice(p1, p2):

    g1 = catalogo[p1]
    g2 = catalogo[p2]

    interseccion = len(g1 & g2)
    union = len(g1 | g2)

    return interseccion / union 

#Leer dos textos
#Calcular su indice de similitud ignorando las STOPWORDS
#Si el índice es mayor a 0.6, se copiaron


STOPWORDS = {"el", "la", "los", "las", "un", "una", "unos", "unas",
            "de", "del", "al", "a", "en", "con", "por", "para",
            "y", "o", "que", "es", "son", "se", "su", "sus",
            "como", "pero", "más", "este", "esta", "estos", "estas"}
        
def limpiar_texto(texto):
    return set(texto.lower().split())- STOPWORDS

def detectar_copia(texto1, texto2):
    palabras1=limpiar_texto(texto1)
    palabras2=limpiar_texto(texto2)

    interseccion= palabras1.intersection(palabras2)
    union= palabras1.union(palabras2)

    if not union:
        return 0.0

    indice=len(interseccion)/len(union)

    if indice > 0.6:
        print(f"Se copiaron. Indice : {indice:.2f}")
    else:
        print(f"No se copiaron. Indice : {indice:.2f}")

    return indice




