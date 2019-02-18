import botpie
import random

message = botpie.utils.argvstr()
bot = botpie.Bot("ImportantBot")

def tracer():
    greets = ["hiya!", "heya!", "hi!", "hoiya!"]
    return random.choice(greets)

bot.addcommand("tracer", handler=tracer)
result = bot.inspectstr(message)

if result:
    print(result)