import sys
from api_communication import *

filename = "output.wav"

audio_url = upload(filename)
save_transcript(audio_url, filename)