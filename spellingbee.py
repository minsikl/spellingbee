from gtts import gTTS
from pygame import mixer

language = 'en'
words = open("words.txt", "r")
for word in words:
  input("Press any key to continue.")
  myobj = gTTS(text=word, lang=language, slow=False)
  myobj.save("word.mp3")
  mixer.init()
  mixer.music.load("word.mp3")
  mixer.music.play()
  while mixer.music.get_busy() == True:
    continue
  answer = input("Input your answer : ")
  if answer.strip() == word.strip():
    print("Correct.")
  else:
    print("Incorrect. The word is {}".format(word))
