import asyncio
import requests
from pyrogram import filters
from pyrogram.enums import ChatAction, ParseMode
from BrandrdXMusic import app

# HuggingFace Inference API URL
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-llm-r1-7b-chat"
HEADERS = {"Authorization": "Bearer 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"}  # <-- Insert your token here

def deepseek_query(prompt: str) -> str:
    payload = {
        "inputs": f"<|user|>\n{prompt}\n<|assistant|>\n",
        "parameters": {"max_new_tokens": 512, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"].split("<|assistant|>")[-1].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

@app.on_message(filters.command(["chatgpt", "ai", "ask", "iri"], prefixes=[".", "J", "j", "s", "/"]))
async def chat_gpt(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        name = message.from_user.first_name if message.from_user else "User"

        if len(message.command) < 2:
            await message.reply_text(f"**Hello {name}, how can I help you today?**")
            return

        query = message.text.split(" ", 1)[1]
        print(f"Query from {name}: {query}")

        # Use DeepSeek model in a thread-safe way
        response = await asyncio.to_thread(deepseek_query, query)
        print(f"DeepSeek Response: {response}")

        if len(response) > 4096:
            for i in range(0, len(response), 4096):
                await message.reply_text(response[i:i+4096], parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text(response, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        await message.reply_text(f"**Error: {str(e)}**")
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
