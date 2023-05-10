import webbrowser
def google_s():
    new = 2

    tabUrl = "http://google.com/?#q="
    term = input("Enter query: ")
    webbrowser.open(tabUrl+term,new=new)