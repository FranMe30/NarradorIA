import cv2
import os


def extract_frames(video_path, output_folder="assets/frames", interval_seconds=2):
    """
    Extrae un frame del video cada cierto número de segundos.

    Args:
        video_path (str): Ruta del archivo de video.
        output_folder (str): Carpeta donde se guardarán los frames.
        interval_seconds (int): Intervalo en segundos entre frames.

    Returns:
        list[str]: Lista de rutas de los frames guardados.
    """

    # Crear carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Limpiar frames anteriores
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Abrir video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"No se pudo abrir el video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        raise ValueError("No se pudo obtener el FPS del video.")

    frame_interval = int(fps * interval_seconds)

    frame_count = 0
    saved_count = 0
    saved_frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            filename = f"frame_{saved_count:03d}.jpg"
            filepath = os.path.join(output_folder, filename)

            cv2.imwrite(filepath, frame)

            saved_frames.append(filepath)
            saved_count += 1

        frame_count += 1

    cap.release()

    return saved_frames