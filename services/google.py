from unicodedata import name
from gtts import gTTS
import os

mytext = 'Welcome to geeksforgeeks!'
language = 'en'

#os.system("mpg321 welcome.mp3")

def converter(v_data):
    for i in v_data:
        instruction=i.instruction
        myobj = gTTS(text=instruction, lang=language, slow=False)
        name=str(i.r_id_id)+str(i.seq_no)
        myobj.save(name+".mp3")

