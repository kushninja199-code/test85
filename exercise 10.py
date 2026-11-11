import win32com.client
l=("aarav","Kushagra","naman","bunty")
speaker=win32com.client.Dispatch("SAPI.spVoice")
voice=speaker.GetVoices()
speaker.Voice = voice.Item(0)
for i in l:
    speaker.speak(f"shoutout  to {i}")