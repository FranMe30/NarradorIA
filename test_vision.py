from modules.vision_module import analyze_image

# Usaremos el primer frame extraído en el Día 2
image_path = "assets/frames/frame_006.jpg"

description, event = analyze_image(image_path)

print("Descripción generada por BLIP:")
print(description)

print("\nEvento clasificado:")
print(event)