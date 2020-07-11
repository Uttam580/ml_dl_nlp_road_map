# Natural_language_processing 

# What is NLP ?
Natural language processing (NLP) is about developing applications and services that are able to understand human languages. Some Practical examples of NLP are speech recognition for eg: google voice search, understanding what the content is about or sentiment analysis etc.

# NLP Implementations
These are some of the successful implementations of Natural Language Processing (NLP):

* Search engines like Google, Yahoo, etc. Google search engine understands that you are a tech guy so it shows you results related to you.

* Social websites feed like the Facebook news feed. The news feed algorithm understands your interests using natural language processing     and shows you related Ads and posts more likely than other posts.

* Speech engines like Apple Siri.

* Spam filters like Google spam filters. It’s not just about the usual spam filtering, now spam filters understand what’s inside the email content and see if it’s a spam or not.

# Tokenization 

Tokenization is the process of tokenizing or splitting a string, text into a list of tokens. One can think of token as parts like a word is a token in a sentence, and a sentence is a token in a paragraph.

# Stemming 

Stemming is the process of reducing inflection in words to their root forms such as mapping a group of words to the same stem even if the stem itself is not a valid word in the Language.

https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html

# Lemmatization

Lemmatization usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma

# Stemming vs Lemmatization

Stemming for studies is studi

Stemming for studying is studi

Lemma for studies is study

Lemma for studying is study

# What is Bag-of-Words?
We need a way to represent text data for machine learning algorithm and the bag-of-words model helps us to achieve that task. The bag-of-words model is simple to understand and implement. It is a way of extracting features from the text for use in machine learning algorithms.


In this approach, we use the tokenized words for each observation and find out the frequency of each token.
Let’s take an example to understand this concept in depth.

“It was the best of times”

“It was the worst of times”

“It was the age of wisdom”

“It was the age of foolishness”

We treat each sentence as a separate document and we make a list of all words from all the four documents excluding the punctuation.
We get,

[‘It’, ‘was’, ‘the’, ‘best’, ‘of’, ‘times’, ‘worst’, ‘age’, ‘wisdom’, ‘foolishness’]

The next step is the create vectors. Vectors convert text that can be used by the machine learning algorithm.
We take the first document — “It was the best of times” and we check the frequency of words from the 10 unique words.
“it” = 1
“was” = 1
“the” = 1
“best” = 1
“of” = 1
“times” = 1
“worst” = 0
“age” = 0
“wisdom” = 0
“foolishness” = 0

Rest of the documents will be:

“It was the best of times” = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]

“It was the worst of times” = [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]

“It was the age of wisdom” = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]

“It was the age of foolishness” = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]


The process of converting NLP text into numbers is called vectorization in ML. Different ways to convert text into vectors are:
Counting the number of times each word appears in a document.
Calculating the frequency that each word appears in a document out of all the words in the document.

# TF-IDF Vectorizer

TF-IDF stands for term frequency-inverse document frequency. TF-IDF weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

# Term Frequency (TF) 

is a scoring of the frequency of the word in the current document. Since every document is different in length,   it is possible that a term would appear much more times in long documents than shorter ones. The term frequency is often divided by the document length to normalize.

# TF= (number of time term t appear in the document/Total number of terms in the documents)

# Inverse Document Frequency (IDF): 
is a scoring of how rare the word is across documents. IDF is a measure of how rare a term is. Rarer the term, more is the IDF score.

# IDF= log(total number of documnets/number of doument withterm t in it )

# TF-IDF Score = TF*IDF





