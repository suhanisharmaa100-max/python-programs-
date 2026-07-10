#create a class called movie
#attributes:title,duration,genre,rating
#view(default should be 0)
#methods:
#play()-increase view by 1 and print"<title> is  now playing"
#rate(now_rating)-update  the movies rating.
#details()-print all the details of the movie
#_str_()return a neat one line description of the movie

#create atleast three movies objects play them multiple times,update a rating,and print each object
class Movie:
    def __init__(self, title, duration, genre, rating):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.rating = rating
        self.views = 0  # Default view count

    def play(self):
        self.views += 1
        print(f"{self.title} is now playing")

    def rate(self, new_rating):
        self.rating = new_rating
        print(f"{self.title} rating updated to {self.rating}")

    def details(self):
        print("\n--- Movie Details ---")
        print(f"Title: {self.title}")
        print(f"Duration: {self.duration} minutes")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}/10")
        print(f"Views: {self.views}")

    def __str__(self):
        return (
            f"{self.title} | {self.genre} | "
            f"{self.duration} min | Rating: {self.rating}/10 | Views: {self.views}"
        )


# Creating three movie objects
movie1 = Movie("Inception", 148, "Sci-Fi", 8.8)
movie2 = Movie("3 Idiots", 171, "Comedy/Drama", 8.4)
movie3 = Movie("Avengers: Endgame", 181, "Action", 8.4)

# Playing movies multiple times
movie1.play()
movie1.play()

movie2.play()
movie2.play()
movie2.play()

movie3.play()

# Updating a movie rating
movie2.rate(9.0)

# Printing each movie object using __str__()
print("\n--- Movie Summary ---")
print(movie1)
print(movie2)
print(movie3)

# Printing full details
movie1.details()
movie2.details()
movie3.details()