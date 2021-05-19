import random
import numpy as np
import grequests
import requests
from bs4 import BeautifulSoup
import time
import webbrowser
from googlesearch import search

start_time = time.time()


movies = []
years = []
ratings = []
genres = []
urls = []
descriptions = []

print("Welcome to my movie suggestion engine! You can select a movie gender and we will suggest you a movie with 7.5 and above rating in imdb from all years till today.")
# PAGE LOOPING

pages = np.arange(1, 2001, 250)
for url in pages:

    url = "https://www.imdb.com/search/title/?title_type=feature&user_rating=7.5,10.0&num_votes=10000,2000000&adult=include&sort=release_date,desc&count=250" + \
            "&start="+str(url)+"&ref_=adv_nxt"
    urls.append(url)

                                                    # REQUESTS AND RESPONSES
rs = (grequests.get(url) for url in urls)
resp = grequests.map(rs)
for r in resp:

    soup = BeautifulSoup(r.text, 'lxml')
    movie_containers = soup.find_all('div', class_='lister-item mode-advanced')  # all movies list containers
      
                                                 # CONTAINER LOOPING AND LISTS CREATION( SCRAPING)
    for i in range(len(movie_containers)):

        movie = movie_containers[i].h3.a.text
        movies.append(movie)
        year = movie_containers[i].h3.find('span', class_='lister-item-year text-muted unbold').text
        years.append(year)
        rate = float(movie_containers[i].strong.text)
        ratings.append(rate)
        genre = movie_containers[i].find('span', class_='genre').text
        genre = genre.lower().strip()
        genres.append(genre)
        description = movie_containers[i].find_all('p', attrs={'class':'text-muted'})[1].text.strip()
        descriptions.append(description)

                                       # FUNCTION TO PICK A MOVIE
def movie_choice():
    while True:
        movieToWatch = random.choice(movies)
        index = movies.index(movieToWatch)
        if genre_choice in genres[index]:
            print("--------This is the movie we suggest you: -----")
            print()
            print(movies[index].upper())
            print(genres[index])
            print(years[index])
            print("RATING: ", ratings[index])
            print("STORY DESCRIPTION: ", descriptions[index])
            quote = "movie trailer video"
            query = (movieToWatch + str(years[index]) + quote)
            trailer_option = input("If you want to search for this movie trailer, enter 'yes' or else enter 'no': ").lower()
            if trailer_option == 'yes':
                for j in search(query, lang='en', num=2, start=0, stop=2, tpe='vid'):
                    print(j)
                    webbrowser.open(j)
                    break
            else:
        
                break
        else:
            continue
    

genre_choice = input("Please enter the gender of the movie you want to watch: ").lower()

while True:                                         
    
    if any(genre_choice in x for x in genres):        # TEST FOR VALID MOVIE GENRE AND (MOVIE_CHOICE) FUNCTION CALL DEPENDING ON USER ANSWER
        movie_choice()
        
        print()
        answer = input("--------If you want to quit movie suggestion, enter Q. To continue suggestion enter S key. To change genre selection enter C -----").upper()
        if answer == "Q":
            break
        elif answer =="C":
            genre_choice = input("Please enter the gender of the movie you want to watch: ").lower()
            movie_choice()
            
        elif answer == "S":
            movie_choice()
            answer = input("--------If you want to quit movie suggestion, enter Q. To continue suggestion enter S key. To change genre selection enter C -----").upper()
            
        
            
    else:
        print("Sorry, this is not a valid genre,try again.")
        genre_choice = input("Please enter the gender of the movie you want to watch: ").lower()
        continue
            

     

print("--- %s seconds ---" % (time.time() - start_time))
        
        
              

#1. bug me ot trailer , argei na to deiksei
            

          





        



            
    


        


            


    
        





