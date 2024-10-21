# summarizer.py

from PyPDF2 import PdfReader
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    
    # Iterate through all the pages and extract text
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    
    return text

# Load the pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

# Function to summarize text with a word limit (approx. 200 words)
def summarize(text, max_words=200):
    # Tokenize the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate summary with beam search
    summary_ids = model.generate(
        inputs,
        max_length=max_words,      # Control the maximum length of the summary (200 words approx.)
        min_length=50,             # Minimum length of the summary
        length_penalty=2.0,        # Controls summary length preference
        num_beams=4,               # Beam search for generating higher quality summaries
        early_stopping=True        # Stops generation when optimal
    )
    
    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to extract and summarize PDF content
def summarize_pdf(pdf_file, word_limit=200):
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_file)
    
    # Summarize the extracted text
    summary = summarize(text, max_words=word_limit)
    
    return summary
