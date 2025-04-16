
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = '7878699991:AAH_N8wuZxyunoe9QDgLHAlwKX8lhbo0smk'
CHANNEL_ID = '-2466755663'

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text
    text = f"📩 Повідомлення від @{user.username or user.first_name} (ID: {user.id}):\n\n{message}"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    print("🤖 Бот запущено. Очікує повідомлення...")
    app.run_polling()

if __name__ == '__main__':
    main()
