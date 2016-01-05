import MyMovieTrailers
import media

#create objects of class Movie and instantiate them

#create object toy_story
toy_story = media.Movie("Toy Story-Part 1", "A story of a boy and his toys",
"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=KYz2wyBy3kc","G","http://www.imdb.com/title/tt0114709/?ref_=fn_al_tt_2","1995")

#create object harrypotter
harrypotter = media.Movie("Harry Potter-Part 1", "A marine on an alien planet",
"https://upload.wikimedia.org/wikipedia/en/4/44/HarryPotter5poster.jpg",
"https://www.youtube.com/watch?v=czFqCdNRHqQ","PG","http://www.imdb.com/title/tt0241527/?ref_=nv_sr_1","2001")

#create object school_of_rock
school_of_rock = media.Movie("School of Rock", "An american comedy.Story of a struggling rock singer and guitarist",
"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
"https://www.youtube.com/watch?v=XCwy6lW5Ixc","PG-13","http://www.imdb.com/title/tt0332379/?ref_=fn_al_tt_1","2003")

#create object ratatouille
ratatouille = media.Movie("Ratatouille", "A computer animated comedy. Story of a rat",
"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
"https://www.youtube.com/watch?v=c3sBBRxDAqk","G","http://www.imdb.com/title/tt0382932/?ref_=fn_al_tt_1","2007")

#create object kung_fu_panda
kung_fu_panda = media.Movie("Kung Fu Panda-Part1", "An adventurous story of a panda who becomes the Kung-Fu master",
"https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
"https://www.youtube.com/watch?v=PXi3Mv6KMzY","PG","http://www.imdb.com/title/tt0441773/?ref_=fn_al_tt_1","2008")

#create object avatar
avatar = media.Movie("Avatar", "A marine on an alien planet",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=uZNHIU3uHT4","PG-13","http://www.imdb.com/title/tt0499549/?ref_=nv_sr_1","2009")

#create object midnight_in_paris
midnight_in_paris = media.Movie("Midnight in Paris", "A romantic comdey. Story of how Paris changes the life of 2 young engaged people.",
"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
"https://www.youtube.com/watch?v=FAfR8omt-CY","PG-13","http://www.imdb.com/title/tt1605783/?ref_=fn_al_tt_1","2011")

#create object hunger_games
hunger_games = media.Movie("The Hunger Games", "An adventurous story",
"https://upload.wikimedia.org/wikipedia/en/c/c8/The_Hunger_Games_%28foil%29.png",
"https://www.youtube.com/watch?v=mfmrPu43DF8","PG-13","http://www.imdb.com/title/tt1392170/?ref_=fn_al_tt_1","2012")

#create object interstellar
interstellar = media.Movie("Interstellar", "An epic science fiction",
"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
"https://www.youtube.com/watch?v=2LqzF5WauAw","PG-13","http://www.imdb.com/title/tt0816692/?ref_=fn_al_tt_1","2014")

#creating a list of the Movie objects
movies = [toy_story,harrypotter,school_of_rock,ratatouille,kung_fu_panda,avatar,midnight_in_paris,hunger_games,interstellar]

#pass the movie list to the open_movies_page function in the MyMovieTrailers module
MyMovieTrailers.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__module__)
# print(media.Movie.__name__)
##module/filename.classna,e
