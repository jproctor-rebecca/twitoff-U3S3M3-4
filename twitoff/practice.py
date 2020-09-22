import spacy
nlp = spacy.load("en_core_web_md")
tweet = nlp("this is some text I am processing")
tweet2 = nlp("This is also a lot omre text that I am processing and hopefully I get something similar to what we were talking about")

print(tweet.vector.shape)
print(tweet2.vector.shape)