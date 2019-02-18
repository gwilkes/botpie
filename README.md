# BotPie

[![version](https://img.shields.io/pypi/v/botpie.svg?style=flat)](https://pypi.org/project/botpie/)
[![python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-372/)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Python framework for managing chatbots (alpha)

`pip install botpie`

## Features

#### Argument Parsing

BotPie handles command parsing by using the Python [argparse][] module to do
most of the work.

[argparse]: https://docs.python.org/3/library/argparse.html

## Basic Script

```python
import botpie
import random

message = botpie.utils.argvstr()
bot = botpie.Bot("ImportantBot")

@bot.command("tracer")
def tracer():
    greets = ["hiya!", "heya!", "hi!", "hoiya!"]
    return random.choice(greets)

result = bot.inspectstr(message)

if result:
    print(result)
```
>   The above example was tested by running `python examples/basic.py tracer`

## Work In Progress

This is a lightweight initial release which does not include several of the desired features yet. Here are some of the plans for future releases:
*   Asynchronous support
*   Optional storage solution for Bot data
*   Interfaces for IRC, Twitch, and Discord

Other todos:
*   Fix docstrings
*   Include a better example for above (show off decorators, use discord connection, etc)