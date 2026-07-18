import os
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from openai import OpenAI

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")

client = OpenAI(
    api_key=os.getenv("FREEMODEL_API_KEY"),
    base_url=os.getenv("FREEMODEL_BASE_URL"),
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في ميزان.\n\n"
        "أنا مساعدك الذكي لمقارنة الأسعار والعثور على أفضل العروض.\n\n"
        "اكتب اسم أي منتج وسأساعدك."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "أنت مساعد ذكي عربي اسمه ميزان."
                        " تساعد المستخدمين في الإجابة على الأسئلة"
                        " والبحث عن المعلومات بطريقة احترافية."
                    ),
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

        reply = response.choices[0].message.content

        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text(f"❌ حدث خطأ:\n{e}")


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not found")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🤖 MeezanBot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
