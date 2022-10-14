import os
import logging
import datetime
import json
import aiohttp
import disnake
from disnake.ext import commands

config = json.load(open('config.json')) 

logging.basicConfig(level=logging.INFO,
                    format = f'\x1b[30;1m%(asctime)s\x1b[0m %(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m %(message)s',
                    encoding='utf-8',
                    datefmt = '%Y-%m-%d %H:%M:%S',
                    style= '%')
logger = logging.getLogger('disnake')

    
bot = commands.AutoShardedBot(
  command_prefix=config["Prefix"],
  intents = disnake.Intents.all(),
  activity=disnake.Streaming(name="Mèo Simmy Xinh Đẹp ❤️" , url="https://twitch.tv/mba_k7"),
  help_command=None,
  test_guilds=[986813940606570546],
  sync_commands_debug=True
  )

bot.launch_time = datetime.datetime.utcnow()
bot.time = datetime.datetime.now().strftime('\x1b[30;1m%Y-%m-%d %H:%M:%S')
@bot.event
async def on_ready():
  print(bot.time, f'\033[1;36;40m{bot.user} đã hoạt động!')

@bot.event
async def on_command_error(ctx, error, **kwargs): 
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.CommandOnCooldown):
      message = f"Pls Wait** {round(error.retry_after, 1)}s** Nu Spam Baka!!!><"
    elif isinstance(error, commands.MissingPermissions):
      message = "No perm ?"
    elif isinstance(error, commands.MissingRequiredArgument):
      return
    elif isinstance(error, commands.errors.NSFWChannelRequired):
      message = "**NSFW channel When**"
    else:
      raise error
    await ctx.reply(message, delete_after=5, mention_author=False)
    
for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
      try:
         bot.load_extension(f"Cogs.{filename[:-3]}")
         logger.info(f"đã load {filename}")
      except Exception as e:
        raise e
def main():
  try:
     bot.run(config['Token'], reconnect=True)
  except aiohttp.ClientConnectorError:
    print("\033[1;31;40mMất Kết Nối Đến Máy Chủ")
  except RuntimeError:
    logger.info("log out")
if __name__ == '__main__':
  main()
