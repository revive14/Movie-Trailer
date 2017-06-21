from media import Movie
import webbrowser, time
import fresh_tomatoes

toy_story = Movie("Toy Story",
"Kids toys come alive",
"http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")



jolly_llb = Movie("Jolly LLB",
"A lawyer from a small town in India moves to Delhi and tries to make a splash by reopening a high-profile case.",
"https://upload.wikimedia.org/wikipedia/en/f/f1/Jolly_LLB.jpg",
"https://www.youtube.com/watch?v=cIIExNPgXm0")

the_mummy = Movie("The Mummy",
"Nick Morton is a soldier of fortune who plunders ancient sites for timeless artifacts and sells them to the highest bidder.",
"http://horrornews.net/wp-content/uploads/2017/06/tm1.jpg",
"https://www.youtube.com/watch?v=oy7vAhNAKPM")

pirates = Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
"The treacherous Captain Salazar and his crew of ghost pirates are back for revenge. Jack's only hope of survival lies in seeking out the legendary Trident of Poseidon, a mythical artefact that grants whoever holds it control over the oceans.",
"http://thedigitaltheater.com/wp-content/uploads/2016/10/potc.jpg",
"https://www.youtube.com/watch?v=a5V5C8mEVzY")

cars = Movie("Cars",
"he story of CARS 3 stems from the collision between Lightning McQueen and the new generation of race cars.",
"https://vignette1.wikia.nocookie.net/pixar/images/2/26/CARS_3_Natalie-Certain.jpg/revision/latest?cb=20170309173039",
"https://www.youtube.com/watch?v=onGynY3EaL4")

before_i_fall = Movie("Before I Fall",
"Samantha Kingston has everything. Then, everything changes. After one fateful night, she wakes up with no future at all. Trapped into reliving the same day over and over, she begins to question just how perfect her life really was.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BNDYwOTY0MDI2OV5BMl5BanBnXkFtZTgwOTE5NzM2MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=q3Zyy4ZXegE")

movies = [jolly_llb,the_mummy,pirates,cars,before_i_fall,toy_story]

fresh_tomatoes.open_movies_page(movies)
