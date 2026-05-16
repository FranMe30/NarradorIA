from modules.commentary_module import generate_comment

# Prueba con distintos eventos
events = [
    "Combate",
    "Exploración",
    "Recolectando recursos",
    "Poca vida",
    "Victoria",
    "Derrota"
]

for event in events:
    print(f"\n=== {event} ===")
    comment = generate_comment(event)
    print(comment)