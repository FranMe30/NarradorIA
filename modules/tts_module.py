from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf
import os

# Modelo de texto a voz en español
MODEL_NAME = "facebook/mms-tts-spa"

print("Cargando modelo TTS en español...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = VitsModel.from_pretrained(MODEL_NAME)
print("Modelo TTS cargado correctamente.")

def text_to_speech(text, output_path="assets/output_audio/commentary.wav"):
    """
    Convierte texto en español a un archivo de audio WAV.
    
    Args:
        text (str): Texto a convertir en voz.
        output_path (str): Ruta donde se guardará el archivo.
    
    Returns:
        str: Ruta del archivo de audio generado.
    """

    # Crear la carpeta de salida si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Tokenizar el texto
    inputs = tokenizer(text, return_tensors="pt")

    # Generar audio
    with torch.no_grad():
        output = model(**inputs).waveform

    # Convertir tensor a arreglo NumPy de una dimensión
    audio = output.squeeze().cpu().numpy()

    # Guardar archivo WAV
    sf.write(
        file=output_path,
        data=audio,
        samplerate=model.config.sampling_rate,
        format="WAV"
    )

    return output_path