
# importing requests package 
import requests      
import pyttsx3
engine = pyttsx3.init();

def NewsFromBBC(): 
      
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=972ec8d879974ff5bf231a05a9d19ba4"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news
        print(i + 1, results[i])
        engine.say(results[i]);
        engine.runAndWait();
                         
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    NewsFromBBC()  
