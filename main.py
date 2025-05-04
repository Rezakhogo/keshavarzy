import requests
import random

# مشخصات ربات و کانال
TOKEN = "7352316334:AAGxS9cr7RymPvmn-GuJ1IlJ6wdbQB7GsWA"
CHAT_ID = "@Avandtos"

# پیام‌های تصادفی درباره کشاورزی
messages = [
    "🌱 تناوب زراعی باعث افزایش سلامت خاک و کاهش آفات می‌شود.",
    "💧 آبیاری قطره‌ای تا ۶۰٪ در مصرف آب صرفه‌جویی می‌کند.",
    "🌾 کوددهی اصولی برای افزایش عملکرد گیاهان حیاتی است.",
    "🌿 استفاده از گیاهان پوششی خاک را در برابر فرسایش محافظت می‌کند.",
    "🌻 استفاده از بذر اصلاح‌شده باعث افزایش بهره‌وری می‌شود.",
    "🚜 مکانیزاسیون کشاورزی بهره‌وری و دقت را بالا می‌برد.",
    "🧪 آزمایش خاک پیش از کشت به بهینه‌سازی مصرف کود کمک می‌کند."
]

# انتخاب تصادفی پیام
text = random.choice(messages)

# ارسال پیام به تلگرام
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": text
}
response = requests.post(url, data=payload)

# بررسی نتیجه
if response.status_code == 200:
    print("✅ پیام با موفقیت ارسال شد.")
else:
    print(f"❌ خطا در ارسال پیام: {response.text}")
