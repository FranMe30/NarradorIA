from transformers import pipeline


# Cargar modelo BLIP una sola vez
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)


def classify_event(description: str) -> str:
    """
    Clasifica la descripción generada por BLIP en un evento del juego.
    """
    text = description.lower()

    combat_keywords = [
        "fight", "fighting", "battle", "attacking",
        "zombie", "skeleton", "creeper", "monster", "enemy"
    ]

    resource_keywords = [
        "mining", "mine", "stone", "tree", "wood",
        "pickaxe", "ore", "diamond", "crafting"
    ]

    victory_keywords = [
        "victory", "win", "won", "defeated dragon"
    ]

    defeat_keywords = [
        "game over", "you died", "death", "dead"
    ]

    low_health_keywords = [
        "low health", "hearts"
    ]

    if any(word in text for word in combat_keywords):
        return "Combate"

    if any(word in text for word in resource_keywords):
        return "Recolectando recursos"

    if any(word in text for word in victory_keywords):
        return "Victoria"

    if any(word in text for word in defeat_keywords):
        return "Derrota"

    if any(word in text for word in low_health_keywords):
        return "Poca vida"

    return "Exploración"


def analyze_image(image_path: str):
    """
    Analiza una imagen y devuelve:
    - descripción generada por BLIP
    - evento clasificado
    """
    result = captioner(image_path)
    description = result[0]["generated_text"]
    event = classify_event(description)

    return description, event