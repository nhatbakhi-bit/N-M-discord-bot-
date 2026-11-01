import discord
from discord import app_commands
import random

TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name="roll", description="Tung 3 xúc xắc")
async def roll(interaction: discord.Interaction):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)

    result = "TÀI" if total >= 11 else "XỈU"

    await interaction.response.send_message(
        f"🎲 Kết quả: {dice[0]} - {dice[1]} - {dice[2]}\n"
        f"🔢 Tổng: {total}\n"
        f"🎯 {result}"
    )

@tree.command(name="help", description="Xem hướng dẫn")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🎲 BOT XÚC XẮC\n/roll - Tung xúc xắc\n/help - Trợ giúp"
    )

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot online: {bot.user}")

bot.run(TOKEN)
