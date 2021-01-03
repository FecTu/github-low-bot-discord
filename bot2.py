import discord
import asyncio
import random
from random import randint , choice
from discord import Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from tabulate import tabulate
import datetime, pyowm
import speech_recognition as sr
from discord.utils import get
import youtube_dl
import shutil
import traceback
import sqlite3
import validators
import nekos
import json

import os
from time import sleep
import requests

PREFIX = "."
bad_words = [ "нахуй", "бунт", "лох", "пидр", "долбаеб", "пидар", "пидарас", "пидор", "пидорас" ]

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( "help" )

@client.event
async def on_ready():
    print("""
               ░██████╗████████╗░█████╗░██████╗░████████╗  ░██████╗██╗░░██╗██╗███████╗██╗░░░██╗██╗░░██╗██╗
               ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██║░░██║██║╚════██║██║░░░██║██║░██╔╝██║
               ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  ╚█████╗░███████║██║░░███╔═╝██║░░░██║█████═╝░██║
               ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ░╚═══██╗██╔══██║██║██╔══╝░░██║░░░██║██╔═██╗░██║
               ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ██████╔╝██║░░██║██║███████╗╚██████╔╝██║░╚██╗██║
               ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝
""")
    print("""
    
            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ░██████╗░█████╗░██████╗░░█████╗░
            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗
            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ╚█████╗░██║░░██║██████╔╝███████║
            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░╚═══██╗██║░░██║██╔══██╗██╔══██║
            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██████╔╝╚█████╔╝██║░░██║██║░░██║
            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝

        """)
    await client.change_presence( status= discord.Status.online, activity= Activity( name= "Патруль", type=ActivityType.watching))

#Autorole
@client.event
async def on_member_join(member):
    role = disocrd.utils.get(member.guild.roles, id =795314312281063425)
    await member.add_roles(role)

#NSFW
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

