# Super simple example: just load and loop a stereo sound.
se = getSoundEnvironment()
if (se != None):
    sound = se.loadSoundFromFile('TRANCO', 'TRANCO.wav')
    soundInstance = SoundInstance(sound)
    soundInstance.setVolume(0.4)
    soundInstance.setLoop(True)
    soundInstance.setPitch(0.88)
    soundInstance.playStereo()
else:
    print("WARNING: Could not get sound environment. Is sound support enabled in your config file?")