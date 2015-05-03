# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

# Movie class called to create multiple instances of different favorite movie

# This is the section for the movie series Star Wars
star_wars = media.Movie("1977",
                        "Star Wars",
                        "Luke Skywalker, Han Solo, Chewbacca and two droids attempts save the universe from the Empire's world-destroying battle-station and rescue Princess Leia from Darth Vader.",
                        "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=vP_1T4ilm8M",
                        "Mark Hamill, Harrison Ford, Carrie Fisher")
                                           
the_empire_strikes_back = media.Movie("1980",
                                      "The Empire Strikes Back",
                                      "Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
                                      "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                      "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                                      "Mark Hamill, Harrison Ford, Carrie Fisher")
                                  
return_of_the_jedi = media.Movie("1983",
                                "Return of the Jedi",
                                "After rescuing Han Solo from the palace of Jabba the Hutt, the rebels attempt to destroy the second Death Star. Luke struggles to make Vader return from the dark side of the Force.",
                                "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                                "https://www.youtube.com/watch?v=CsDwpF3uiZI",
                                "Mark Hamill, Harrison Ford, Carrie Fisher")

the_phantom_menace = media.Movie("1999",
                                "Star Wars Episode I:The Phantom Menace",
                                "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force.",
                                "http://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                                "https://www.youtube.com/watch?v=qV1T2DJBwIs",
                                "Ewan McGregor, Liam Neeson, Natalie Portman")

attack_of_the_clones = media.Movie("2002",
                                "Star Wars Episode II:Attack of the Clones",
                                "Anakin Skywalker shares a forbidden romance with Padmé, while Obi-Wan investigates an assassination attempt on the Senator.",
                                "http://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",
                                "https://www.youtube.com/watch?v=gYbW1F_c9eM",
                                "Hayden Christensen, Natalie Portman, Ewan McGregor")

revenge_of_the_sith = media.Movie("2005",
                                "Star Wars Episode III:Revenge of the Sith",
                                "Sith Lord Darth Sidious steps out of the shadows and Anakin succumbs to his emotions, becoming Darth Vader the Dark One.",
                                "http://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                                "https://www.youtube.com/watch?v=5UnjrG_N8hU",
                                "Hayden Christensen, Natalie Portman, Ewan McGregor")

# This is the section for the movie series Terminator
the_terminator = media.Movie("1984",
                            "The Terminator",
                            "A human-looking cyborg is sent from 2029 to 1984 to assassinate a waitress, whose unborn son will lead humanity in a war against the machines",
                            "http://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                            "https://www.youtube.com/watch?v=lHz95RYUbik",
                            "Arnold Schwarzenegger, Linda Hamilton")

judgment_day = media.Movie("1991",
                            "Terminator 2: Judgement Day",
                            "A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her young son, John Connor, from a more advanced cyborg, made out of liquid metal.",
                            "http://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
                            "https://www.youtube.com/watch?v=eajuMYNYtuY",
                            "Arnold Schwarzenegger, Linda Hamilton")

# This is the section for the movie series Indiana Jones
indy_lost_ark = media.Movie("1981",
                            "Raiders of The Lost Ark",
                            "In the first installment of the Indiana Jones film franchise, archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
                            "http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",
                            "https://www.youtube.com/watch?v=gz4crpFaW4M",
                            "Harrison Ford, Karen Allen, Paul Freeman")
                                           
indy_temple_of_doom = media.Movie("1984",
                                  "Indiana Jones and the Temple of Doom",
                                  "Indiana Jones stumbles upon a secret cult plotting a terrible plan in the catacombs of an ancient palace.",
                                  "http://upload.wikimedia.org/wikipedia/en/1/10/Indiana_Jones_and_the_Temple_of_Doom_PosterB.jpg",
                                  "https://www.youtube.com/watch?v=QqGdBaSxINM",
                                  "Harrison Ford, Kate Capshaw")
                                  
indy_last_crusade = media.Movie("1989",
                                "Indiana Jones and The Last Crusade",
                                "Indiana Jones search for his father, Dr. Henry Jones Sr., who went missing while pursuing the Holy Grail.",
                                "http://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg",
                                "https://www.youtube.com/watch?v=a6JB2suJYHM",
                                "Harrison Ford, Sean Connery, Alison Doody")

indy_crystal_skull = media.Movie("2008",
                                "Indiana Jones and the Kingdom of the Crystal Skull",
                                "Indiana Jones becomes entangled in a Soviet plot to uncover the secret behind mysterious artifacts known as the Crystal Skulls",
                                "http://upload.wikimedia.org/wikipedia/en/d/d5/Kingdomofthecrystalskull.jpg",
                                "https://www.youtube.com/watch?v=nMhfESAa4tw",
                                "Harrison Ford, Cate Blanchett, Shia LaBeouf")
                                                    


# All the movie instances are grouped together in a list
movie_list = [star_wars, the_empire_strikes_back, return_of_the_jedi,the_phantom_menace, attack_of_the_clones, revenge_of_the_sith,
              the_terminator,judgment_day, indy_lost_ark, indy_temple_of_doom, indy_last_crusade, indy_crystal_skull]

# The Python module called fresh_tomatoes.py is called to generate a website that display the movie list
fresh_tomatoes.open_movies_page(movie_list)
