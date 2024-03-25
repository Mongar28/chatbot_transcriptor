import telebot
import os
from pydub import AudioSegment


def obtener_peso(archivo):

    bytes_tamaño = os.path.getsize(archivo)
    megabytes_tamaño = bytes_tamaño / (1024 * 1024)
    return megabytes_tamaño


def reducir_peso_mp3(archivo_original, archivo_destino, bitrate='64k'):

    # Obtiene el peso del archivo original en megabytes
    peso_original_mb = obtener_peso(archivo_original)

    # Carga el archivo MP3 original
    audio = AudioSegment.from_mp3(archivo_original)

    # Aplica el nuevo bitrate para reducir el peso
    audio.export(archivo_destino, format="mp3", bitrate=bitrate)

    # Obtiene el peso del archivo reducido en megabytes
    peso_reducido_mb = obtener_peso(archivo_destino)

    print(f"Peso del archivo original: {peso_original_mb:.2f} MB")
    print(f"Peso del archivo reducido: {peso_reducido_mb:.2f} MB")
    print(f"El archivo se ha reducido y guardado en: {archivo_destino}")


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

        file_name_r = file_name.replace('.mp3', '_r.mp3')
        file_path_r = f"audios/{file_name_r}"

        reducir_peso_mp3(file_path, file_path_r)

        # Escritura del archivo de audio para luego pasarlo a wisper
        with open(file_path_r, 'wb') as new_file:
            new_file.write(downloaded_file)

        return file_path_r

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
