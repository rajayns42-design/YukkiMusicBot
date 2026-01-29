import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from YukkiMusic import app

# Chatbot status switch
chatbot_status = {}

# --- 1. Command: /chatbot on/off ---
@app.on_message(filters.command(["chatbot", "chat"]) & ~filters.bot)
async def toggle_chatbot(_, message):
    chat_id = message.chat.id
    is_on = chatbot_status.get(chat_id, True)
    
    if is_on:
        chatbot_status[chat_id] = False
        await message.reply_text("❌ **Chatbot OFF!** Ab main kisi ko reply nahi dungi.")
    else:
        chatbot_status[chat_id] = True
        await message.reply_text("✅ **Chatbot ON!** Ab sabse baatein karungi... 😘")

# --- 2. Unlimited Auto-Reply (Every Message) ---
@app.on_message(filters.text & ~filters.bot, group=10)
async def fast_ai_reply(client, message):
    chat_id = message.chat.id
    
    # Check if chatbot is OFF
    if not chatbot_status.get(chat_id, True):
        return

    # Commands ko ignore karein
    if message.text.startswith(("/", "!", ".")):
        return

    # Typing action dikhana
    await client.send_chat_action(chat_id, ChatAction.TYPING)

    # Flirting AI Prompt
    user_input = message.text
    api_url = f"https://api.punjabimunda.workers.dev/chat?query=Act as a very flirty and romantic partner. Use Hinglish and be fast. Message: {user_input}"

    try:
        response = requests.get(api_url).json()
        reply = response.get("results") or response.get("reply")
        
        if reply:
            # Har message ka unlimited reply
            await message.reply_text(reply)
    except:
        pass
