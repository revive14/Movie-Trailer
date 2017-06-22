from media import Movie  # importing Movie class from media.py file
import fresh_tomatoes


# creating Movie class instances

toy_story = Movie("Toy Story",
                  "Kids toys come alive",
                  "http://bit.ly/1LTwLEy",
                  "http://bit.ly/VZggnq")

jolly_llb = Movie("Jolly LLB",
                  """A lawyer tries to make a splash
                  by reopening a high-profile case.""",
                  "http://bit.ly/2ssnXFL",
                  """https://www.youtube.com/
                  watch?v=cIIExNPgXm0""")

the_mummy = Movie("The Mummy",
                  """Nick Morton is a soldier of fortune
                  who plunders ancient sites and sells them""",
                  "http://bit.ly/2sVLJeP",
                  """https://www.youtube.com
                  /watch?v=IjHgzkQM2Sg""")

pirates = Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
                """The treacherous Captain Salazar and
                his crew of ghost pirates are back for revenge.""",
                "http://bit.ly/2rXnxUd",
                """https://www.youtube.com/
                watch?v=a5V5C8mEVzY""")

cars = Movie("Cars",
             """The story of CARS 3 stems from the collision between Lightning McQueen
                and the new generation of race cars.""",
             "http://bit.ly/2rDXSRn",
             """https://www.youtube.com/
             watch?v=onGynY3EaL4""")

before_i_fall = Movie("Before I Fall",
                      """Samantha Kingston has everything.
                      Then, everything changes.""",
                      "http://bit.ly/2tQ8EV3",
                      """https://www.youtube.com/
                      watch?v=q3Zyy4ZXegE""")

# saving the movie instances in a list
movies = [jolly_llb, the_mummy, pirates, cars, before_i_fall, toy_story]

# the following function accept list as argument
fresh_tomatoes.open_movies_page(movies)
