import telebot


class BotMessages():
    # This class holds messages as attributes

    welcome: str = """
    🤖 *¡Bienvenido al Bot de la línea!* 🤖
    🧠🐝 **Territorios Inteligentes** 🐝🧠​ \n
    Este bot está en desarrollo, pero por ahora,
    puedes transcribir archivos de audio o notas de voz.
    """

    instructions: str = """
    🎧⌨️✍ Para transcribir, simplemente sigue estos pasos: envía una nota de voz o un archivo de audio y ten en cuenta lo siguiente:\n\n
    ✅ El archivo de audio no puede pesar más de 20 MB \n
    ✅ El archivo de audio no puede exceder los 30 minutos \n
    ✅ El bot funcionará mejor si la voz en el audio es clara y comprensible.\n
    ✅ En última instancia, el bot devolverá un archivo de Word que contiene el texto de la transcripción.\n
    ✅ Cuanto más largo sea el audio, más tiempo tomará la respuesta.\n"""

    def file_waiting_message(self,
                             file_name: str,
                             file_size: str,
                             file_duration: str) -> str:
        file_size = file_size / (1024 * 1024)
        waiting_message: str = f"""
        Tu audio se esta procesando y puede tardar un poco.\n\n🅣🅡🅐🅝🅢🅒🅡🅘🅑🅘🅔🅝🅓🅞...🎧⌨️⌛\n\n
        📁 𝗡𝗼𝗺𝗯𝗿𝗲 𝗱𝗲𝗹 𝗮𝗿𝗰𝗵𝗶𝘃𝗼:
        {file_name}
        📏 𝗧𝗮𝗺𝗮𝗻̃𝗼:{file_size:.2f} MB
        ⏳ 𝗗𝘂𝗿𝗮𝗰𝗶𝗼́𝗻:{file_duration} Segundos.
        \n\n\n
        """

        return waiting_message

    def voice_waiting_message(self, message) -> str:

        voice_size = message.voice.file_size
        voice_size = voice_size / (1024 * 1024)
        waiting_message: str = f"""
        Tu audio se está procesando y puede tardar un poco.\n\n🅣🅡🅐🅝🅢🅒🅡🅘🅑🅘🅔🅝🅓🅞...🎧⌨️⌛\n\n
        📁 Nombre del archivo: nota_de_voz
        📏 Tamaño del archivo: {voice_size:.2f} MB
        ⏳ Duración: {message.voice.duration} Segundos.
        \n\n\n
        """

        return waiting_message
