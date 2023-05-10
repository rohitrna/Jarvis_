import Speach_to_txt as stt
import pyttsx3
engine = pyttsx3.init();

def stand_by():
    
    str_num = stt.listen()
    #str_num = input()
    #str_num = "1234567890pam4445"
    i = 0

    while(i != len(str_num)):
        str_num1 = str_num [:4]
        if(str_num1 == "ruby"): 
            print(str_num1)
            engine.say(" Disengaging Standby mode")
            engine.runAndWait()
            break
        str_num = str_num[1:]   
        i = i+1
    print(str_num)