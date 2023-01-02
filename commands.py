import re
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from torch import autocast
import torch
from diffusers import StableDiffusionPipeline
from parameters import USE_AUTH_TOKEN



def dummy(images, **kwargs):
    return images, False


pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16, use_auth_token=USE_AUTH_TOKEN)
pipe = pipe.to("cuda")  
pipe.safety_checker = dummy



def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("use /draw <prompt> to create images. use /draw <sed>_<prompt> to specify a seed")





def dibuja(update: Update, context: CallbackContext) -> None:
    if update.message.text.lower() == "/draw":
        return

    new_frase = update.message.text.lower().replace("/draw", "").strip()+ "\n"



    g = torch.Generator()
    random_seed = g.seed()

    if len(new_frase.split('_')) == 2:
        random_seed, new_frase = new_frase.split('_')
        random_seed = int(random_seed)


    generator = torch.Generator("cuda").manual_seed(random_seed)
    prompt = new_frase.strip()
    print("*"*20)
    print(prompt)

    username = update.message.from_user.username
    
    user_id = update.message.from_user.id
    
    with open('logs.txt', 'a') as f:
        f.write(f"{user_id}, {username}, {prompt} \n")


    with autocast("cuda"):
        image = pipe(prompt, num_inference_steps=100, generator=generator)["sample"][0]  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
        


    # Now to display an image you can do either save it such as:
    image.save(f"sample_difussion.png")
    update.message.bot.send_photo(update.message.chat.id ,open('sample_difussion.png','rb'))
    update.message.reply_text(f"seed: {random_seed}")



def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("use /draw <prompt> to create images. use /draw <sed>_<prompt> to specify a seed")

commands = [("start", start),
            ("draw",dibuja),
            ("help", help)
            ]


if __name__ == "__main__":
    pass

