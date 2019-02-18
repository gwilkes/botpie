# BotPie

A Python framework for managing chatbots - 0.0.1 (alpha)

## Install and Run

```
git clone https://github.com/gwilkes/botpie.git
cd botpie/
python setup.py install
```

## Features

#### Argument Parsing

BotPie handles command parsing by using the Python [argparse][] module to do
most of the work.

#### Mapping with Decorators

[argparse]: https://docs.python.org/3/library/argparse.html

## Basic Script

```
import botpie
import random

message = botpie.utils.argvstr()
bot = botpie.Bot("ImportantBot")

@bot.command("!tracer")
def tracer():
    greets = ["hiya!", "heya!", "hi!", "hoiya!"]
    return random.choice(greets)

result = bot.inspect(message)

if result:
    print(result)
```

## Work In Progress

This is a lightweight initial release which does not include several of the desired features yet. Here are some of the plans for future releases:
*   Asynchronous support
*   Optional storage solution for Bot data

Other todos:
*   Fix docstrings
*   Include a better example for above (show off decorators, use discord connection, etc)

## Requirements

Python 3.7+ (this *may* change down the road to support older versions)