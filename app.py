# search-ms:displayname=Program%20Files의%20검색%20결과&crumb=location:C%3A%5CProgram%20Files\Tesseract-OCR
import pytesseract
import discord
import pytesseract
import cv2
import numpy as np
from PIL import Image
import requests     
import os
    
bot = discord.Client(command_prefix='.', description="This is an AUTHs")

serverid = 1 # 인증서버 아이디
channelid = 1 # 인증채널 아이디
# Events
@bot.event
async def on_ready():
    if not os.path.isdir('사진'):
        os.mkdir('사진')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="RWS2 AUTH"))
    print('ad')

@bot.event
async def on_message(message):
    if message.channel.id == channelid:
        # message.channel.send(message.content)
        if str(serverid) == str(message.guild.id):
            if 'https://' in message.content:   
                url = message.content
                r = requests.get(url)
                filename = f"사진/img.png"
                with open(filename, 'wb') as out_file:
                    out_file.write(r.content)
                    role = discord.utils.get(message.guild.roles, name="인증역할") 
                    await message.author.add_roles(role)

        #         await message.channel.send(pytesseract.image_to_string('사진/img.png', lang='kor+eng', config='-c preserve_interword_spaces=1 --psm 4'))
        #         # await message.channel.send(file=discord.File(f"사진/img.png"))

            
# Addyout BOT TOKEN here
bot.run("")