import requests
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import CallbackQuery
from YukkiMusic import app

# Chatbot status switch (Default ON)
chatbot_status = {}

# --- 1. Command: /chatbot on/off ---
@app.on_message(filters.command(["chatbot", "chat"]) & ~filters.bot)
async def toggle_chatbot(_, message):
    chat_id = message.chat.id
    is_on = chatbot_status.get(chat_id, True)
    
    if is_on:
        chatbot_status[chat_id] = False
        await message.reply_text("❌ **Chatbot OFF!**\nAb main chup ho gayi hoon. 🥺")
    else:
        chatbot_status[chat_id] = True
        await message.reply_text("✅ **Chatbot ON!**\nAa gayi main! Ab sirf tumhari aur meri baatein hongi... 😘")

# --- 2. Button Handler (For Help Menu) ---
@app.on_callback_query(filters.regex("chatbot_setup"))
async def cb_chatbot_setup(client, query: CallbackQuery):
    chat_id = query.message.chat.id
    is_on = chatbot_status.get(chat_id, True)
    status_text = "✅ ACTIVE" if is_on else "❌ INACTIVE"
    
    await query.answer("Romantic Chatbot Menu", show_alert=True)
    await query.edit_message_text(
        f"🚀 **Desi Romantic Chatbot**\n\n"
        f"Current Status: **{status_text}**\n\n"
        "Main har message ka fast aur flirty reply dungi.\n\n"
        "🔹 Turn ON: `/chatbot on` \n"
        "🔹 Turn OFF: `/chatbot off`"
    )

# --- 3. Unlimited Desi Flirting Logic ---
@app.on_message(filters.text & ~filters.bot, group=10)
async def fast_ai_reply(client, message):
    chat_id = message.chat.id
    
    # Status Check
    if not chatbot_status.get(chat_id, True):
        return

    # Ignore Commands
    if message.text.startswith(("/", "!", ".")):
        return

    # Show Typing Action
    await client.send_chat_action(chat_id, ChatAction.TYPING)

    # UPDATED: More Desi & Romantic Prompt
    user_input = message.text
    prompt = (
        "Act as a very romantic, naughty and caring Indian partner. "
        "Use pure Hinglish (Hindi + English mix). "
        "Keep replies short, fast, and very sweet. "
        "Use emojis like ❤️, 😘, 🙈. Don't use any names. "
        f"User said: {user_input}"
    )
    
    api_url = f"https://api.punjabimunda.workers.dev/chat?query={prompt}"

    try:
        response = requests.get(api_url).json()
        reply = response.get("results") or response.get("reply")
        
        if reply:
            await message.reply_text(reply)
    except:
        pass
