import disnake
from disnake.ext import commands
class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
    
  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def help(self, ctx):
     cog = self.bot.get_cog('nsfw1')
     
     embed = disnake.Embed(title="Also use `Mnsfw` to see the new hentai images",description=', '.join(f"`{i.name}`" for i in cog.walk_commands()), color=0x2e3135)
     embed.set_author(name=f"The Nsfw commands | {len(cog.get_commands())}", icon_url="https://files.catbox.moe/ed73sp.png")
     embed.set_footer(text="Thank For Using!", icon_url=ctx.author.display_avatar)
     view = disnake.ui.View()
     view.add_item(item=disnake.ui.Button(label="Invite Me",style=disnake.ButtonStyle.link, url="https://discord.com/oauth2/authorize?client_id=975380767809110116&permissions=137439332416&scope=bot%20applications.commands", emoji="<:emoji_8:986828967300464650>"))
     await ctx.reply("đéo bt nói gì <:emoji_54:1021056235249864744>",embed=embed, mention_author=False, view=view)
def setup(bot):
  bot.add_cog(Help(bot))
  