import time 

def MagicalArts(username):
    #You are now on a journey to pick your field of study. You now enter your first class, Magical arts (soon to be public health, 400 years from now); 
    #Magical arts: meets two evil guys, becomes discouraged, feels isolated. Meets a friend that encourages them
    guy1 = "Sephiroth"
    guy2 = "Bowser"
    friend1 = "Hermione"
    print("You have now entered your first class, Magical Arts. You have the choice to sit in the front of the class or in the back.")
    
    decision1 = input("Where would you like to sit? Choose either Front or Back \n")
    if decision1.lower() == 'front':
        print("You decided to sit in the front of the room. There, you meet two individuals.")
        print(guy1 + ": Oye! Why is this random princess in this class?!")
        print(guy2 + ": Right? This is not your playground missy.\n")
        print("You were having a hard time from the start. You thought that this journey would be filled with adventures and friends, but it was starting to seem much more than that.\n")
        print("You had no choice but to listen to the two evil men sitting beside you. Their judgemental looks were starting to become unbearable. But then...! \n")
        print("Unknown: Hello! May I sit next you?\n")
        decision2 = input("What is your answer?: Yes or No\n")
        if decision2.lower() == 'yes':
            print("Unknown: Thanks! My name is " + friend1 + ". What's yours?")
            print("You smile and give her your name.")
            print(friend1 + ": My god, those guys keep giving us nasty looks... Hey what\'s wrong?")
            print("Unknown: Thanks! My name is " + friend1 + ". What\'s yours?\n")
            decision3 = input("Reply to " + friend1 + "? Yes or No\n")
            if decision3.lower() == 'yes':
                print("Your sad face did not go away as you explained how your first day was going terribly and your feelings of discouragement.")
                print("Your new friend was shocked to hear how the two men treated you.")
                print(friend1 + ": They should not have said those things! I know you are strong, so stand up and face them! Show them how capable you are!\n")
                print("After hearing those encouraging words, your mood flipped and you began to feel excited once more!")
                print("Even if some people bring you down, there will always be others who support you!")
            else:
                print("Your sad face did not go away. You shook your head and decided to keep your feelings to yourself")
                print("Your new friend was taken aback by your silence")
                print(friend1 + ": If you ever need someone to talk to, I will be here. \n")
                print("You nodded. Soon class began and the rest of it was uneventful, besides the two men and their glaring stares.")
        else:
            print("You sat there uncomfortably as the girl in front of you walked away. \nThe rest of the class was uneventful, besides the two men and their glaring stares. ")
    else:
        print("You decided to sit in the back of the classroom. There, you meet two individuals.")
        print(guy1 + ": Oye! Why is this random princess in this class?!")
        print(guy2 + ": Right? This is not your playground missy.\n")
        print("You were having a hard time from the start. You thought that this journey would be filled with adventures and friends, but it was starting to seem much more than that...\n")
        print("You had no choice but to listen to the two evil men sitting beside you. Feelings of discouragement began to form and your mood plummeted. \n")
        print("Soon class began and the rest of it was uneventful, besides the two men and their glaring stares.")

        
def sharknado(username):
    prof = "Professor Jaws"
    guy = "Fin"
    print('You head to your next class, The Phenomenon behind Sharknados.\nYou really like the ocean and sharks are one of your favorite animals, so you\'re super excited for this class!\n')
    time.sleep(1)
    print(prof + ": We will be learning about how fish are both friends AND food. Does anyone know how to befriend a shark?\n")
    decision1 = input("How about Booping the snoot (A) or Feeding it bait (B)? (Please type A or B)\n")
    if decision1.upper()=="A":
        print(prof + ": Seriously? You don\'t know anything, I would be embarrassed to say that if I were you. How about someone else try?\n\n")
    else:
        print(prof + ": Wow, I can\'t believe you even suggested that. How about someone else try?\n\n")
    time.sleep(1)
    print(guy + ": We can lure out the shark with bait and then boop the snoot!\n")
    print(prof + ": What a wonderful idea!\n")
    time.sleep(1)
    print("It\'s a bit discouraging to hear that your ideas, voiced aloud by another classmate, gets a much better response.\n")
    decision2 = input("Do you want to drop the class? (Type Y/N)\n")
    if (decision2 =="Y") or (decision2 =="y"): 
        print("You decide to give up, but will you really let this professor stop you?\n")
        # pause time for three seconds
        print("...\n")
        time.sleep(3)
        print("You are filled with DETERMINATION anyways. Your confidence is restored, and you study really hard for this class.\n")
        print("You pass with flying colors!\n")
    else:
        print("You are filled with DETERMINATION and you are ready to slay to success.\n")
        print("You study really hard for this class and you pass with flying colors!\n")
                    
    return 0
        

