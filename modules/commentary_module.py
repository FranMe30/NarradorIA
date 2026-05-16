import random

COMMENTS = {
    "Combate": [
        "¡El jugador entra en combate con gran valentía!",
        "¡La batalla se intensifica en este momento!",
        "¡Los enemigos atacan y la tensión aumenta!"
    ],
    "Recolectando recursos": [
        "Está reuniendo materiales esenciales para sobrevivir.",
        "Cada recurso recolectado acerca al jugador a la victoria.",
        "La minería y la recolección son clave en esta aventura."
    ],
    "Exploración": [
        "Nuestro aventurero se adentra en territorios desconocidos.",
        "Explora el mundo en busca de nuevos descubrimientos.",
        "Cada paso revela secretos ocultos en Minecraft."
    ],
    "Poca vida": [
        "¡La situación es crítica, le queda muy poca vida!",
        "¡Un golpe más podría acabar con la partida!",
        "La tensión está al máximo."
    ],
    "Victoria": [
        "¡Victoria épica! El jugador ha superado el desafío.",
        "¡El esfuerzo ha dado frutos!",
        "¡Triunfo total en esta increíble aventura!"
    ],
    "Derrota": [
        "La derrota ha llegado, pero siempre hay una nueva oportunidad.",
        "El jugador ha caído en combate.",
        "Esta batalla termina en derrota."
    ]
}


def generate_comment(event: str) -> str:
    """
    Genera un comentario en español a partir del evento detectado.
    """
    options = COMMENTS.get(
        event,
        ["Se ha detectado un nuevo evento en la partida."]
    )
    return random.choice(options)