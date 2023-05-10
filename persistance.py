import psutil
from subprocess import Popen
import subprocess


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def run_batch_file(file_path):
    Popen(file_path,creationflags=subprocess.CREATE_NEW_CONSOLE)


def persistance():
    
    if checkIfProcessRunning('runBat.exe'):
         persistance()
            
    else:
        print('Jarvis is not runing-Launching')
        #os.system("C:\Windows\System32\cmd.exe C:\Users\RN\Desktop\Python\Jarvis_Online\Jarvis-master\run_Jarvis.bat")
        run_batch_file('runBat.exe')
        persistance()
persistance()