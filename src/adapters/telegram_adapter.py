from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler


def setup(token):
    builder = ApplicationBuilder().token(token).build()
    return builder


def add_command_handler(builder, command, fn):
    builder.add_handler(CommandHandler(command, fn))


def add_message_handler(builder, fn):
    builder.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), fn))


async def reply_text(update, text):
    await update.message.reply_text(text)


async def reply_photo(update, photo):
    await update.message.reply_photo(photo)


def start(builder):
    builder.run_polling()
