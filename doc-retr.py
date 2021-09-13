# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm
# import time

# from nltk.corpus import stopwords 
# from nltk.stem.wordnet import WordNetLemmatizer
# import string
import re
import csv
# import numpy as np
# from collections import Counter
from bs4 import BeautifulSoup
from os import listdir
# import nltk.data

def handle_prefixed_punctuations(word):
    # dont remove punctuations in a negative and positive, decimal or float number
    if (re.match(r'^[\-]?[0-9]*\.?[0-9]+$', word)):
        return word
    elif (word[:1] == "-") or (word[:1] == ",") or (word[:1] == "."):
        return word[1:]
    else:
        return word

# myPath =  "./cacm-html/"
# for file in listdir(myPath):
#     output = open(myPath+file)
#     soup = BeautifulSoup(output, "html.parser")
#     all_text = ''.join(soup.findAll(text=True))
#     all_text = all_text.lower()
#     line = all_text
#     fName =  file.split(".html")[0]
#     temp_array = []
#     # we need to remove trailing and pre-fixed "," , "." and "-" from the words
#     for each_word in line.split():
#         length = len(each_word)
#         # removing trailing punctuations
#         if (each_word[(length - 1): length] == "-") or (each_word[(length - 1): length] == ",") or (
#             each_word[(length - 1): length] == "."):
#             each_word = each_word[:(length - 1)]  # removing the punctuation
#         # removing pre-fixed punctuations
#         each_word = handle_prefixed_punctuations(each_word)
#         thelist = ["_", ":", "/", "!", "?", "#", "^", "*", "~", "&", "(", ")", "[", "]", "{", "}", "'", ";", '"', "$",
#                    "%", "|", ]
#         for punctuation in thelist:
#             each_word = each_word.replace(punctuation, '')
#         temp_array.append(each_word)
#     content_as_array = temp_array
#     line = ' '.join(content_as_array)
#     outputf = open("Corpus/"+fName+".txt","w+")
#     outputf.write(line)
#     outputf.close()


#creating a dataframe for the above
# txt_csv = open("./data.csv", "w+")
# csv_writer = csv.writer(txt_csv)
header = ["Doc Name", "Doc Contents"]
corpus_path = "./Corpus/"

with open("./data.csv", "w+") as txt_csv:
    csv_writer = csv.writer(txt_csv)

    csv_writer.writerow(header)

    for file in listdir(corpus_path):
        cur_doc = open(corpus_path+file)
        csv_writer.writerow([file, cur_doc.readline()])