def Potions101(username):
    labpartner = 'DK'
    print('It is now time to go to your third class of the day.\n')
    print('Before you go into class you decide to call your mom. Its been a long day and it would be nice to receive some comfort \n\n')
    print('The phone rings twice before your mom finally picks up. "Hi ' + username + '" , your mom says. You greet your mother back, and you begin to talk \nabout the extremely long and stressful day you\'ve had.\n')
    print('That sounds too hard ' + username +  '! You should be taking classes under the Holy studies! Those classes better fit your capabilites and skill range.\n')
    print('You are a bit shocked by what your mother told you. "Mom! I dont want to major in Holy studies. \n Princesses should be able to study and conquer what ever area of academia they desire!" \n')
    print('Your mom ignores what you said and instead asks you, "so what class are you taking next?"\n')
    print('Annoyed, you tell her that your next class is Potions101 and against your better judgement you begin to tell her how you heard that this class is incredibly hard.\n')
    print('Your mom cuts you off, '  + username + ' I already told you that you\'re wasting your time on these classes that are too hard for you. All you\'re going to do is give yourself a headache. Its better to stop now and take classes better suited for people like you.')
    print('"Mom! Why can\'t you ever support me!", you shout at your mom. \n')
    print('Your mom replies by telling you that all she wants is the best for you and asks you a question. \n"' + username + ' will you at least consider changing studies?"\n')
    response1 = input('Do you say yes or no? Type: Yes or No\n')
    if response1.lower == 'yes':
        print('Saying yes to your mom made you feel incredibly sad. You know that your heart is not in Holy studies. If you were to change studies, you know you would deeply regret your decisions. With a heavy heart, you head into class.')
    elif response1.lower == 'no':
        print('You know that you desire to challenge yourself and test your limits. While your mom\'s lack of support hurts, you have to keep pushing on!')
    print()
    print('Class starts and you rush to sit on an empty chair. You turn to your side, and greet the lab partner that you will have for the duration of the semester. \n')
    print(' "Hello! My name is ' + username + '". You say to your lab partner. They turn to look at you and smile back. \n')
    print(' "Hey! My name is ' + labpartner + '". He looks at you a bit longer and then asks if you\'re okay. \nYou guess that you must still look sad based on the call you had with your mother. \n')
    print('This might be oversharing but you decide to confide in your partner. While working through the lab procedures you begin to tell \nhim about the call you had with your mother. \n')
    print('At the end of your story he looks shocked. He tells you that your mother has no right to dictate your future.\n"Think about it ' + username + '. You have been leading us through this entire lab procedure!')
    print(' "It\'s because of your quick calculations that we have been able to finish up early. You clearly have a talent for science. Don\'t give up!"')
    print('DK tells you that unless you start having more confidence in yourself, you will be easily swayed by others. ' + labpartner + ' ask you: "Do you believe in your own capabilties?')
    response2 = input('Do you choose to answer him? Type: Yes or No\n')
    if response2 == "Yes":
        response3 = input('So do you choose to believe in yourself? Type: Yes or No \n')
        if response3 == "Yes":
            print(labpartner + ' smiles at you! You begin to feel more confident in yourself. You can overcome hardship!')
        elif response3 == "No":
            print(labpartner + ' looks angry! Then he looks away and tells you that not believing in yourself will only lead to failure. " ' + username + ' the only one who can change your mindset is yourself!" \n')
            print('You\'re surprised at how passionatly your lab partner feels about this. This makes you smile, he\'s right, you are an amazing and intelligent person!')
    elif response2 == "No":
        print(labpartner + 'looks a bit disappointed at your lack of response but he still smiles at you and lets you know that in the future he hopes you start having more confidence in your capabilites')
    print()
    print('You finished lab early and it\'s time to leave. After the conversation you had with ' + labpartner + ' you feel better and decide to call your mom and tell her how class went. \n')
    print('"Hello mom! I just wanted to call you and tell you that class went well! \nI was the one leading our lab group and we were even able to finish our lab early." \n')
    print('You continue talking to your mom. "While I can tell this class will definitely be hard, I know it will be doable!" \n')
    print('Your mom takes a pause, and sounding surprised she tells you good job. She is surpised at how confident you sound, \n and can\'t find it in her to get after you for not changing into Holy studies. \n')
    print('The pride in your voice warms her heart, and she decides to wait it out a bit more before nagging you to change studies. \n Who knows maybe ' + username + ' can excel in her science classes, your mom thinks.')
    print('Hearing your mom praise you makes you happy. Despite how hard today was, you can\'t wait to take on the semester at SLAY Uni.\n')
    time.sleep(3)
     #if --> print could you have defended your beliefs a little bit more. 
    return 0

