import nltk
import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from newspaper import Article

nltk.download('punkt')
nltk.download('stopwords')

def calculate_sentence_scores(sentences, frequency_table):
    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in frequency_table:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = frequency_table[word]
                else:
                    sentence_scores[sentence] += frequency_table[word]

    return sentence_scores

def get_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text, article.title, article.publish_date

def get_summary_from_url(url, num_sentences=5):
    text, title, publish_date = get_text_from_url(url)
    sentences = sent_tokenize(text)
    frequency_table = {}
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    for word in words:
        word = word.lower()
        if word not in stopWords:
            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1

    sentence_scores = calculate_sentence_scores(sentences, frequency_table)
    top_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    summary = [sent for sent in sentences if sent in top_sentences]
    
    # Create a more comprehensive output
    summary_with_info = {
        "title": title,
        "publish_date": publish_date,
        "source_url": url,
        "summary_sentences": summary
    }

    return summary_with_info

# Input the URL of the webpage you want to summarize
url = "https://www.ibm.com/topics/machine-learning"  # Replace with the desired URL

# Generate a more extensive summary
summary_info = get_summary_from_url(url, num_sentences=25)

# Print the comprehensive summary
print("Title:", summary_info["title"])
print("Publish Date:", summary_info["publish_date"])
print("Source URL:", summary_info["source_url"])
print("Summary:")
for sentence in summary_info["summary_sentences"]:
    print(sentence)
