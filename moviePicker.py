import webbrowser
import random

listOfMovies = ["Crazy Lazy Hazy","Baby Driver","3idiots","Zorba the Greek", "Lock stock and the two smoking barrels","Hatefull 8","Step brothers","Got 5 on it 2","War dogs","Jaws","The Meg","Good,the bad,and the ugly"]
numOfSize = len(listOfMovies)
numOfSize = numOfSize - 1
indxNum = random.randint(0,numOfSize)

a = listOfMovies[indxNum]
print(a)


def movies(a):
    new = 2
    tabUrl = "https://www7.123moviesgo.tv/search/"
    #term = st.listen()
    term = a
    term = term.replace(' ', '-').lower()
    webbrowser.open(tabUrl+term,new=new)

movies(a)