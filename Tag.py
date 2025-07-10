import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message, User

# ======== CONFIG =========
API_ID = 21189715             # Your API ID
API_HASH = "988a9111105fd2f0c5e21c2c2449edfd"  # Your API HASH
SESSION_STRING = "BQGuP2cATolbNp6x2VJbRV69OjUfn6GaHjFLodJaVbRkRG06R1bUD8nYbVomZq8Cq-QPAF_sKRqqlxrzj5YLfbQC4w0ysGTvaHTwTsuWx24M4BzJNTNpIQ1lWtvFlD9mOG1YI8B-YN_P2FdCW6pUFAjA34JWJhKoKZWLbUCrk16401n4DqswpeE_XcR8of_xxCoIZAccEIU7ugiYketKyOfFfNft1qhFcN0p-1egH-9vvJvhBZQ4qBxArGz3Bz7BPUiqs-ZaWYO4zeEXDx2CIMpt6_PIb3DRXvCDlxUvATjsTBEjOSJWKVe9cMXwMGRZGdoIZZJA4SvmXdhbDDuZQavbDrkg7QAAAAFGEz7IAA"  # Your Pyrogram string session
SUDO_ID = 8111174619         # Your Telegram user ID

# ======== CASUAL MESSAGES =========
casual_messages = [
    "Hey! How was your day?",
    "Had lunch?",
    "Did you sleep well?",
    "Good morning!",
    "Don’t forget to drink water!",
    "Hope your day’s going well!",
    "What’s up?",
    "Feeling sleepy?",
    "Any weekend plans?",
    "Watching something good lately?",
    "Working or chilling today?",
    "Have you eaten?",
    "What’s your mood today?",
    "Good night 💤",
    "Stay hydrated!",
    "Everything okay?",
    "Missed you here!",
    "Feeling motivated?",
    "Anyone up for a game?",
    "Remember to smile today!",
    "Life’s good?",
    "Did you workout today?",
    "Try something new today!",
    "Sending good vibes!",
    "Tell me something fun!",
    "What's on your mind?",
    "Heard a good song today?",
    "What's your favorite snack?",
    "Weekend mood?",
    "Rainy days or sunny skies?",
    "Do you believe in luck?",
    "Let’s play truth or dare!",
    "Pick a number 1–10!",
    "How’s the weather?",
    "Coffee or tea?",
    "Night owl or early bird?",
    "Feeling happy today?",
    "Any travel plans?",
    "Need a virtual hug?",
    "Working hard or hardly working?",
    "Who’s hungry?",
    "Biryani or Pizza?",
    "Let’s vibe!",
    "Movie night today?",
    "Take a deep breath 💨",
    "Feeling grateful today?",
    "Post a meme now!",
    "Today feels…?",
    "Anyone wants chai?",
    "Let’s go on a virtual trip!",
    "Last thing you Googled?",
    "Let’s laugh for no reason 😂",
    "Tell me your dream destination",
    "Phone battery percentage?",
    "Let’s take a nap 💤",
    "Your favorite emoji?",
    "Let’s skip Monday!",
    "Who’s in love? ❤️",
    "Tag your bestie!",
    "Rate today from 1–10",
    "Hug or handshake?",
    "Let’s manifest success!",
    "One word for today?",
    "How are you, really?",
    "Mental peace matters.",
    "Drop your favorite quote.",
    "What song describes you?",
    "Who inspires you?",
    "Rate your sleep last night!",
    "What makes you smile?",
    "Pani piya kya?",
    "Missed meals today?",
    "Let’s dance 🕺",
    "You’re awesome, remember that!",
    "Motivation level: ?",
    "Your current mood?",
    "Let’s talk random!",
    "Sunshine or moonlight?",
    "Keep smiling 😄",
    "Inner peace unlocked!",
    "You got this 💪",
    "Don’t forget to stretch!",
    "It’s okay to rest.",
    "Let’s spread positivity!",
    "Dinner plans?",
    "Midweek vibes?",
    "Let’s take a break.",
    "Pause. Breathe. Continue.",
    "Recharge your soul 🔋",
    "Small wins count!",
    "Be kind to yourself.",
    "Do one thing for yourself today.",
    "Your vibe attracts your tribe.",
    "Self-love is key 🗝️",
    "Make today count.",
    "Gratitude unlocks happiness.",
    "You’re not alone.",
    "Take time for yourself.",
    "Life’s short, enjoy!",
    "Keep moving forward.",
    "Laugh loud today.",
    "Trust the process.",
    "Believe in yourself.",
    "Happiness looks good on you.",
    "One smile = 1 blessing!",
    "You’re stronger than you think.",
    "Shine bright 🌟",
    "Look up and smile!",
    "Share something you learned today.",
    "What’s one goal this week?",
    "Chai time anyone?",
    "Focus on progress.",
    "How's your vibe?",
    "Let's have a chill moment.",
    "Midnight thoughts?",
    "Late night snacks?",
    "Netflix suggestions?",
    "Who’s feeling lazy?",
    "Laugh attack incoming!",
    "One thing you're grateful for?",
    "Type without looking!",
    "Pet lovers here?",
    "Time to unplug 🔌",
    "Stay soft, stay strong.",
    "Mood: ❤️‍🔥",
    "Random thought: ______",
    "It’s okay to feel things.",
    "Best compliment today?",
    "Wholesome check ✅",
    "Let’s talk nostalgia.",
    "Music = Therapy 🎵",
    "What’s your energy level?",
    "Today’s win?",
    "Tell me a secret (jk!)",
    "Life update?",
    "Vibe check?",
    "Emoji mood right now?",
    "Drop a 💯 if you're chillin",
    "Couch potato day?",
    "Any dream last night?",
    "Let’s talk crushes 😏",
    "Who needs motivation?",
    "Shower thoughts?",
    "Group selfie when?",
    "Tea break?",
    "Weekend plans: ______",
    "Feeling productive?",
    "Zoom call disasters?",
    "Remote life check!",
    "Your hobby?",
    "Try learning a new word today!",
    "Compliment someone here 💬",
    "Write your dream job!",
    "One emoji to describe your week?",
    "Let’s plan a fake trip!",
    "What’s trending?",
    "Which app did you open first today?",
    "Would you rather…?",
    "Describe yourself in 3 emojis.",
    "Something that made you smile?",
    "Hey, you’re cool 😎",
    "Unpopular opinion?",
    "How do you relax?",
    "Who loves silence?",
    "Night talks or morning walks?",
    "Your favorite childhood snack?",
    "Cartoon you still love?",
    "Who’s feeling bored?",
    "Text someone you miss.",
    "Movie that made you cry?",
    "Best advice received?",
    "Tell me your mood in a song lyric.",
    "Virtual high five! 🙌",
    "You deserve good things.",
    "Screenshot your current screen!",
    "Who’s your safe space?",
    "Tell me a joke!",
    "Let’s play rapid fire!",
    "Your comfort food?",
    "Best smell ever?",
    "Let’s manifest peace.",
    "What would you name a pet tiger?",
    "Choose your superpower!",
    "Describe today with 1 word.",
    "Send your favorite emoji spam!",
    "Let’s play 5 questions!",
    "Meme war incoming?",
    "One guilty pleasure?",
    "What relaxes your brain?",
    "Biggest flex today?",
    "Rate this chat!",
    "Drop random facts!",
    "Who’s cooking today?",
    "Sleep schedule: broken or fixed?",
    "Working on your dreams?",
    "Last voice message sent?",
    "Last pic in your gallery?",
    "Your 2025 goal?",
    "Positive vibes only 💫",
    "Who do you admire?",
    "Let’s not overthink today.",
    "Silent vibes?",
    "Talkative or reserved?",
    "Your favorite time of day?",
    "Late night conversations?",
    "Still awake? 💤",
    "Love yourself more 💖",
    "What’s one habit to build?",
    "Random advice?",
    "What's your biggest dream?",
    "What time is it for you?",
    "Should we start a challenge?",
    "What's your love language?",
    "Describe yourself in 2 lines.",
    "Are you a morning person?",
    "What’s your favorite moment today?",
    "Mental health check?",
    "Who's your person?",
    "Something you wish others knew?",
    "Kindness matters ❤️",
    "What’s in your mind?",
    "Sending hugs 🤗",
    "Inner peace is gold.",
    "You made it this far!",
    "Tiny steps matter.",
    "Find your balance.",
    "Just show up.",
    "Clap for yourself 👏",
    "Healing is happening.",
    "Today is your day 🌞",
]


