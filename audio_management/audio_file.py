import telebot


def file_audio(message, bot, type_file):
    # Si el audio es un archivo
    # Descarga delarchivo de audio

    if type_file == 'audio':
        file_name: str = message.audio.file_name
        file_path: str = f"audios/{file_name}"
        file_info: str = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Escritura del archivo de audio para luego pasarlo a wisper
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            bot.send_message(
                message.chat.id, "Se ha creado el archivo de audio")

        return file_path

    elif type_file == 'voice':
        # Descarga delarchivo de audio
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # pasamos el archvio de audio al modelo de wisper
        file_path: str = "audios/nota_de_voz.ogg"

        # Escritura del archivo de audio para luego pasarlo a wisper
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        return file_path
