import webbrowser
import Speach_to_txt as ST
def youtube_s():
    new = 2

    tabUrl = "https://www.youtube.com/results?search_query="
    print("Enter query")
    term = ST.listen()
    #term = input("Enter query: ")
    webbrowser.open(tabUrl+term,new=new)