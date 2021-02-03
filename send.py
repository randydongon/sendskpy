from skpy import Skype
import sys
import os
import re
sys.dont_write_bytecode = True

args = []
try:
    args = sys.argv[:]


except Exception as e:
    print(e)
    exit()


def sendMsg(id, content):

    sk = Skype('', '')

    if re.findall('19', id):
        ch = sk.chats[id]
        ch.sendMsg(content)

        print('group message')
    else:
        ch = sk.contacts[id].chat
        ch.sendMsg(content)
        print('single chat')

    # print(id)


def checkarguments():
    if len(args) < 3 or len(args) > 3:
        print(f"Sype message takes ID and Message")
        print(args[1:])
        return

    id, content = args[1:]
    sendMsg(id, content)


checkarguments()


