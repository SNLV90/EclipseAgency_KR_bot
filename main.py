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
        ["⭐Отзывы"],
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

    if context.user_data.get("step") == "name":
        context.user_data["name"] = text
        context.user_data["step"] = "age"

        await update.message.reply_text("Введите возраст:")
        return

    if context.user_data.get("step") == "age":
        context.user_data["age"] = text
        context.user_data["step"] = "country"

        await update.message.reply_text("Введите гражданство:")
        return

    if context.user_data.get("step") == "country":
        name = context.user_data["name"]
        age = context.user_data["age"]
        country = text

        user_id = update.effective_user.id
        username = update.effective_user.username

        await context.bot.send_message(
            chat_id=MANAGER_ID,
            text=f"""📄 НОВАЯ АНКЕТА

👤 Имя: {name}
🎂 Возраст: {age}
🌍 Гражданство: {country}

📱 Username: @{username if username else 'нет'}
🆔 Telegram ID: {user_id}
"""
        )

        await update.message.reply_text(
            "✅ Анкета отправлена менеджеру.\nОжидайте ответа."
        )

        context.user_data.clear()
        return

    if text == "📄 Оставить анкету":
        context.user_data["step"] = "name"
        await update.message.reply_text("Введите ваше имя:")

    elif text == "💰 Зарплата":
        await update.message.reply_text(
            """💰 ЗАРПЛАТА

Средний доход:
▪️ от 150 000 до 300 000 ₽ в месяц

Доход зависит от города, клуба и графика работы.

Для подробной информации свяжитесь с менеджером."""
        )

    elif text == "📋 Условия работы":
        await update.message.reply_text(
            """📋 УСЛОВИЯ РАБОТЫ

🇰🇷 Работа в премиальных караоке Южной Кореи

✅ Доход от 150 000 до 300 000 ₽ в месяц
✅ Бесплатное проживание
✅ Встреча в аэропорту
✅ Помощь с документами
✅ Поддержка менеджера 24/7
✅ Без знания корейского языка

Обязанности:
• Общение с гостями
• Поддержание приятной атмосферы
• Караоке и настольные игры

Для консультации напишите менеджеру."""
        )

    elif text == "📞 Менеджер":
        await update.message.reply_text("@SNLVKR")

    elif text == "📢 Наш канал":
        await update.message.reply_text("https://t.me/KoreaGirlsJob")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

if __name__ == "__main__":
    app.run_polling()
