''' Task 38 Compulsory task 1
Obj:    work through the example.py
        host my solution on Github
        Add the link for your remote Git repo to a text file named semantic_similarity.txt
'''

# start

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
''' Output:
0.5929930274321619  cat to monkey gives a 59% similarity
0.40415016164997786 banana to monkey gives a 40% similarity
0.22358827466989753 banana to cat gives a 22% similarity
'''
word1 = nlp("camel")
word2 = nlp("horse")
word3 = nlp("sugar")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
''' Output:
0.9999999369458503  camel to horse 99.99% similarity is interesting - didnt think it would be that high
0.14684520650974806 sugar and horse 14.7% similarity is quite low - horses are known to love sugar
0.14684520650974806 sugar to camel 14.7% similarity, same as horse and sugar. Interesting, its applying the logic that
camels and horses are literally the same.  Other substitutions for word 3 produced the same result, so camel and horse
are seen as basically been the same.
'''


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''Output:
0.5929930274321619
0.40415016164997786
0.22358827466989753
cat cat 1.0
cat apple 0.20368057489395142
cat monkey 0.5929930210113525
cat banana 0.2235882729291916
apple cat 0.20368057489395142
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646700501441956
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882729291916
banana apple 0.6646700501441956
banana monkey 0.4041501581668854
banana banana 1.0
'''
tokens = nlp('dog bone monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
''' Output:
dog dog 1.0
dog bone 0.25421422719955444
dog monkey 0.4771559536457062   # lower similarity than cat and monkey (0.59)
dog banana 0.2090904712677002
bone dog 0.25421422719955444
bone bone 1.0
bone monkey 0.23434989154338837
bone banana 0.23619279265403748 # lower similarity than apple and banana (0.66)
monkey dog 0.4771559536457062
monkey bone 0.23434989154338837
monkey monkey 1.0
monkey banana 0.4041501581668854
banana dog 0.2090904712677002
banana bone 0.23619279265403748
banana monkey 0.4041501581668854
banana banana 1.0'''

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car",
            "I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

''' Output:
where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787540461994952
I'd like my boat back -  0.562494104588661
I will name my dog Diana -  0.6491444739190607'''

print("\nMy variation\n")
sentence_to_compare = "This is my code task on my computer."
sentences = ["where is my code?", "I use my computer for a lot of things.", "I can\'t find my code.",
            "My code works.","My computer is broken."]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''Output:      # similarities are quite high, which reading the sentences and ignoring the stop words, makes sense.

where is my code? -  0.8570679388958663
I use my computer for a lot of things. -  0.7698567159900225
I can't find my code. -  0.6488018118528417
My code works. -  0.7118983442808636
My computer is broken. -  0.7675658121751125'''

# example.py provided in the task

import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.
# Remember to install this model by typing python -m spacy download en_core_web_md into your command line

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Now we are going to look into longer texts and compare them.
# Below we  have two lists: one containing complaints submitted to a company, and another of recipes found online.
# We want to establish how spaCy's model can identify similarities or dissimilarities between complaint and recipes.

# Make sure to run this example file and read through the explanations.

# Below is a list of six complaints.
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]

# We will now compare the similarity of the complaints to ascertain if spaCy's similarity
# model is able to distinguish between these long pieces of text.

print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))
print("test")
'''Output:
1.0
0.9058970680531702
0.8761883563680793
0.8921914246767313
0.9362319998716938
0.9077991339554589
0.9058970680531702
1.0
0.8960303314307113
0.8683352787585712
0.9251986105731227
0.909277512798149
0.8761883563680793
0.8960303314307113
'''
# Below is a list of six recipe instructions.

recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]

# We will now compare the similarity of the recipes. to ascertain how well spaCy's similarity
# model is able to distinguish between them.

print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))


''' Output:     Similarity scores are high 87% +
-------------Recipes similarity---------------
1.0
0.9058970680531702
0.8761883563680793
0.8921914246767313
0.9362319998716938
0.9077991339554589
0.9058970680531702'''

# Now we want to obtain the extent of similarity between the complaints and the recipes.
# we will loop through every recipe instruction and compare it with a complaint.

print("-------------Recipes and complaints similarity---------------")

for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

''' Output:     similarity scores are much lower ranging from 53 - 79%
-------------Recipes and complaints similarity---------------
0.7908975726272921
0.6548518295341987
0.739868093247277
0.7337805432695084
0.6703983067394562
0.7674085842432804
0.7580808759364783
0.5323926147261138
0.711456026675044
0.7008472635918351
0.5443125901605878
'''
# What do you observe? Note that the similarity index has reduced from what we observed in the short-text
# example discussed in the content PDF.
# end
