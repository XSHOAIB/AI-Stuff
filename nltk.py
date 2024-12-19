import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
text = "Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

stop_words = set(stopwords.words('english'))

words = text.split()
filtered_words = [word for word in words if word.lower() not in stop_words]

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("Filtered Words (without stopwords):", filtered_words)
print("Lemmatized Words:", lemmatized_words)
print("Stemmed Words:", stemmed_words)
