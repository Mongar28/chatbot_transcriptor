import telebot
from messages.messages import BotMessages
from audio_management.audio_file import file_audio
from api_openai.whisper import whisper_api
from dotenv import load_dotenv
import os


# Configuración del bot
# Cargarmos la varible de entorno desde el archivo .env que contine el api_token del bot
load_dotenv()

API_TOKEN_BOT: str = os.getenv("API_TOKEN_BOT")
bot = telebot.TeleBot(API_TOKEN_BOT)

# Inicializamos la clase BotMessages la cual contiene los mensajes que se enviaran al los usuarios
botMessages = BotMessages()

# Handle '/start' and '/help'


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, botMessages.welcome, parse_mode="Markdown")
    bot.reply_to(message, botMessages.instructions, parse_mode="Markdown")


# Transcripción del audio y envio del archivo
@bot.message_handler(content_types=["text", "audio", "voice"],)
def bot_mensajes_texto(message):
    # Si el audio es un archivo
    if message.audio:

        waiting_message = botMessages.file_waiting_message(
            message.audio.file_name,
            message.audio.file_size,
            message.audio.duration
        )

        print(waiting_message)
        user_name = message.from_user.first_name
        print(f"se esta procesando el audio de: {user_name}")

        # Imprimimos el mensaje de espera
        bot.send_message(message.chat.id, waiting_message)

        # Abrimos el archivo y lo enviamos
        bot.send_chat_action(message.chat.id, "upload_document")

        # Ejecutamos la funcion que descarga el archvio de auio y retorno file_name dond ese encuentra
        file_path: str = file_audio(message, bot, "audio")

    # En caso de que sea un mensaje de voz
    elif message.voice:

        user_name = message.from_user.first_name
        print(f"se esta procesando el audio de: {user_name}")
        
        waiting_message: str = botMessages.voice_waiting_message(message)

        # Imprimimos el mensaje de espera
        bot.send_message(message.chat.id, waiting_message)

        # Abrimos el archivo y lo enviamos
        bot.send_chat_action(message.chat.id, "upload_document")

        # Ejecutamos la funcion que descarga el archvio de auio y retorno file_name dond ese encuentra
        file_path: str = file_audio(message, bot, "voice")

    # Ejecutamos la funcion que usa el whisper con el file_path para transcriobr y retorna el texto
    text_transcription: str = whisper_api(file_path)
    # Enviamos el texto de la transcripción en un mensaje al usuario
    bot.send_message(message.chat.id, text_transcription)


bot.infinity_polling()
