import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import PorterStemmer
import nltk

# Download necessary resources for NLTK
nltk.download('punkt')

# Initialize the stemmer
stemmer = PorterStemmer()

def process_text(text):
    # Tokenization
    tokens = simple_preprocess(text)  # Gensim's simple_preprocess handles basic tokenization
    
    # Remove stop words using Gensim
    tokens_no_stopwords = gensim.parsing.preprocessing.remove_stopwords(' '.join(tokens)).split()
    
    # Stemming using NLTK
    stemmed_tokens = [stemmer.stem(token) for token in tokens_no_stopwords]
    
    # Lemmatization using Gensim's simple_preprocess (which provides a basic lemmatization)
    lemmatized_tokens = [token for token in tokens_no_stopwords]
    
    return tokens, stemmed_tokens, lemmatized_tokens

# Example usage
if name == "main":
    # Accept input text from the user
    user_text = input("Enter a sentence or paragraph: ")
    
    # Process the user input
    tokens, stemmed_tokens, lemmatized_tokens = process_text(user_text)
    
    # Print results
    print("\nOriginal Tokens:")
    print(tokens)
    
    print("\nStemmed Tokens:")
    print(stemmed_tokens)
    
    print("\nLemmatized Tokens:")
    print(lemmatized_tokens)
