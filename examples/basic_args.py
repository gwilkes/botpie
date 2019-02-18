import botpie

message = botpie.utils.argvstr()

def sens(game):
    gamesens = {
        "ow": "2.1",
        "cod": "3",
        "d2": "4"
    }
    sens = gamesens.get(game)
    if sens:
        return "{} mouse sensitivity is {}".format(game, sens)

bot = botpie.Bot("InfoBot", add_help=True)
cmd = bot.addcommand("sens", handler=sens)
cmd.addargument("game", default="ow", nargs="?", help="pick a game")

result = bot.inspectstr(message)

if result:
    print(result)