def p_print():
    print("                                                      ")                                                                       
    print("                   ▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒               ")              
    print("                   ▒▒              ░░▒▒                ")              
    print("                   ▒▒                ▒▒                 ")             
    print("                   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                 ")             
    print("                   ░░▒▒░░░░░░░░░░░░▒▒░░                  ")            
    print("                     ▒▒            ▒▒                    ")            
    print("                     ▒▒            ▒▒                    ")            
    print("                     ▒▒            ▒▒                     ")           
    print("                     ▒▒            ▒▒                     ")           
    print("                     ▒▒            ▒▒                      ")          
    print("                     ▒▒            ▒▒                      ")          
    print("                   ▒▒▒▒            ▒▒▒▒                    ")          
    print("                 ▒▒                    ▒▒                   ")         
    print("               ▒▒                        ▒▒                 ")         
    print("             ▒▒        ░░                  ▒▒                ")        
    print("           ▒▒  ████▓▓██▓▓██▓▓▓▓▓▓██    ▓▓▓▓  ▒▒              ")        
    print("         ▒▒  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒            ")        
    print("         ▒▒  ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓  ▒▒            ")        
    print("       ▒▒  ▓▓▓▓▓▓▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓  ▒▒░░         ")       
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░  ░░  ▓▓▒▒▒▒▓▓▓▓▓▓  ▒▒           ")       
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓              ▓▓▓▓▓▓▓▓▓▓  ▒▒░░         ")       
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓  ████  ████  ▓▓▓▓▓▓▓▓▓▓  ▒▒           ")       
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓  ██      ██  ▓▓▓▓▓▓▓▓▓▓  ▒▒░░         ")       
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓  ▓▓▓▓▓▓▓▓██  ▒▒            ")      
    print("       ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒░░           ")     
    print("       ▒▒  ▓▓▓▓▓▓▓▓    ██  ██  ▓▓  ▓▓    ██▓▓▓▓  ▒▒             ")     
    print("         ▒▒  ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓░░▒▒               ")     
    print("         ▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒               ")     
    print("            ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒                 ")     
    print("            ▒▒                                ▒▒                 ")              
    print("              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  ")      
    print("              ▒▒  ░░░░░░░░░░░░░░░░  ░░░░    ▒▒                   ")     
    print("              ▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒      \n\n")
    return 0


def bits(username):
    print("In your last class, you're feeling pretty confident. You had completed the reading from the night before, despite it being a little long. \n")
    print("During lecture, you sit at the front of the class, eager to learn about the current topic: electric boogaloo theory.\n ")
    print('The professor stands in front of everyone and asks "Okay class, does true randomness exist in electric boogaloos?" \n')
    print('You decide that it\'s time to start actively participating in class.\n')
    decision1 = input('Should you raise your hand? Type: Yes or No\n')
    if decision1.lower() == 'yes':
        print('You confidently raise your hand and the professor calls on you\n')
        print('You open your mouth and say, "True randomness does not exist". \n')
    elif decision1.lower() == 'no':
        print('You start raising your hand but stop halfway. You\'re feeling shy suddenly.\n')
        print('The professors sees your hand anyways and decides to call on you. \n')
        print('You open your mouth and say, "True randomness does not exist".\n')
    #answer true randomness correctly
    print('Sephiroth: NO THAT\'S WRONG! True randomness DOES exist. If it didn\'t how would we know about it? \n')
    print('Bowser: Yeah, exactly. You\'re stupid for thinking otherwise. This is why princesses don\'t belong here. \n')
    print('Sephiroth: Yeah, princesses don\'t belong here at SLAY Uni\n')
    print('How do you respond?')
    res = input("Would you like to respond with option A or option B? Choose one randomly. (type A or B)\n")
    if res.upper() == 'A':
        print(username + ': "Did y\'all not do last nights homework? In the Intro chapter, it clearly states that true randomness does not exist because there is no set way to test true randomness."\n')
        print('Sephiroth and Bowser look embarrassed, and sit quietly.')
    elif res.upper() == 'B':
        print(username + ': "Shut up you don\'t know what you\'re talking about." \n')
        print('Sephiroth and Bowser faces get red. They stand up aggressively, but before they can say anything, one of them trips over their bag.')
    print('\nFrowning, the professor turns to Sephiroth and Bowser and asks them to leave. "Your rude behavior will not be toleated in my class.\n This is a safe space for learning. Apologize now or leave my class."\n')
    print('Sephiroth and Bowser leave quietly.\n')
    print('The professor then turns to you and praises you for answering correctly and reading the textbook. "For your amazing participation, I will give you 5 bonus points on the test."\n')
    print('You feel proud of yourself for participating in class and for standing up for yourself. \n')
    return 0