@client.command()
@is_nsfw()
async def neko(ctx):
    emb = discord.Embed( title ="Neko", color = 0x1100ff )
    emb.set_image(url=nekos.img("nsfw_neko_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def yuri(ctx):
    emb = discord.Embed( title = "Yuri", color = 0x1100ff )
    emb.set_image(url=nekos.img("les"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def hentai(ctx):
    emb = discord.Embed( title = "Hentai", color = 0x1100ff )
    emb.set_image(url=nekos.img("Random_hentai_gif"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed( title = "Cum", color = 0x1100ff )
    emb.set_image(url=nekos.img("cum"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def pussy(ctx):
    emb = discord.Embed( title = "Pussy", color = 0x1100ff )
    emb.set_image(url=nekos.img("pwankg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def feet(ctx):
    emb = discord.Embed( title = "Feet", color = 0x1100ff )
    emb.set_image(url=nekos.img("feetg"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def cuddle(ctx):
    emb = discord.Embed( title = "Cuddle", color = 0x1100ff )
    emb.set_image(url=nekos.img("cuddle"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def solo(ctx):
    emb = discord.Embed( title = "Solo", color = 0x1100ff )
    emb.set_image(url=nekos.img("solog"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def kemo(ctx):
    emb = discord.Embed( title = "Kemo", color = 0x1100ff )
    emb.set_image(url=nekos.img("erokemo"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def kuni(ctx):
    emb = discord.Embed( title = "Kuni", color = 0x1100ff )
    emb.set_image(url=nekos.img("kuni"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def loli(ctx):
    emb = discord.Embed( title = "Loli", color = 0x1100ff )
    emb.set_image(url=nekos.img("smallboobs"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def blowjob(ctx):
    emb = discord.Embed( title = "Blowjob", color = 0x1100ff )
    emb.set_image(url=nekos.img("blowjob"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def anal(ctx):
    emb = discord.Embed( title = "Anal", color = 0x1100ff )
    emb.set_image(url=nekos.img("anal"))
    emb.set_footer( text = f"Вызвано:{ctx.message.author}", icon_url= ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@client.command()
@is_nsfw()
async def nsfw(ctx):
    emb = discord.Embed( title= "Команды NSFW", color = 0x1100ff )
    emb.add_field( name= "{}neko".format( PREFIX ), value= "Кошки-девочки", inline= True)
    emb.add_field( name= "{}yuri".format( PREFIX ), value= "Лезбиянки", inline= True)
    emb.add_field( name= "{}loli".format( PREFIX ), value= "Лоликон", inline= True)
    emb.add_field( name= "{}blowjob".format( PREFIX ), value= "Работает ротиком", inline= True)
    emb.add_field( name= "{}kuni".format( PREFIX ), value= "Лизать киску", inline= True)
    emb.add_field( name= "{}kemo".format( PREFIX ), value= "Няшки", inline= True)
    emb.add_field( name= "{}solo".format( PREFIX ), value= "Соло", inline= True)
    emb.add_field( name= "{}pussy".format( PREFIX ), value= "Киски", inline= True)
    emb.add_field( name= "{}feet".format( PREFIX ), value= "Красивые ношки", inline= True)
    emb.add_field( name= "{}hentai".format( PREFIX ), value= "Хентай", inline= True)
    emb.add_field( name= "{}anal".format( PREFIX ), value= "анал", inline= True)
    emb.add_field( name= "{}cum".format( PREFIX ), value= "Кончают", inline= True)
    emb.set_image( url = "https://danbooru.donmai.us/data/e71dc6de8c5c153e56ee179e5dc5d58f.gif")
    await ctx.send(embed = emb)

#Filter
@client.event
async def on_message( message ):
    await client.process_commands( message )

    msg = message.content.lower()

    if msg in bad_words:
        await message.delete()
        await message.author.send( f"{ message.author.mention }, Братик Бяка не матюкайся(")

#Private rooms
@client.event
async def on_voice_state_update( member, before, after,):
        if before.channel is None and after.channel.id == 795301881681412150:
            for guild in client.guilds:
                maincategory = discord.utils.get( guild.categories, id = 795301881681412148 )
                channel2 = await guild.create_voice_channel( name=f"Канал {member.display_name}", category = maincategory )
                await channel2.set_permissions(member, connect = True, mute_members = True, move_members = True, manage_channels = True)
                await channel2.edit(user_limit = 2)
                await member.move_to(channel2)
                def check(x,y,z):
                    return len(channel2.members) == 0
                await client.wait_for( "voice_state_update", check=check )
                await channel2.delete()

#Mute
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def mute(ctx, member:discord.Member ,time:int, reason = None):
    channel = client.get_channel(795318297104875530)
    muterole = discord.utils.get(ctx.guild.roles,id=795317719976771624)
    emb = discord.Embed( title= "Mute", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline=False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline=False )
    emb.add_field( name = "Причина", value = reason, inline=False )
    emb.add_field( name = "Время", value = time, inline=False)
    emb.set_thumbnail(url = member.avatar_url)
    await member.add_roles(muterole)
    await channel.send(embed = emb)
    await asyncio.sleep(time)
    await member.remove_roles(muterole)

#Unmute
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def unmute(ctx, member:discord.Member):
    channel = client.get_channel(795318297104875530)
    muterole = discord.utils.get(ctx.guild.roles,id=795317719976771624)
    emb = discord.Embed( title= "Unmute", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline=False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline=False )
    emb.set_thumbnail(url = member.avatar_url)
    await channel.send(embed = emb)
    await member.remove_roles(muterole)

#Kick
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
    channel = client.get_channel(795318297104875530)
    emb = discord.Embed( title= "Kick", color=0x1100ff )
    emb.add_field( name ="Администратор", value= ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value= reason, inline=False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.kick()
    await channel.send(embed = emb)

#Ban
@client.command( pass_context = True )
@commands.has_permissions( view_audit_log = True )
async def ban( ctx, member: discord.Member,time:int, reason = None ):
    channel = client.get_channel(795318297104875530)
    emb = discord.Embed( title= "Ban", color=0x1100ff )
    emb.add_field( name = "Администратор", value = ctx.message.author.mention, inline= False )
    emb.add_field( name = "Нарушитель", value = member.mention, inline= False)
    emb.add_field( name = "Причина", value = reason, inline= False)
    emb.add_field( name = "Время", value= time, inline= False)
    emb.set_thumbnail( url = member.avatar_url)
    await member.ban()
    await channel.send(embed = emb)

#Clear channel
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ):
    await ctx.channel.purge(limit = amount)
    channel = ctx.message.channel
    message = {}

@clear.error
async def clear_error( ctx, error ):

    if isinstance( error, commands.MissingPermissions ):
        await message.author.send( f"{ message.author.mention }, у вас не достаточно прав!" )

@client.event
async def on_command_error( ctx, error ):
    pass

# Get token
#token = open( "token.txt", "r").readline()

client.run(os.getenv('BOT_TOKEN'))