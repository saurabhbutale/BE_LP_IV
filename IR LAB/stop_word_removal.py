import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import PunktSentenceTokenizer
# Download the necessary NLTK resources
#nltk.download('punkt')
#nltk.download('stopwords')

def remove_stopwords_from_file(file_path):
    """
    Function to remove stop words from a text file.
    
    Parameters:
    file_path : str
        The path to the file from which stop words will be removed.
    
    Returns:
    filtered_text : str
        The text after stop words have been removed.
    """
    # Open and read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
     # Print the original text before stop word removal
    print("Original Text:\n")
    print(text)
    print("\n" + "="*50 + "\n")  # Divider for better readability
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Get the list of English stop words
    stop_words = set(stopwords.words('english'))
    
    # Filter out the stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

# Example usage

# Replace 'your_file.txt' with the path to your actual text file
file_path = 'stop_word.txt'

# Preprocess the text file by removing stop words
processed_text = remove_stopwords_from_file(file_path)

# Display the processed text
print("Text after stop word removal:")
print(processed_text)
