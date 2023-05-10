import webbrowser
def youtube_s():
    new = 2

    tabUrl = "https://www.youtube.com/results?search_query="
    term = input("Enter query: ")
    webbrowser.open(tabUrl+term,new=new)