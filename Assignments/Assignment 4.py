import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab') 
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')  
nltk.download('words')

# Sample text
text = "Apple was founded by Steve Jobs in California. He loved creating innovative products."

# 1. Tokenization
print("Word Tokenization:", word_tokenize(text))
print("Sentence Tokenization:", sent_tokenize(text))

# 2. Stopword Removal
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
print("After Stopword Removal:", filtered_tokens)

# 3. Stemming
ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered_tokens]
print("After Stemming:", stemmed)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w.lower()) for w in filtered_tokens]
print("After Lemmatization:", lemmatized)

# 5. POS Tagging
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)

# 6. Named Entity Recognition (NER)
ner_tree = ne_chunk(pos_tags)
print("Named Entities:", ner_tree)
