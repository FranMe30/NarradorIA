from modules.tts_module import text_to_speech

text = "¡La batalla se intensifica y el jugador lucha con valentía!"

audio_path = text_to_speech(text)

print("Audio generado en:")
print(audio_path)