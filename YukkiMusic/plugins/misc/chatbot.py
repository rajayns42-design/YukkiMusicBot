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
        await message.reply_text("❌ **Auto-Reply OFF!**\nAb main baatein nahi karungi.")
    else:
        chatbot_status[chat_id] = True
        await message.reply_text("✅ **Auto-Reply ON!**\nChalo baby, unlimited baatein shuru karte hain.. 😘")

# --- 2. Button Handler: Menu control ke liye ---
@app.on_callback_query(filters.regex("chatbot_setup"))
async def cb_chatbot_setup(client, query: CallbackQuery):
    chat_id = query.message.chat.id
    is_on = chatbot_status.get(chat_id, True)
    status_text = "✅ ACTIVE" if is_on else "❌ INACTIVE"
    
    await query.answer("Fast Reply Menu", show_alert=True)
    await query.edit_message_text(
        f"🚀 **Fast & Unlimited Chatbot**\n\n"
        f"Status: **{status_text}**\n\n"
        "Ye bot group aur private mein har message ka turant romantic reply dega.\n\n"
        "🔹 ON karne ke liye: `/chatbot on` \n"
        "🔹 OFF karne ke liye: `/chatbot off`"
    )

# --- 3. Unlimited Auto-Reply Logic ---
@app.on_message(filters.text & ~filters.bot, group=10)
async def fast_ai_reply(client, message):
    chat_id = message.chat.id
    
    # Check status
    if not chatbot_status.get(chat_id, True):
        return

    # Commands ignore karein
    if message.text.startswith(("/", "!", ".")):
        return

    # Typing action (Fast feel ke liye)
    await client.send_chat_action(chat_id, ChatAction.TYPING)

    # Raw Flirting Prompt
    user_input = message.text
    api_url = f"https://api.punjabimunda.workers.dev/chat?query=Act as a highly flirty and romantic partner. Use Hinglish. Give very fast, short and sexy replies. No names. Message: {user_input}"

    try:
        response = requests.get(api_url).json()
        reply = response.get("results") or response.get("reply")
        
        if reply:
            await message.reply_text(reply)
    except:
        # Fallback agar API down ho
        pass
