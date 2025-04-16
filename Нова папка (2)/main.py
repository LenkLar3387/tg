from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# Токен бота та ID каналу тепер беруться зі змінних середовища (безпечно!)
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text
    # Форматуємо повідомлення для каналу
    text = f"📩 Повідомлення від @{user.username or user.first_name} (ID: {user.id}):\n\n{message}"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=text)

def main():
    # Створюємо бота
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    # Додаємо обробник текстових повідомлень (крім команд)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    print("🤖 Бот запущено. Очікує повідомлення...")
    app.run_polling()

if __name__ == '__main__':
    main()