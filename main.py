from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"
MANAGER_ID = 997176937
REVIEWS_CHANNEL = "@EclipseAgencyReviews"

BUTTONS = [
    "📄 Оставить анкету",
    "💰 Зарплата",
    "📋 Условия работы",
    "⭐ Отзывы",
    "📢 Наш канал",
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📄 Оставить анкету"],
        ["💰 Зарплата"],
        ["📋 Условия работы"],
        ["⭐ Отзывы"],
        ["📢 Наш канал"],
    ]

    context.user_data.clear()

    await update.message.reply_text(
        "🇰🇷 Добро пожаловать в Eclipse Agency KR",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in BUTTONS:
        if text == "⭐ Отзывы":
            context.user_data.clear()
            context.user_data["review_mode"] = True
            await update.message.reply_text(
                "✍️ Напишите ваш отзыв одним сообщением.\n\nОн будет опубликован анонимно в канале отзывов."
            )
            return

        if text == "📄 Оставить анкету":
            context.user_data.clear()
            context.user_data["application_mode"] = True
            await update.message.reply_text("Напишите:\n\nИмя\nВозраст\nГражданство")
            return

        if text == "💰 Зарплата":
            context.user_data.clear()
            await update.message.reply_text("💰 Доход от 150 000 ₽ до 300 000 ₽ в месяц.")
            return

        if text == "📋 Условия работы":
            context.user_data.clear()
            await update.message.reply_text(
                """📋 Условия работы

🇰🇷 Работа в премиум караоке Южной Кореи

✅ Бесплатное проживание
✅ Помощь с документами
✅ Встреча и сопровождение
✅ Без знания корейского языка

💰 Доход от 150 000 ₽ до 300 000 ₽ в месяц"""
            )
            return

        if text == "📢 Наш канал":
            context.user_data.clear()
            await update.message.reply_text("📢 Наш канал:\n\nhttps://t.me/KoreaGirlsJob")
            return

    if context.user_data.get("review_mode"):
        await context.bot.send_message(
            chat_id=REVIEWS_CHANNEL,
            text=f"⭐ Новый отзыв\n\n{text}",
        )
        context.user_data.clear()
        await update.message.reply_text("✅ Спасибо! Ваш отзыв опубликован анонимно.")
        return

    if context.user_data.get("application_mode"):
        user = update.message.from_user
        username = f"@{user.username}" if user.username else "username не указан"

        await context.bot.send_message(
            chat_id=MANAGER_ID,
            text=(
                "📄 Новая анкета\n\n"
                f"👤 Имя в Telegram: {user.full_name}\n"
                f"🔗 Username: {username}\n"
                f"🆔 ID: {user.id}\n\n"
                f"Анкета:\n{text}"
            ),
        )

        context.user_data.clear()
        await update.message.reply_text("✅ Спасибо! Ваша анкета отправлена менеджеру.")
        return


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

if __name__ == "__main__":
    app.run_polling()
