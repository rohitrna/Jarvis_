import subprocess
import Speach_to_txt as stt

def take_Notes():
    print("speak")
    nts = stt.listen()
    nts1 = nts
    i = 0
    #subprocess.Popen('c:\\windows\\system32\\rundll32.exe shell32.dll,#61')
    #subprocess.Popen('c:\\windows\\system32\\notepad.exe')
    while(i != len(nts)):
        nts = nts [:4]
        if(nts == "done"): 
            #print(str_num1)
            
            text_file = open("TheNotes.txt", "w")
            n = text_file.write(nts)
            text_file.close()
    
            break
        nts = nts[1:]   
        i = i+1
    
    
    