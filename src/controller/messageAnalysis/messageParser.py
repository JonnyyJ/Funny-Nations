import os
import configparser
import re

from src.controller.messageAnalysis.checkBalance import checkBalance
from src.controller.messageAnalysis.getLeaderBoard import getLeaderBoardTop10
from src.controller.messageAnalysis.checkCashFlow import checkCashFlow
from src.controller.messageAnalysis.transferMoney import transferMoney

from src.controller.messageAnalysis.blackJack.newBlackJackGame import newBlackJackGame
from src.controller.messageAnalysis.blackJack.hit import blackJackHit
from src.controller.messageAnalysis.blackJack.stay import blackJackStay

from src.controller.messageAnalysis.liveGift import liveGift
from src.controller.messageAnalysis.joinGame import joinGame

from discord import Client, Message
from pymysql import Connection

from src.data.casino.Casino import Casino

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../../../config.ini')
commandPrefix = config['command']['prefix'] + ' '
commandPrefixLen = len(commandPrefix)


async def messageParser(self: Client, message: Message, db: Connection, casino: Casino):
    """
    Parse message
    Identify whether it is a command to this bot, or just a normal message
    :param casino:
    :param self: Discord's client object
    :param message: Message obj
    :param db: Database object
    :return: None
    """
    if message.content[:commandPrefixLen] != commandPrefix:
        return
    if len(message.content) > 100:
        await message.channel.send("你说的太长了")
        return
    command: str = message.content[3:]
    if re.match(f"^余额$", command):
        await checkBalance(message, db)
    if re.match(f"^富豪榜$", command):
        await getLeaderBoardTop10(self, message, db)
    if re.match(f"^账单$", command):
        await checkCashFlow(self, message, db)
    if re.match(f"^账单 .+", command):
        await checkCashFlow(self, message, db)
    if re.match(f"^转账 [0-9]+\.?[0-9]* \<\@\![0-9]+\>$", command):
        await transferMoney(self, db, message, command)
    if re.match(f"^礼物 (.+) [1-9][0-9]* \<\@\![0-9]+\>$", command):
        await liveGift(self, db, message, command)


    if re.match(f"^开局21点 [0-9]+\.?[0-9]*$", command):
        await newBlackJackGame(self, message, db, command, casino)
    if re.match(f"^要牌$", command):
        await blackJackHit(self, message, casino)
    if re.match(f"^停牌$", command):
        await blackJackStay(self, message, casino)


    if re.match(f"^加入$", command):
        await joinGame(self, message, db, casino)

