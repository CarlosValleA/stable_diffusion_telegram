import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from commands import caracola
import demoji

demoji.download_codes()

def once(update: Update, msg) -> bool:
    x = re.search(r".*11$|.*11 |.*11(\!|\?|\_)+", msg)
    y = re.search(r".*once$|.*once |.*once(\!|\?|\_)+", msg)
    if x!= None or y != None:
        update.message.reply_text("Chupalo entonce")
        return True 

    if "10+1" in msg:
        update.message.reply_text("Chupalo igual")
        return True 
    
    if "12-1" in msg:
        update.message.reply_text("Siguelo chupando")
        return True 

    return False

def trece(update: Update, msg) -> bool:
    x = re.search(r".*13$|.*13 |.*13(\!|\?|\_)+", msg)
    y = re.search(r".*trece$|.*trece |.*trece(\!|\?|\_)+", msg)
    if x!= None or y != None:
        update.message.reply_text("Más me crece")
        return True 

    if "12+1" in msg:
        update.message.reply_text("Te crei vio")
        return True 

    if "14-1" in msg:
        update.message.reply_text("Usted no aprende")
        return True 
    return False

def nacho(update: Update, msg) -> bool:
    palabras = ["oe nacho",
                "oye nacho"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Agarrame el cacho")
        return True 
    return False

def napa(update: Update, msg) -> bool:
    palabras = ["oe napa",
                "oye napa",
                "oe nappa",
                "oye nappa"]

    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Agarra el caeza e papa")
        return True 
    return False

def nico(update: Update, msg) -> bool:
    palabras = ["oe nico",
                "oye nico"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Agarrame el pico")
        return True 
    return False

def correteado(update: Update, msg) -> bool:
    palabras = ["correteado"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Quizás quiso decir *Nico*?", parse_mode='MarkdownV2')
        update.message.reply_text("o tal vez quiso decir *Pablo*?", parse_mode='MarkdownV2')

        return True 
    return False


def promesa(update: Update, msg) ->bool:

    palabras = ["cual promesa",
                "cual promesa?",
                "cual promesa ?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("La de chuparme el pico bajo la mesa")
        return True
    return False

def foto(update: Update, msg) ->bool:

    palabras = ["que foto",
                "cual foto"
                "que foto?",
                "que foto ?",
                "cual foto?",
                "cual foto ?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("La de mi pico en tu poto")
        return True
    return False

def quien(update: Update, msg) ->bool:
    palabras = ["quien?",
                "quien ?"]

    palabras2 = ["who ?",
                "who?"]

    palabras3 = [  "kien?",
                "kien ?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Quien te pregunto?")
        return True

    if any([(p in msg) for p in palabras2]):
        update.message.reply_text("Who ask you?")
        return True

    if any([(p in msg) for p in palabras3]):
        update.message.reply_text("kien te pregunto?")
        return True


    return False

def bienecha(update: Update, msg) ->bool:

    palabras = ["una cosa bien hecha?",
                "una cosa bien hecha ?",
                "una cosa bien echa?",
                "una cosa bien echa ?",
                "una wea bien echa ?",
                "una wea bien echa?",
                "una wea bien hecha?",
                "una wea bien hecha ?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Agarrame el pico e'las mechas!!!")
        return True
    return False

def kya(update: Update, msg) ->bool:
    palabras = ["kya",
                "kyaa",
                "kyaaa",
                "kyaaaa",
                "kyaaaaa",
                "kyaaaaaa"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Yamete kudasai")
        return True
    return False

def rodrigo(update: Update, msg) -> bool:
    palabras = ["que rodrigo",
                "cual rodrigo",
                "que rodrigo ?",
                "que rodrigo?",
                "cual rodrigo ?",
                "cual rodrigo?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Si me lo chupai te lo digo")
        return True 
    return False

def fiesta(update: Update, msg) -> bool:
    palabras = ["cual fiesta",
                "que fiesta" ,
                "que fiesta ?",
                "que fiesta?",
                "cual fiesta ?",
                "cual fiesta?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("La de tu culo con esta")
        return True 
    return False

def accidente(update: Update, msg) -> bool:
    palabras = ["cual accidente",
                "que accidente" ,
                "que accidente ?",
                "que accidente?",
                "cual accidente ?",
                "cual accidente?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("el de mi pico en tu frente")
        return True 
    return False

def loca(update: Update, msg) -> bool:
    palabras = ["se volvio loca"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Mi tula en tu boca")
        return True 
    return False

def enojado(update: Update, msg) -> bool:
    palabras = ["enojado?",
                "enojado ?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Ven y chupa al pelao")
        return True 
    return False

def caracolaText(update: Update, msg) -> bool:
    palabra = "caracola"
    if  palabra in msg:
        caracola(update,CallbackContext)
        return True 
    return False

def risa(update: Update, msg) -> bool:
    palabra = "caracola"
    emojis = demoji.findall(msg)

    for emoji,description in emojis.items():
        if description in 'face with tears of joy' or description in 'rolling on the floor laughing':
            update.message.reply_text("Que te reí aweonao")
            return

def rietebien(update: Update, msg) -> bool:
    palabras = ["jso"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Riete bien aweonao")
        return True 
    return False


def funa(update: Update, msg) -> bool:
    palabras = ["cual funa",
                "que funa" ,
                "que funa ?",
                "que funa?",
                "cual funa ?",
                "cual funa?"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Donde chupai el pico como tuna")
        return True 
    return False

def temblor(update: Update, msg) -> bool:
    palabras = ["temblor",
                "terremoto"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("No llores Nico")
        return True 
    return False

def perro(update: Update, msg) -> bool:
    palabras = ["perro"]
    if any([(p in msg) for p in palabras]):
        update.message.reply_text("Tranquilo Ale es solo la palabra. Guau guau")
        return True 
    return False


p_comebacks = [once, trece, nacho, napa, nico, promesa, foto, bienecha, quien, kya, rodrigo, fiesta, accidente, loca, enojado, funa, temblor, perro, caracolaText,risa,rietebien,correteado ]
p_comebacks = []
def comebacks(update:Update, contex: CallbackContext) -> None:
    msg = update.message.text.lower()
    #msg = unidecode.unidecode(msg)
    for cbk in p_comebacks:
        if cbk(update, msg):
            return None