import gtts
import pyaudio
import playsound
# Create a gTTS object.
tts = gtts.gTTS(text="Hola, mundo!", lang='es')

# Save the voice code as an MP3 file.
tts.save("hola.mp3")
 

# Play the MP3 file.
playsound.playsound("hola.mp3")