import os 
import sys
import disnake
import datetime
sys.stderr = open(os.devnull, "w")
import psutil
sys.stderr = sys.__stderr__

from disnake.ext import commands
class Slash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  
  @commands.slash_command(name="stats", description="mmbeo")
  async def _stats(self, inter):
    delta_uptime = datetime.datetime.utcnow() - self.bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    cpu = psutil.cpu_percent() / psutil.cpu_count()
    ram = psutil.Process().memory_full_info().uss / 1024**2
    embed = disnake.Embed(color=0x2e3135)
    embed.set_author(name="Shinee Bot Stats", icon_url=self.bot.user.display_avatar)
    embed.add_field(
      name="Béo", 
      value=f"<a:emoji_61:1024266757239734272> Server : **{len(self.bot.guilds)}**\n<:emoji_62:1024269647798870026> Member : **{len(list(self.bot.get_all_members()))}**")
    embed.add_field(
      name="Version",
      value="<:emoji_55:1024245812798177300> Bot Version : **1.1.6**\n<:emoji_56:1024248038891466822> Python Version : **3.8.0**\n<:emoji_57:1024248690971525160> Disnake Version : **[2.6.0](https://github.com/DisnakeDev/disnake)**"
    )
    embed.add_field(
      name="Dit Me May" ,
      value=f"<:emoji_60:1024266720585719869> Cpu : {cpu}%\n<:emoji_60:1024266720585719869> Ram : {round(ram)} MB\n<:emoji_60:1024266720585719869> Websocket Latency : {round(self.bot.latency * 1000)} ms")
    embed.add_field(name="<a:emoji_59:1024261581112082472> Uptime", value=f"```python\n{days} Day, {hours} Hours, {minutes} Minutes, {seconds} Seconds\n```")
    await inter.response.send_message(embed=embed)
    
  @commands.slash_command(name="source", description="dit vao mom em")
  async def _source(self, inter):
    await inter.response.send_message(content="https://github.com/nevwex/nsfwbot")
    
    
  @commands.slash_command(name="text", description="dit vao mom em")
  async def text(self, inter,*,text, member:disnake.Member):
    await inter.response.send_message("ok(mất 1 chút tgian để bot send", ephemeral=True)
    webhook = await inter.channel.create_webhook(name=member.name, avatar=member.avatar)
    await webhook.send(text)
    
def setup(bot):
  bot.add_cog(Slash(bot))