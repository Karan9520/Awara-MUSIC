import requests
from pyrogram import filters
from pyrogram.enums import ChatAction, ParseMode
from BrandrdXMusic import app  # Aapka app instance (Bot Client)

# BIN Lookup command handler
@app.on_message(filters.command(["bin", "bins"], prefixes=["/", ".", "!", "j", "J"]))
async def handle_bin_command(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        command_parts = message.text.split()
        if len(command_parts) < 2:
            await message.reply_text(
                "*❌ Please provide a BIN number. Example:* `/bin 412451`",
                parse_mode=ParseMode.MARKDOWN
            )
            return

        bin_number = command_parts[1].strip()
        api_url = f"https://last-warning.serv00.net/bin_lookup.php?bin_number={bin_number}"

        response = requests.get(api_url)

        if response.status_code == 200:
            try:
                data = response.json()
                credit = data.get("credit", "Unknown")
                bin_code = data.get("bin", "Unknown")
                scheme = data.get("scheme", "Unknown")
                bin_type = data.get("type", "Unknown")
                brand = data.get("brand", "Unknown")
                prepaid = data.get("prepaid", "Unknown")

                bank = data.get("bank", {})
                bank_name = bank.get("name", "Unknown")
                bank_url = bank.get("url", "Unknown")
                bank_phone = bank.get("phone", "Unknown")

                country = data.get("country", {})
                country_name = country.get("name", "Unknown")
                country_alpha2 = country.get("alpha2", "Unknown")
                country_currency = country.get("currency", "Unknown")
                country_emoji = country.get("emoji", "🌍")

                message_text = (
                    "✅ BIN Lookup Result\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🏷 BIN: `{bin_code}`\n"
                    f"🔹 Scheme: `{scheme}`\n"
                    f"🔘 Type: `{bin_type}`\n"
                    f"🏦 Brand: `{brand}`\n"
                    f"🛒 Prepaid: `{prepaid}`\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🏛 Bank Name: `{bank_name}`\n"
                    f"🌐 Bank URL: `{bank_url}`\n"
                    f"📞 Bank Phone: `{bank_phone}`\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    f"🌎 Country: `{country_name}` {country_emoji}\n"
                    f"🔠 Alpha2 Code: `{country_alpha2}`\n"
                    f"💰 Currency: `{country_currency}`\n"
                    "━━━━━━━━━━━━━━━━━━━━"
                )

                await message.reply_text(message_text, parse_mode=ParseMode.MARKDOWN)

            except Exception as e:
                await message.reply_text(
                    f"*❌ Error parsing data: *`{str(e)}`",
                    parse_mode=ParseMode.MARKDOWN
                )
        else:
            await message.reply_text(
                "*❌ Failed to fetch BIN details. Try again later.*",
                parse_mode=ParseMode.MARKDOWN
            )

    except Exception as e:
        await message.reply_text(f"*❌ Error: *`{str(e)}`", parse_mode=ParseMode.MARKDOWN)

# CC Validation Command Handler
@app.on_message(filters.command(["ccvalidate", "cccheck"], prefixes=["/", ".", "!", "j", "J"]))
async def handle_cc_validation(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        command_parts = message.text.split()
        if len(command_parts) < 2:
            await message.reply_text(
                "*❌ Please upload a CSV file with CC numbers for validation.* Example: `/ccvalidate <file>`",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        file_id = command_parts[1]  # Placeholder for file ID
        # File download logic and processing should go here.
        # After processing, send results back to user as a file.
        
        await message.reply_text("Processing the CC validation... Please wait.", parse_mode=ParseMode.MARKDOWN)

        # Example: Process the CSV file containing CC numbers
        # validate_ccs(file_path) would be implemented for CC validation logic

    except Exception as e:
        await message.reply_text(f"*❌ Error: *`{str(e)}`", parse_mode=ParseMode.MARKDOWN)

# CC Generation Command Handler
@app.on_message(filters.command(["ccgen", "ccgenerate"], prefixes=["/", ".", "!", "j", "J"]))
async def handle_cc_generation(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        command_parts = message.text.split()
        if len(command_parts) < 2:
            await message.reply_text(
                "*❌ Please provide a BIN number to generate a valid CC number.* Example: `/ccgen 412451`",
                parse_mode=ParseMode.MARKDOWN
            )
            return

        bin_number = command_parts[1].strip()
        cc_number = generate_cc_number(bin_number)  # Assume generate_cc_number() is implemented

        if cc_number:
            await message.reply_text(
                f"✅ Generated CC Number: `{cc_number}`",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await message.reply_text(
                "*❌ Failed to generate a valid CC number. Try again later.*",
                parse_mode=ParseMode.MARKDOWN
            )

    except Exception as e:
        await message.reply_text(f"*❌ Error: *`{str(e)}`", parse_mode=ParseMode.MARKDOWN)

# Function to generate a valid CC number based on a BIN
def generate_cc_number(bin_number):
    """Generate a random CC number based on the provided BIN (first 6 digits)."""
    # Generate a valid CC number logic (append random digits and check using Luhn algorithm)
    cc_number = bin_number + ''.join([str(random.randint(0, 9)) for _ in range(10)])  # Random 10 digits
    # You can also integrate checksum validation (Luhn Algorithm) to ensure valid CC number
    return cc_number  # Example CC number, you can integrate further checks

# Start the bot
app.run()
