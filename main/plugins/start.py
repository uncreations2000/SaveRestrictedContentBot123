#Github.com/Vasusen-code
import pyrogram
from pyrogram import Client, filters
import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'r' + 't'
@Drone.on(filters.command(["start"]))
def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    bot.send_message(message.chat.id, f"__👋 Hi **{message.from_user.mention}**, I am Save Restricted Bot, I can send you restricted content by it's post link__\n\n{USAGE}",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🌐 Source Code", url="https://www.bing.com/chat")]]), reply_to_message_id=message.id)


@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Send me Link of any message to clone it here, For private channel message, send invite link first.\n\n**SUPPORT:** @TeamDrone"
    await start_srb(event, text)
    
