from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
from tkinter import messagebox
from chatterbot.trainers import ChatterBotCorpusTrainer

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()



bot = ChatBot("My Bot")
'''
convo =[
    "Hello",
    "Hi there!",
    "what is your name?",
    "my name is Vision,i am here to talk with you",
    "what can you do?",
    "i can answer you some general questions",


    "How are you doing?",
    "I'm doing great.",
    "how are you?",
    "i'm good",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
]'''
#
#trainer = ListTrainer(bot)

# now training the bot with the help of trainer
#
#trainer.train(convo)
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

main = Tk()

main.geometry("600x650")

main.title("'VISION'")
img = PhotoImage(file="jarvis3.png")
photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    # answer_from_bot=english_bot.get_response(query)
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="ASK ME",bg="light blue", fg="blue", font=("Cursive", 20), command=ask_from_bot)
btn.pack()
#btn2 = Button(main, text=" mic", font=("Verdana", 20), command=repeatL)
#btn2.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


def micstart():
    t=threading.Thread(target=repeatL)
    t.start()
    messagebox.showinfo('Mic started', 'Say Something')

btn2 = Button(main, text="MIC",bg="light blue", fg="blue", font=("Serif", 25), command=micstart)
btn2.pack(side=LEFT,pady=0)
# threading.Thread(target=repeatL)

#t.start()
def stop():
    print("bye! have a nice day")
    exit()
btn3 = Button(main, text="EXIT",bg="light blue", fg="red", font=("Serif", 25), command=stop)
btn3.pack(side=RIGHT,pady=0)


main.mainl