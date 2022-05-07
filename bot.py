from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from voice import text_to_file


TOKEN = "..."
updater = Updater(TOKEN)


def start_hendler(update, context):
    start_text = (f"""Здравсвуй, {update.effective_user.first_name}!
Я буду твоим другом :)""")
    update.message.reply_text(start_text)


def hello_hendler(update, context):
    update.message.reply_text(f'Привет, {update.effective_user.first_name} напиши мне что-то и я озвучу твоё сообщение')


def help_hendler(update, context):
    help_text = """Бот работает в тестовом режиме.
Переводит тект в аудивосообщение, а так же показывает курс биткоина и эфира в реальном времени"""
    update.message.reply_text(help_text)


def reply_all_text(update, context):
    file_voice = text_to_file(update.message.text)
    update.message.reply_text("Озвучиваю текст: " + update.message.text)
    update.message.reply_voice(voice=open(file_voice, 'rb'))


def reply_all_voice(update, context):
    text_from_voice = """Находится в разработке.
В данный момент не поддерживается перевод аудио в текст."""
    update.message.reply_text(text_from_voice)


ud = updater.dispatcher
ud.add_handler(CommandHandler('start', start_hendler))
ud.add_handler(CommandHandler('hello', hello_hendler))
ud.add_handler(CommandHandler('help', help_hendler))
ud.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_all_text))
ud.add_handler(MessageHandler(Filters.voice & ~Filters.command, reply_all_voice))

updater.start_polling() # обрабатывает входящие сообщения на сервере (единожды)
updater.idle() # делает так чтобы наши сообщения на сервере проверялись многократно