# ======== CLIENT & STATE =========
app = Client(name="userbot", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
active_tags = {}

# ======== COMMAND: START TAGGING =========
@app.on_message(filters.command("starttag") & filters.group)
async def start_tag(client: Client, message: Message):
    if message.from_user.id != SUDO_ID:
        return

    chat_id = message.chat.id
    if active_tags.get(chat_id):
        await message.reply("Already tagging in this group.")
        return

    active_tags[chat_id] = True
    await message.reply("🚀 Starting to tag members...")

    async for member in client.get_chat_members(chat_id):
        if not active_tags.get(chat_id):
            break

        user: User = member.user
        if user.is_bot:
            continue

        mention = f"@{user.username}" if user.username else f"[{user.first_name}](tg://user?id={user.id})"
        text = f"{random.choice(casual_messages)}\n{mention}"

        try:
            await client.send_message(chat_id, text, parse_mode="markdown")
        except Exception as e:
            print(f"Failed to tag: {e}")

        await asyncio.sleep(5)

    active_tags.pop(chat_id, None)

# ======== COMMAND: STOP TAGGING =========
@app.on_message(filters.command("stop") & filters.group)
async def stop_tag(client: Client, message: Message):
    if message.from_user.id != SUDO_ID:
        return

    chat_id = message.chat.id
    if active_tags.get(chat_id):
        active_tags[chat_id] = False
        await message.reply("🛑 Tagging stopped.")
    else:
        await message.reply("No tagging in progress.")

# ======== COMMAND: PING =========
@app.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    if message.from_user.id == SUDO_ID:
        await message.reply("✅ Bot is alive.")

# ======== START APP =========
print("🤖 Userbot starting...")
app.run()
