from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8819651987:AAF00QV5XXrwoTjiGJtTNQTMTrvQ9kfP8go"
MANAGER_ID = 997176937


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 Оставить анкету"],
        ["💰 Зарплата"],
        ["📋 Условия работы"],
        ["⭐ Отзывы"],
        ["📢 Наш канал"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🇰🇷 Добро пожаловать в Eclipse Agency KR",
        reply_markup=reply_markup
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📄 Оставить анкету":
        await update.message.reply_text(
            "Напишите:\n\nИмя\nВозраст\nГражданство"
        )

    elif text == "💰 Зарплата":
        await update.message.reply_text(
            "💰 Средний доход от 150 000 ₽ до 300 000 ₽ в месяц."
        )

    elif text == "📋 Условия работы":
        await update.message.reply_text(
            """📋 Условия работы

🇰🇷 Работа в премиум караоке Южной Кореи

✅ Бесплатное проживание
✅ Помощь с документами
✅ Встреча и сопровождение
✅ Без знания корейского языка

💰 Доход от 150 000 ₽ до 300 000 ₽ в месяц"""
        )

    elif text == "⭐ Отзывы":
        await update.message.reply_text(
            "✍️ Напишите ваш отзыв одним сообщением."
    )

    elif text == "📢 Наш канал":
        await update.message.reply_text(
            "📢 Наш канал:\n\nhttps://t.me/KoreaGirlsJob"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

if __name__ == "__main__":
    app.run_polling()
