from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import random
import os


def check(user_answer, answer):
    if user_answer.lower() == answer.lower():
        return("correct",1)
    else:
        return("wrong the answer was: %s" % answer.lower(),0)

def Eng_to_Ja(list):
    num = random.randrange(0,len(list))
    eng_word = list[num]
    word = translator.translate(eng_word, dest='ja').text
    tts = gTTS(text=word, lang='ja')
    return (tts, eng_word)

def question(audio, i):
    try:
        os.remove("word" + str(i) + ".mp3")
    except:
        pass

    try:
        audio.save("word" + str(i) + ".mp3")
    except:
        pass
    playsound("word" + str(i) + ".mp3")
    os.remove("word" + str(i) + ".mp3")
    answer = input("What do you think this is: ")
    return(answer)

translator = Translator()
words = ["Hobby", "movies", "manga", "surfing", "picnic", "pet", "play with pet", "shopping", "Skype", "Skype call", "like", "love", "popular", "trending", "friend", "go shopping with friend", "Beach", "violin", "piano", "play", "violin", "book", "read book", "cycling", "party", "Cafe", "make friends", "I want to", "there is", "I want to", "because", "many", "I live in", "I was born in", "I have lived in", "weekend", "everyday", "Brisbane", "Melbourne", "Sydney", "Canberra", "gold coast", "Tasmania", "Tokyo", "Osaka", "Yokohama", "Hiroshima", "Nara", "when", "where", "why", "who", "what", "same", "different", "Japanese culture", "Japanese food", "more", "fashionable", "last year", "next year", "mother", "father", "older brother", "older sister", "younger brother", "younger sister", "son", "daughter", "family"]

wrong = []

AOW = int(input("Amount Of words: "))

correct = 0
incorrect = 0

for i in range(AOW):
    audio, eng_word = Eng_to_Ja(words)
    answer = question(audio, i)

    an,add = (check(answer, eng_word))
    print(an + "\n")
    correct += add
    if add == 0:
        wrong.append(eng_word)

print("correct: %s\nPercentage correct: %s" %(correct, correct/AOW*100))
print(wrong)

while True:
    if len(wrong) > 0:
        for i in range(len(wrong)):
            audio, eng_word = Eng_to_Ja(wrong)
            answer = question(audio, i)

            an,add = (check(answer, eng_word))
            print(an + "\n")
