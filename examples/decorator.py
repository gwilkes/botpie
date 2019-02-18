import botpie
import random

message = botpie.utils.argvstr()
bot = botpie.Bot("ImportantBot")

@bot.command("tracer")
def greeter():
    greets = ["hiya!", "heya!", "hi!", "hoiya!"]
    return random.choice(greets)

result = bot.inspectstr(message)

if result:
    print(result)