rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

word = input('Ingrese una palabra clave para filtrar las reglas ')

text = rules.split("\n")

rule = ""

for line in text:
    if word.lower() in line.lower():
        rule += line + "\n"

if rule == "":
    print('No se encontraron reglas con dicha palabra clave.')
else:
    print(f'Reglas filtradas por la palabra clave {word}')
    print(rule)

