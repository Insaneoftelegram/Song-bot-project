import discord
from discord.ext import commands
from moviepy.editor import *

bot = commands.Bot(command_prefix='!')

@bot.command()
async def convert_video(ctx, video_url: str):
    video = VideoFileClip(video_url)
    anime_filter = video.fx(vfx.colorx, 1.3)  # Apply anime filter
    anime_file_path = 'anime_video.mp4'
    anime_filter.write_videofile(anime_file_path, codec='libx264')  # Convert to anime video
    await ctx.send(file=discord.File(anime_file_path))

bot.run('YOUR_DISCORD_BOT_TOKEN')
