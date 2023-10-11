import asyncio
import os
import discord
import openai

from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
openai.api_key = os.environ["OPEN_AI_KEY"]

bot = commands.Bot(intents = intents, command_prefix='/')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.slash_command(name='makeparty', description='Create a party for an RPG')
async def rpGPT_make_party(ctx, platform: str, members: int):
    await ctx.respond(f"Generating party for {ctx.author.mention}...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "You will create a balanced party using a specified number of members for the specified platform. "
                 "Include each name, race, class, and a 2 sentence backstory."},
                {"role": "user", "content": f"Platform: {platform}, members: {members} "}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} your party has been generated:\n\n{response}")

@bot.slash_command(name='encounter', description='Create a random encounter for your party')
async def rpGPT_encounter(ctx, platform: str, setting: str, members: int, level: int):
    await ctx.respond(f"Generating an encounter for {ctx.author.mention}...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1999,
            messages = [
                {"role": "system", "content": "You will create a 3 paragraph rpg encounter introduction based on the given information."},
                {"role": "user", "content": f"Platform: {platform}, Setting: {setting}, Members in Party: {members}, Party Level: {level} "}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} your encounter has been generated: \n\n{response}")

@bot.slash_command(name='backstory', description='Create a backstory for your rpg character')
async def rpGPT_backstory(ctx, name: str, _class: str, race: str, alliance="Neutral", personality = "calm and outgoing"):
    await ctx.respond(f"{ctx.author.mention} your backstory is being generated...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "You will create an rpg backstory given the following information. "
                 "Include each name, race, class, and a 2 sentence backstory."},
                {"role": "user", "content": f"Name: {name}, class: {_class}, race: {race}, alliance: {alliance}, personality: {personality} "}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} your backstory is complete:\n\n {response}")

@bot.slash_command(name='bard', description='Make the bard write a song. Add your character\'s names and classes for flavor!')
async def rpGPT_bard(ctx, characters_involved: str):
    await ctx.respond(f"{ctx.author.mention} your song is being generated...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "You will create a song written by a bard in a classic rpg style. The song should be less than 2000 characters including newlines. If 'Characters Involved: Any' then make up your own names. Otherwise use the names provided."},
                {"role": "user", "content": f"Characters Involved: {characters_involved}"}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} here is your new epic song: \n\n{response}")

@bot.slash_command(name='npc', description='Let rpGPT-bot generate your npc\'s on the fly!')
async def rpGPT_npc(ctx, platform: str, number_of_names_to_generate: int):
    await ctx.respond(f"{ctx.author.mention} your names are being generated...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 500,
            messages = [
                {"role": "system", "content": "You will create names for npc's given a platform, and a number of names to generate. Include their name and race."},
                {"role": "user", "content": f"Game: {platform}, Number of names to generate: {number_of_names_to_generate}"}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} here is/are your name(s)... \n\n{response}")

@bot.slash_command(name='quest', description='Get a quick quest-hook')
async def rpGPT_quest(ctx, platform: str):
    await ctx.respond(f"{ctx.author.mention} your quest is being imagined...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "Create a single sentence quest-hook for the provided platform. The quest should be either given by someone you name, or something from a rumor."},
                {"role": "user", "content": f"Platform: {platform}"}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} here is your new quest...\n\n {response}")

@bot.slash_command(name='town', description='Let rpGPT-bot create your town and its rumors! Use small/medium/large/huge for town sizes.')
async def rpGPT_town(ctx, platform: str, size_of_town: str):
    await ctx.respond(f"{ctx.author.mention} your new town is being built...", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "Describe a town for the given platform. Include rumors, lore, and/or legends. Use only 3 paragraphs."},
                {"role": "user", "content": f"Platform: {platform}, Town Size: {size_of_town}"}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} your town has been constructed: \n\n{response}")

@bot.slash_command(name='townsum', description='Just like the /town command, but just the bullet points.')
async def rpGPT_townsum(ctx, platform: str, size_of_town: str):
    await ctx.respond(f"{ctx.author.mention} your town summary is being constructed... ", ephemeral=True)
    async with ctx.typing():
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            temperature = 0.9,
            max_tokens = 1500,
            messages = [
                {"role": "system", "content": "Describe a town for the given platform. Include rumors, lore, and/or legends. Create 10 short bullets or less, with each bullet less than 3 sentences."},
                {"role": "user", "content": f"Platform: {platform}, Town Size: {size_of_town}"}
                ]
            )
        response = completion['choices'][0]['message']['content']
        await asyncio.sleep(10);
    await ctx.send(f"{ctx.author.mention} here is the summary of your new town:\n\n{response}")


bot.run(TOKEN)