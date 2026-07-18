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

logging.basicConfig(
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,
)

TOKEN =8578143859:AAFZAqkgGdFgLBSmSZAGQJx0Hv50TeTn2ZM

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"👋 أهلاً بك في ميزان.\n\n"
"أنا مساعدك الذكي لمقارنة الأسعار والعثور على أفضل العروض.\n\n"
"اكتب اسم أي منتج وسأساعدك في العثور على أفضل خيار."
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
user_message = update.message.text

await update.message.reply_text(  
    f"🔍 استلمت طلبك:\n\n{user_message}\n\n"  
    "قريبًا سأبحث لك عن أفضل الأسعار."  
)

def main():
if not TOKEN:
raise ValueError("BOT_TOKEN environment variable not found")

app = Application.builder().token(TOKEN).build()  

app.add_handler(CommandHandler("start", start))  
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  

print("MeezanBot Started...")  

app.run_polling()

if name == "main":
main()
