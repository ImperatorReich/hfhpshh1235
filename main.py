#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep


with open(r"config.txt",'r') as file:
    global api_id
    global api_hash
    global bindchat
    global outchat
    global bindlink
    line = file.readlines()
    line = [line.rstrip() for line in line]
    print("api_id - "+line[0]+"\n"+"api_hash - "+line[1]+"\n"+"bindchat - "+line[2]+"\n"+"outchat - "+line[3]+"\n"+"bindlink - "+line[4])
    api_id = int(line[0])
    api_hash = str(line[1])
    bindchat = int(line[2])
    outchat = int(line[3])
    bindlink = str(line[4])


app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command(['id'], prefixes='.') & filters.me)
def id(_,msg):
    from_chat = msg.reply_to_message.forward_from_chat.id
    title = msg.reply_to_message.forward_from_chat.title
    app.send_message(msg.chat.id, 'айди чата (' + title+ ') : '+str(from_chat) )
    msg.delete()

@app.on_message(filters.command(['ins'], prefixes='.') & filters.me)
def ins(_,msg):
    print(msg)


@app.on_message(filters.chat(bindchat))
def sendd(_,msg):
    print(msg)
    print(msg.entities)
    # if msg.caption_entities or msg.entities == None:
    #     app.copy_message('me', msg.chat.id, msg.message_id)
    # else:
    ofseti = 0
    try:
        for typ in msg.caption_entities or msg.entities:
            print(typ.type)
            tipi = str(typ.type)
            # print(typ.offset)
            if tipi == "MessageEntityType.TEXT_LINK":
                print('yes')
                ofseti = typ.offset
                print(ofseti)

        if msg.media_group_id != None:
            arsen = app.copy_media_group(outchat, msg.chat.id, msg.message_id)
            # print(arsen)
            for cpt in arsen:
                if cpt.caption != None:
                    cpt.edit(msg.caption[:ofseti] + '\n' + bindlink)
        else:
            arsen = app.copy_message(outchat, msg.chat.id, msg.message_id)
            try:
                arsen.edit(msg.text[:ofseti] + '\n' + bindlink)
            except:
                try:
                    arsen.edit(msg.caption[:ofseti] + '\n' + bindlink)
                except Exception as e:
                    print(e)
                # msg.text[:ofseti] or
    except Exception as e:
        print('TRURNED')
        print(e)
        #app.copy_message('me', msg.chat.id, msg.id)







# @app.on_message(filters.chat(bindchat))
# def senddd(_,msg):
#     for typ in msg.caption_entities or msg.entities:
#         print(typ.type)
#         tipi = str(typ.type)
#         # print(typ.offset)
#         if tipi == "MessageEntityType.TEXT_LINK":
#             print('yes')
#             ofseti = typ.offset
#             print(ofseti)
#     arsen = app.copy_media_group('me', msg.chat.id, msg.id)
#     print(arsen)
app.run()
