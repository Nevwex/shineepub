from disnake.ext import commands
class NoPreFix(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.content == "<@975380767809110116>":
      await message.reply("Prefix is `M` or `m` ||secks||")
    
def setup(bot: commands.Bot):
  bot.add_cog(NoPreFix(bot))