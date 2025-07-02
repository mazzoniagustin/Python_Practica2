descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]

keywords = ["entretenimiento" , "música", "charla"]

count = {"entretenimiento": 0, "música": 0, "charla": 0}

for description in descriptions:
    description = description.lower()
    for word in keywords:
        line = description.split()
        if word in line:
            count[word] += 1
print(f'Menciones de charla {count["charla"]}')
print(f'Menciones de música {count["música"]}')
print(f'Menciones de entretenimiento {count["entretenimiento"]}')
