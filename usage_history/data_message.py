from datetime import datetime


def info_massage(message, type_document: str):

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime(
        "%d-%m-%Y %H:%M")  # Formato DD-MM-YYYY HH:MM

    if type_document == "audio":

        # Se hace la conversion de B a M
        file_size = message.audio.file_size
        file_size = file_size / (1024 * 1024)
        file_size = f"{file_size:.2f} MB"

        data_message = {
            "username": message.from_user.first_name,
            "document_name": message.audio.file_name,
            "audio_duration": message.audio.duration,
            "audio_size": file_size,
            "date": fecha_actual
        }
    elif type_document == "voice":

        voice_size = message.voice.file_size
        voice_size = voice_size / (1024 * 1024)
        voice_size = f"{voice_size:.2f} MB"

        data_message = {
            "username": message.from_user.first_name,
            "document_name": "nota_voz",
            "audio_duration": message.voice.duration,
            "audio_size": voice_size,
            "date": fecha_actual
        }

    return data_message
