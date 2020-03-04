import os
import re
from gtts import gTTS
from gtts.lang import tts_langs

input_text = \
"""

σ

"""

langs = tts_langs('com')
# print( 'langs', langs ); raise

languages = [
    'en',
    'el',
    'pt-br',
]

trimmed_text =  re.sub( r'\s', '', input_text )[:50]

for lang in languages:
    filename = "D:\\User\\Downloads\\gtts_%s_%s.mp3" % ( trimmed_text, lang )

    tts = gTTS( input_text, lang=lang )
    tts.save( filename )

    print( "Playing Audio '%s'" % filename )
    os.system( filename )
