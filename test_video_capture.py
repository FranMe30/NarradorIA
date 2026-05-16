from modules.video_capture import extract_frames

# Cambia el nombre si tu video tiene otro nombre
video_path = "assets/input_videos/minecraft.mp4"

frames = extract_frames(video_path)

print("Frames extraídos:")
for frame in frames:
    print(frame)

print(f"\nTotal de frames guardados: {len(frames)}")