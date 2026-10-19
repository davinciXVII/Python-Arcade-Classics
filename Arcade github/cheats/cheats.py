import telebot
import re
import sqlite3
SAVE_PATTERN=r"%save\s*((\w+\s*)+) - ((\w+\s*)+) - ((\w+\s*)+)" #pattern for load
LOAD_PATTERN=r"%load\s*((\w+\s*)+)" 
DELETE_PATTERN=r"%delc\s*((\w+\s*)+) - ((\w+\s*)+)"
DELETE_GAME_PATTERN=r"%delg\s*((\w+\s*)+)"
def decor_db(func):
    def wrapper(*args):
        connector=sqlite3.connect("cheats.db")     
        cursor=connector.cursor()
        result=func(*args,cursor=cursor)
        connector.commit()
        connector.close()
        return result
    return wrapper
token="8436164216:AAH9-VTk1mKnunEmqOQaCrA6wXRZhihExUc"
bot=telebot.TeleBot(token)
@decor_db
def delete_from_table(name,code,cursor):
    if code:
        cursor.execute(f"SELECT * FROM cheats WHERE name='{name}' AND code='{code}' ")
        if not cursor.fetchall():
            return False
        cursor.execute(f"DELETE FROM cheats WHERE name='{name}' AND code='{code}' ")
        return True
    else:
        cursor.execute(f"SELECT * FROM cheats WHERE name='{name}' ")
        if not cursor.fetchall():
            return False
        cursor.execute(f"DELETE FROM cheats WHERE name='{name}' ")
        return True


@decor_db
def load_from_table(name,cursor):
    cursor.execute(f"SELECT * FROM cheats WHERE name='{name}' ")
    return cursor.fetchall()
@decor_db
def save_into_table(name,code,info,cursor):
    cursor.execute(f"INSERT INTO cheats(name,code,info) VALUES('{name}','{code}','{info}')")
@decor_db
def create_table(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS cheats(name TEXT,code TEXT,info TEXT)')
create_table()


@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(msg.chat.id,"!!! The hyphen is part of the command!!!\nSaving a cheat code:\n%save game name - cheat code - description" \
    "\nLoading a cheat code:\n%load game name \nDeleting a cheat code:\n%delc game name - cheat code \nDeleting a game"
    "\n%delg game name")

@bot.message_handler(content_types=["text"])
def answer(msg):
    for pattern,func in zip(patterns,funcs):
        if re.match(pattern,msg.text):
            func(re.match(pattern,msg.text),msg)
            break
    else:
        bot.send_message(msg.chat.id,"error command /help")


def save(mo,msg):
    name,code,info=mo.groups()[0],mo.groups()[2],mo.groups()[4]
    save_into_table(name,code,info)
    bot.send_message(msg.chat.id,"data saved")
    
def load(mo,msg):
    name=mo.groups()[0]
    result=load_from_table(name)
    if not result:
        bot.send_message(msg.chat.id,"game was not founded ")
    else:
        bot.send_message(msg.chat.id,f"there are saved codes for a game {name}")
    for _,code,info in result:
        bot.send_message(msg.chat.id,f"{code} - {info}")
    
def dellc(mo,msg):
    name,code=mo.groups()[0],mo.groups()[2]
    result=delete_from_table(name,code)
    if result:
        bot.send_message(msg.chat.id,"code was deleted")
    else:
        bot.send_message(msg.chat.id,"code was not founded")
    
def dellg(mo,msg):
    name=mo.groups()[0]
    result=delete_from_table(name,None)
    if result:
        bot.send_message(msg.chat.id,"game was deleted")
    else:
        bot.send_message(msg.chat.id,"game was not founded")

patterns=(SAVE_PATTERN,LOAD_PATTERN,DELETE_PATTERN,DELETE_GAME_PATTERN)
funcs=(save,load,dellc,dellg)
    

bot.polling()

