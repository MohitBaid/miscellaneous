import win32com.client as wincl
def text2speech(text):
	speak = wincl.Dispatch("SAPI.SpVoice")
	speak.Speak(text)

print ( " Enter Input " )
s = input()
text2speech(s)

	