def p_bits():
    print("\t\t\t\t    _____    ")
    print("\t\t\t\t.-,;='';_),-.")
    print("\t\t\t\t \_\(),()/_/ ")
    print("\t\t\t\t   (,___,)   ")
    print("\t\t\t\t  ,-/`~`\-,___   ")
    print("\t\t\t\t / /).:.('--._)  ")
    print("\t\t\t\t{_[ (_,_)    ")
    print("\t\t\t\t    | Y |    ")
    print("\t\t\t\t   /  |  \   ")
    print("\t\t\t\t   \"\"\" \"\"\"   ")
    return 0

def dean_rec(username):
    print("As you're walking around campus, waiting at the chariot stop to take you home, you hear someone call " + "\'" +  username.upper() + "\'" + "!!!")
    print("You stop to see an older woman running up to you, dressed in formal attire with a nametag that says ' Queen of Student Relations '")
    print("The Queen: Thank you for waiting. I have heard much about you " + username + ". Would you please follow me? \n")
    decision1 = input("Will you follow her? Yes or No \n")
    if decision1.lower() == 'yes':
        print("You follow the Queen to her office and oddly enough, the door shuts behind you two. Silence surrounds you both.")
        print(".")
        print(".")
        print(".")
        print("The Queen: Do you believe you belong here " + username + "?")
        decision2 = input("What is your answer? Choose wisely. (Yes or No) \n")
        if decision2.lower() == 'yes':
            print("You look The Queen in her eyes and confidently nod. Even after all the trials and tribulations you faced at Slay, \nyou knew that you truly did belong here.")
            print("The Queen looked at you for a moment and smiled.\n")
            print("The Queen: You passed the test! I am extremely proud of you " + username + ". I was once in your shoes, where others would look down on me ")
            print("           simply because I was a woman. You are more than qualified to be here and I am sure you will reach even greater heights than I.")
            print("")
        else:
            print("You avoid The Queen's eyes. Even after all the trials and tribulations you faced at Slay, \nyou still weren\'t sure if you truly did belong at Slay.")
            print("The Queen looked at you for a moment.\n")
            print("The Queen: You are more than qualified to be here " + username + ", and I am sure you will reach even greater heights than I. I am extremely proud ")
            print("           of you and all that you have endured here at Slay, although I do sincerely apologize for it all. From this day forward, please recall ")
            print("           these words and never give up on your dreams, for I know you are capable to achieve them and more. \n")
            print("You were shocked to hear such uplifting words from none other than the Queen herself. She was right, and you decided it was finally time to take ")
            print("control of your destiny and push forward, no matter the obstacles in your path. With the help of those around you and your own determination, it ")
            print("time to change!")
    else:
        print("The Queen chuckles and tells you to follow her as an order. You nodded anyways and continued. \n")
        print("You follow the Queen to her office and oddly enough, the door shuts behind you two. Silence surrounds you both.")
        print(".")
        print(".")
        print(".")
        print("The Queen: Do you believe you belong here " + username + "?")
        print("You look The Queen in her eyes and confidently nod. Even after all the trials and tribulations you faced at Slay, \nyou knew that you truly did belong here.")
        print("The Queen looked at you for a moment and smiled.\n")
        print("The Queen: You passed the test! I am extremely proud of you " + username + ". I was once in your shoes, where others would look down on me ")
        print("           simply because I was a woman. You are more than qualified to be here and I am sure you will reach even greater heights than I.")
        print("")

        
    return 0
