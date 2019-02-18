import botpie
import random

message = botpie.utils.argvstr()
bot = botpie.Bot("InfoBot")

@bot.command("sens")
@bot.argument("game", default="ow", nargs="?", help="pick a game")
def sens(game):
    gamesens = {
        "ow": "2.1",
        "cod": "3",
        "d2": "4"
    }
    sens = gamesens.get(game)
    if sens:
        return f"{game} mouse sensitivity is {sens}"

result = bot.inspectstr(message)

if result:
    print(result)