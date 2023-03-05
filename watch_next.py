''' Task 38 Compulsory task 2
Obj:    read in the movies from the movies.txt file
    compare them for similarity against the planet_hulk description
    Using similarity scores, recommend similar movie from the list
'''

# start

import spacy

nlp = spacy.load('en_core_web_md')

# Comparison film description
planet_hulk_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the
    Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into
    slavery and trained as a gladiator.'''

# ----- read all the indiv movie descriptions into a list ready for comparison -----

movie_info = []  # will contain movie info for each movie

movies_file = open("movies.txt", "r", encoding='utf-8')  # open movies file and adds them to a list
movies_data = movies_file.readlines()
for movie in movies_data:
    movie_info.append(movie)

# ----- compare the indiv. movies with the planet_hulk description to get similarity score -----

model_sentence = nlp(planet_hulk_compare)
movie_match = []  # temp list of those movies that score similarity score of 80% or more

for sentence in movie_info:
    similarity = nlp(sentence).similarity(model_sentence)
    # print(sentence + " - ", similarity)   # will print the individual similarity scores - not necess for user
    if similarity >= 0.80:  # using a 80% similarity as a base comparison - you cld decide on a higher/lower score
        movie_match.append(sentence)

# ----- Output to the user on recommendations -----

print("\n===== Welcome to movie watch! =====")
print("\nThe following movies are a match based on your like of Planet_Hulk:")
for sentence in movie_match:
    print(f"\n{sentence}")
print("\nEnjoy!")
# end