def p_intro():
    print("█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ █░░ █▀▀█ █░░█ ")
    print("█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ 　 ░░█░░ █░░█ 　 ▀▀█ █░░ █▄▄█ █▄▄█ ")
    print("░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ 　 ░░▀░░ ▀▀▀▀ 　 ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█ ")
    print("█░░█ █▀▀▄ ░▀░ ▀█░█▀ █▀▀ █▀▀█ █▀▀ ░▀░ ▀▀█▀▀ █░░█ ")
    print("█░░█ █░░█ ▀█▀ ░█▄█░ █▀▀ █▄▄▀ ▀▀█ ▀█▀ ░░█░░ █▄▄█ ")
    print("░▀▀▀ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▄▄▄█\n\n\n")
    return 0

def main():
    #intro 
    p_intro()
    username = input("Welcome! Please input the name of your character: \n")
    print("\nOnce upon a time, about 400 years ago, there once was a princess (you) named " + username + ".")
    print("You are starting your journey at SLAY University, which will become UT Austin in the far, far future.")
    answer = input("However, you are having trouble deciding what you want to study. Are you, " + username + ", ready to choose your path? (please input Y or N)\n")
    
    #magical arts
    if ((answer == "Y") or (answer == "y")): 
        print("Great! your first class of the day is the truly eventful Magical Arts class (AKA Public Health in 400 years).\n")
        print("\n\t\t\t\t(∩^o^)⊃━☆:･ﾟ✧*:･ﾟ✧✯\t\t \n")
        time.sleep(1)
        MagicalArts(username)
    else:
        print("okay, bye!")
        return username
    
    #Marine Biology
    print("\n\t\t\t\t(∩^o^)⊃━☆:･ﾟ✧*:･ﾟ✧✯\t\t \n")
    time.sleep(1)


    print("Congrats " + username + " for finishing your first college class!\n")
    answer = input("Are you ready for your next class? (please input Y or N)\n")
    if((answer == "Y") or (answer == "y")):
        print("\nGreat! Your next class is the ~quite interesting~ Phenomenon Behind Sharknados (AKA Marine Biology in 400 years).\n")
        print("\t\t\t\t       .")
        print("\t\t\t\t      \":\"")
        print("\t\t\t\t    ___:____     |\"\/\"|")
        print("\t\t\t\t  ,'        `.    \  /")
        print("\t\t\t\t  |  O        \___/  |")
        print("\t\t\t\t~^~^~^~^~^~^~^~^~^~^~^~^~)")
        time.sleep(2)
        sharknado(username)  
        print("\t\t\t\t       .")
        print("\t\t\t\t      \":\"")
        print("\t\t\t\t    ___:____     |\"\/\"|")
        print("\t\t\t\t  ,'        `.    \  /")
        print("\t\t\t\t  |  O        \___/  |")
        print("\t\t\t\t~^~^~^~^~^~^~^~^~^~^~^~^~)")
        time.sleep(2)
    else:
        print("thanks, bye!")
        return username 
    
    #chemistry 
    print("\n Good job in The phenomenon behind Sharknado!\n")
    answer = input("Would you like to keep going? (please input Y or N)\n")
    if((answer == "Y") or (answer == "y")):
        print("oh no!")
        print("your next class is the dreaded Potions 101 (AKA Chemistry in 400 years).\n")
        p_print()
        time.sleep(2)
        Potions101(username)  
    else:
        print("thanks, bye!")
        return username 
    
    #computer science
    p_print()
    time.sleep(2)
    print("\n Wow! You're on a roll!\n")
    input("You only have one class left. Would you like to attend it? (please input Y or N)\n")
    if((answer == "Y") or (answer == "y")):
        print("Great!")
        print("your last class is the magical Bits & Electric Boogaloos (AKA Computer Science in 400 years).\n")
        p_bits()
        bits(username)  
    else:
        print("thanks, bye!")
        return username 
    
    #supportive dean
    p_bits()
    print("\nCongrats on finishing all of your classes! And don't worry, your hard work does not go unnoticed.\n")
    result = dean_rec(username)
    if(dean_rec == 1):
        print("You still have to choose a field of study. After this journey, what would you choose?")
        print("\t\t✧˖°  THE END  ✧˖°\t\t")
        

    print("\t\t\t\t   _____                         ____                     ______  ")
    print("\t\t\t\t  / ____|                       / __ \                   / ___ \ ")
    print("\t\t\t\t | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __   / /  __) |")
    print("\t\t\t\t | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| < <  |__ < ")
    print("\t\t\t\t | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |     \ \ ___) |")
    print("\t\t\t\t  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|      \_____/ ")
    print("\t\t\t\t                                                                  ")  
    return 0  


main()
