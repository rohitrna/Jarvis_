import webbrowser
import Speach_to_txt as st
def google_s():
    new = 2

    tabUrl = "http://google.com/?#q="
    print("Enter query:")
    term = st.listen()
    #term = input("Enter query: ")
    webbrowser.open(tabUrl+term,new=new)