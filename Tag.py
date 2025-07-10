import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message, User

# ========== CONFIG ==========
API_ID = 21189715  # Your API ID
API_HASH = "988a9111105fd2f0c5e21c2c2449edfd"  # Your API Hash
SESSION_STRING = "BQGuP2cATolbNp6x2VJbRV69OjUfn6..."  # Your full Pyrogram string session
SUDO_ID = 8111174619  # Your Telegram User ID

# ========== MESSAGES ==========
casual_messages = [
    "Hey! How was your day?", "Did you sleep well?", "Feeling sleepy?",
    "Hope your day’s going well!", "Watching something good lately?",
    "Let’s vibe!", "Have you eaten?", "Good night 💤", "Stay hydrated!",
    "What’s your mood today?", "Sending good vibes!", "Missed meals today?",
    "Life’s short, enjoy!", "Let’s take a break.", "Feeling motivated?",
    "Tell me your dream destination", "Rainy days or sunny skies?",
    "Random thought?", "Midweek vibes?", "Couch potato day?",
    "What's your energy level?", "Positive vibes only 💫", "Take a deep breath 💨",
    "Virtual high five! 🙌", "Weekend plans?", "Keep moving forward!",
    "Still awake? 💤", "Recharge your soul 🔋", "Hug or handshake?",
    "Describe today with 1 word.", "Movie night today?", "Feeling productive?",
    "Good morning ☀️", "Emoji mood right now?", "Let’s manifest peace!",
    "Drop your favorite quote.", "Your comfort food?", "Laugh attack incoming!",
    "Pet lovers here?", "Mental peace matters.", "Let’s spread positivity!",
    "Hey, you’re cool 😎", "Just show up.", "Healing is happening.",
    "Tiny steps matter.", "Clap for yourself 👏", "Stay soft, stay strong.",
    "Take time for yourself.", "Rate today from 1–10", "How are you, really?"
]

# ========== INIT CLIENT ==========
app = Client("userbot", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
active_tags = {}

# ========== START TAGGING ==========
@app.on_message(filters.command("starttag") & filters.group)
async def start_tagging(client: Client, message: Message):
    if message.from_user.id != SUDO_ID:
        return await message.reply("❌ You are not authorized.")

    chat_id = message.chat.id
    if active_tags.get(chat_id):
        return await message.reply("⚠️ Tagging is already running.")

    active_tags[chat_id] = True
    await message.reply("🚀 Starting tagging...")

    async for member in client.get_chat_members(chat_id):
        if not active_tags.get(chat_id):
            break

        user: User = member.user
        if user.is_bot:
            continue

        mention = (
            f"@{user.username}"
            if user.username
            else f"<a href='tg://user?id={user.id}'>{user.first_name or 'User'}</a>"
        )
        text = f"{random.choice(casual_messages)}\n{mention}"

        try:
            await client.send_message(chat_id, text, parse_mode="html")
        except Exception as e:
            print(f"[ERROR] Failed to tag: {e}")

        await asyncio.sleep(5)

    active_tags.pop(chat_id, None)
    await message.reply("✅ Tagging finished or stopped.")

# ========== STOP TAGGING ==========
@app.on_message(filters.command("stop") & filters.group)
async def stop_tagging(client: Client, message: Message):
    if message.from_user.id != SUDO_ID:
        return await message.reply("❌ You are not authorized.")

    chat_id = message.chat.id
    if active_tags.get(chat_id):
        active_tags[chat_id] = False
        await message.reply("🛑 Tagging stopped.")
    else:
        await message.reply("❌ No tagging is running.")

# ========== PING ==========
@app.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    if message.from_user.id == SUDO_ID:
        await message.reply("✅ Bot is alive and running!")

# ========== START BOT ==========
print("🤖 Userbot starting...")
app.run()
