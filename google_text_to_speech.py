import os
from gtts import gTTS

text_data = \
"""



concert


"""

#Saving part starts from here
tts = gTTS(text_data, lang='en')
tts.save("saved_file.mp3")
print("File saved!")

#Playing Audio File
print("Playing Audio")
os.system("saved_file.mp3")
print("Done Playing")
