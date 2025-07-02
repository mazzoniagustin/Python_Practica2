titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

max_lenght_title = ""
max_words = 0

for title in titles:
    words = title.split()
    lenght = len(words)
    if lenght > max_words:
        max_words = lenght
        max_lenght_title = title
        
print(f'El titulo más largo es: {max_lenght_title}')