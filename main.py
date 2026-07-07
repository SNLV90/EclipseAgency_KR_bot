from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8819651987:AAF00QV5XXrwoTjiGJtTNQTMTrvQ9kfP8go"
MANAGER_ID = 997176937
REVIEWS_CHANNEL = "@EclipseAgencyReviews"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 Оставить анкету"],
        ["💰 Зарплата"],
        ["📋 Условия работы"],
        ["⭐️ Отзывы"],
        ["📢 Наш канал"],
    ]

    await update.message.reply_text(
        "🇰🇷 Добро пожаловать в Eclipse Agency KR",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if context.user_data.get("review_mode"):
        await context.bot.send_message(
            chat_id=REVIEWS_CHANNEL,
            text=f"⭐️ Новый отзыв\n\n{text}",
        )
        context.user_data.clear()
        await update.message.reply_text("✅ Спасибо! Ваш отзыв опубликован анонимно.")
        return

    if text == "⭐️ Отзывы":
        context.user_data["review_mode"] = True
        await update.message.reply_text(
            "✍️ Напишите ваш отзыв одним сообщением.\n\nОн будет опубликован анонимно в канале отзывов."
        )

    elif text == "📄 Оставить анкету":
        await update.message.reply_text("Напишите:\n\nИмя\nВозраст\nГражданство")

    elif text == "💰 Зарплата":
        await update.message.reply_text("💰 Доход от 150 000 ₽ до 300 000 ₽ в месяц.")

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

    elif text == "📢 Наш канал":
        await update.message.reply_text("📢 Наш канал:\n\nhttps://t.me/KoreaGirlsJob")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

if name == "main":
    app.run_polling()
