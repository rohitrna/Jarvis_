from urllib.request import urlopen
import pyttsx3
engine = pyttsx3.init();

link = "https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html"

f = urlopen(link)
myfile = f.read()
myfile1 = myfile.decode()
text_file = open("Output.txt", "w")
text_file.write(myfile1)
text_file.close()

#print(myfile)
#engine.say(myfile);
#.runAndWait();