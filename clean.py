#!/usr/bin/python

import os
import discord
from discord.ext import commands

token   = " " # seu token aqui
prefixo = ";" # prefixo do clean

print("""
  ██╗███╗   ██╗ ██████╗  ██████╗███████╗███╗   ██╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     
  ██║████╗  ██║██╔═══██╗██╔════╝██╔════╝████╗  ██║╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  ██║██╔██╗ ██║██║   ██║██║     █████╗  ██╔██╗ ██║   ██║          ██║   ██║   ██║██║   ██║██║     
  ██║██║╚██╗██║██║   ██║██║     ██╔══╝  ██║╚██╗██║   ██║          ██║   ██║   ██║██║   ██║██║     
  ██║██║ ╚████║╚██████╔╝╚██████╗███████╗██║ ╚████║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
""")

os.system('color f')
os.system('color 9')

bot = commands.Bot(command_prefix=prefixo, self_bot=True)

@bot.command()
async def clean(ctx, limit: int=None):
   passed = 0
   failed = 0
   async for msg in ctx.message.channel.history(limit=limit):
       if msg.author.id == bot.user.id:
           try:
               await msg.delete()
               passed += 1
           except:
               failed += 1
   os.system('color f')
   print(f" [Finalizado] {passed} Mensagens removidas e {failed} com erro.")
   os.system('color 9')

bot.run(token, bot=False)
