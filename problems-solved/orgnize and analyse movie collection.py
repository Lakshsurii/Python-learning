movie_titles=set()
movie_details={}
def add_movie():
    movie_title=input("Enter Movie title: ")
    year_of_release=input("Enter release year: ")
    duration=input("Enter duration of movie: ")
    genre=input("Enter genre of movie: ")
    return movie_title, year_of_release, duration, genre
    
def add_movie_title(movie_title):
    if movie_title in movie_titles:
        print("Movie already exist")
    else:
        movie_titles.add(movie_title)
        print(f"Movie '{movie_title}' added to the collection.")

def display_unique_titles():
    print(movie_titles)

def store_movie_details(movie_title, year_of_release, duration, genre):
     movie_details[movie_title]= [year_of_release,duration,genre]
     print(f"Details of '{movie_title}' have been stored.")

def get_movie_details():
     movie_title=input("Enter Movie title: ")
     if movie_title in movie_titles:
         print(movie_details[movie_title])
     else:
         print("movie not found")
def update_genre():
    movie_title=input("Enter movie title: ")

    if movie_title in movie_details:
        updated_genre=input("Enter the new genre: ")
        movie_details[movie_title][2]=updated_genre
    else:
        print("movie not found")

def analyze_collection():
    print("Number of movies: ",len(movie_titles))

    genres={movie_details[movie][2] for movie in movie_details}
    print(genres)
        
        
def main():
    
    # Movie 1
    movie_title, year_of_release, duration, genre = add_movie()
    add_movie_title(movie_title)
    store_movie_details(movie_title, year_of_release, duration, genre)

    # Movie 2
    movie_title, year_of_release, duration, genre = add_movie()
    add_movie_title(movie_title)
    store_movie_details(movie_title, year_of_release, duration, genre)

    # Movie 3
    movie_title, year_of_release, duration, genre = add_movie()
    add_movie_title(movie_title)
    store_movie_details(movie_title, year_of_release, duration, genre)

    display_unique_titles()
    get_movie_details()
    update_genre()
    analyze_collection()

main()    

    
