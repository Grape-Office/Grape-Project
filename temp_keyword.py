import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
nltk.download('stopwords')

title = "title"
text_content = "text contents"

stop_words = set(stopwords.words('english'))
words = word_tokenize(title + ' ' + text_content)
filtered_words = [word for word in words if word not in stop_words]

freq_dist = nltk.FreqDist(filtered_words)
keywords = [word for word, freq in freq_dist.items() if freq > 1]

print(keywords)

