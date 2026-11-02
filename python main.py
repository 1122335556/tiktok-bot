from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler, 
    ContextTypes, 
    filters
)

# 1. دالة الترحيب عند كتابة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    
    welcome_text = (
        f"أهلاً بك يا {user.first_name} في البوت! 🚀\n\n"
        "تم تفعيل كامل الصلاحيات لاستخدام خدماتنا.\n"
        "نتمنى لك تجربة ممتعة! ✅\n\n"
        "👇 اضغط على الزر أدناه أو اكتب 'ارفع لي حملة' للبدء:"
    )
    
    keyboard = [
        [InlineKeyboardButton("🚀 ارفع لي حملة", callback_data="launch_campaign")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# 2. دالة استقبال الرسائل والتفاصيل والكليشات
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.strip()
    
    # إذا طلب بدء حملة
    if any(keyword in text for keyword in ["حملة", "حمله", "ارفع"]):
        reply_text = (
            "🎯 **بدء إنشاء حملة إعلانية جديدة**\n\n"
            "يرجى إرسال تفاصيل الحملة (اسم المنتج، نوع الحساب، الرابط، والميزانية) لبدء الترويج."
        )
        await update.message.reply_text(reply_text, parse_mode="Markdown")
        
    # إذا أرسل تفاصيل الكليشة أو الأكواد
    elif any(keyword in text for keyword in ["المنتج", "الميزانيه", "الميزانية", "رابط", "الصفحة", "الكواد", "الأكواد", "#"]):
        confirm_text = (
            "✅ **تم استلام تفاصيل الحملة بنجاح!**\n\n"
            "📋 **تفاصيل الإعداد والجاري رفعها:**\n"
            "• **الاستهداف:** العراق (جميع المحافظات)\n"
            "• **نوع الحساب:** حساب وكالة\n"
            "• **الإعدادات:** تعطيل التعليقات، التحميل، والمشاركة\n\n"
            "⏳ جاري تجهيز الحملة ورفعها..."
        )
        await update.message.reply_text(confirm_text, parse_mode="Markdown")
        
    else:
        await update.message.reply_text("أهلاً بك! اكتب **ارفع لي حملة** لبدء إعداد الإعلان.")

# 3. دالة معالجة الأزرار
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "launch_campaign":
        reply_text = (
            "🎯 **بدء إنشاء حملة إعلانية جديدة**\n\n"
            "يرجى إرسال تفاصيل الحملة لبدء الترويج."
        )
        await query.edit_message_text(reply_text, parse_mode="Markdown")

def main():
    # توكن البوت
    TOKEN = "8876913970:AAEifstGk-xQIiWo2PyPb8y6BE-bsZtJSdo"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت يعمل الآن بنجاح...")
    app.run_polling()

if __name__ == '__main__':
    main()
