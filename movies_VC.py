import webbrowser
import Speach_to_txt as st
def movies():
    new = 2

    tabUrl = "https://123moviesgo.ac/search/"
    
   # tabUrl = "https://www5.123movies.link/all_search/"
    term = st.listen()
    #term = input("Enter query: ")
    webbrowser.open(tabUrl+term,new=new)





#weeds-season-5