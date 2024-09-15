import httpx, base64
from pyrogram import Client, filters


@Client.on_message(filters.command("upscale"))
async def upscale_image(client, message):
    try:
        # Check if the replied message contains a photo
        if message.reply_to_message and message.reply_to_message.photo:
            # Send a message indicating upscaling is in progress
            progress_msg = await message.reply_text(
                "✦ ᴜᴘsᴄᴀʟɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢᴇ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ..."
            )

          
            image = message.reply_to_message.photo.file_id
            file_path = await client.download_media(image)

            with open(file_path, "rb") as image_file:
                f = image_file.read()

            b = base64.b64encode(f).decode("utf-8")

            async with httpx.AsyncClient() as http_client:
                response = await http_client.post(
                    "https://api.qewertyy.me/upscale",
                    data={"image_data": b},
                    timeout=None,
                )

            # Save the upscaled image
            upscaled_file_path = "upscaled_image.png"
            with open(upscaled_file_path, "wb") as output_file:
                output_file.write(response.content)

            # Delete the progress message
            await progress_msg.delete()

            # Send the upscaled image as a PNG file
            await client.send_document(
                message.chat.id,
                document=upscaled_file_path,
                caption=f"✦ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ➠ [ᴅᴏɴᴀᴛᴇ_ᴀʀᴍʏ™](https://t.me/DONATE_ARMY_ULTIMATE_FILTER_BOT)\n\n✦ ᴜᴘᴅᴀᴛᴇ ➠ [𝘿𝙊𝙉𝘼𝙏𝙀 ๛ 𝘼𝙍𝙈𝙔 ✘ 𝘽𝙊𝙏𝙎 ™](https://t.me/DONATE_ARMY_BOTS)",
            )
        else:
            await message.reply_text("✦ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ.")

    except Exception as e:
        print(f"✦ ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ➛ {e}")
        await message.reply_text("✦ ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ᴛʜᴇ ɪᴍᴀɢᴇ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.")
