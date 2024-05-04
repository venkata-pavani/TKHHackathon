#!/usr/bin/env python
# coding: utf-8

# import requests
# from bs4 import BeautifulSoup
# import spacy
# import nltk
# from nltk.tokenize import word_tokenize, sent_tokenize
# from collections import Counter
# 
# nltk.download('punkt')
# 
# # Extract text from a web page
# def extract_text(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Extract text from paragraphs and join them
#     text = ' '.join([p.get_text() for p in soup.find_all('p')])
#     return text
# 
# # Analyze text and Entities
# def analyze_text(text):
#     # Load spaCy's English tokenizer
#     nlp = spacy.load('en_core_web_sm')
#     # Process the text with spaCy
#     doc = nlp(text)
#     # Extract named entities with their labels
#     entities = [(ent.text, ent.label_) for ent in doc.ents]
#     return entities
# 
# # Extracting main keywords and Compose Summary Sentence
# def summarize_text(text, keywords, num_sentences=5):
#     # Tokenize text into sentences
#     sentences = sent_tokenize(text)
#     summary_sentences = []
#     # Check each sentence for the presence of keywords
#     for sentence in sentences:
#         # If a keyword is found in the sentence, add it to the summary
#         if any(keyword in sentence.lower() for keyword in keywords):
#             summary_sentences.append(sentence)
#             # If we have enough summary sentences, stop
#             if len(summary_sentences) >= num_sentences:
#                 break
#     return ' '.join(summary_sentences)
# 
# # Function to summarize named entities by their labels and include counts
# def summarize_entities(entities):
#     entity_dict = {}
#     for entity, label in entities:
#         entity_dict[(label, entity)] = entity_dict.get((label, entity), 0) + 1
#     return entity_dict
# 
# # Function to summarize a web page, extracting main keywords and providing an overall summary
# def summarize_web_page(url, num_keywords=10, num_sentences=5):
#     # Extract text from the web page
#     text = extract_text(url)
#     # Analyze the text and find named entities
#     entities = analyze_text(text)
#     # Summarize named entities by their labels and include counts
#     entity_summary = summarize_entities(entities)
#     # Remove duplicates and count occurrences
#     unique_entities = {f"{label.capitalize()}: {entity} (Count: {count})" for (label, entity), count in entity_summary.items()}
#     # Extract main keywords
#     keywords = [entity for label, entity in entity_summary.keys()][:num_keywords]
#     # Summarize text using most frequent words and important sentences
#     summary = summarize_text(text, keywords, num_sentences)
#     
#     # Print the summary
#     print("======================================================================")
#     print("                       MAIN KEYWORDS SUMMARY")
#     print("======================================================================")
#     for entity in unique_entities:
#         print(entity)
#     
#     print("\n======================================================================")
#     print("                        OVERALL PAPER SUMMARY")
#     print("======================================================================")
#     print(summary)
# 
# # URL of the web page to explore
# url = 'https://research.google/blog/overcoming-leakage-on-error-corrected-quantum-processors/'
# 
# # Summarize the web page
# summarize_web_page(url)
# 

# In[84]:


import sys
import requests
from bs4 import BeautifulSoup
import spacy
from nltk.tokenize import sent_tokenize
from collections import Counter

# Function to extract text from a web page
def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract text from paragraphs and join them
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text


def analyze_text(text):
    # Load spaCy's English tokenizer
    nlp = spacy.load('en_core_web_sm')
    # Process the text with spaCy
    doc = nlp(text)
    # Extract named entities with their labels
    entities = [ent.text for ent in doc.ents]
    return entities

def summarize_text(text, keywords, num_sentences=10):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    summary_sentences = []
    # Check each sentence for the presence of keywords
    for sentence in sentences:
        # If a keyword is found in the sentence, add it to the summary
        if any(keyword in sentence.lower() for keyword in keywords):
            summary_sentences.append(sentence)
            # If we have enough summary sentences, stop
            if len(summary_sentences) >= num_sentences:
                break
    return ' '.join(summary_sentences)

def summarize_entities(entities):
    entity_counts = Counter(entities)
    return entity_counts

def summarize_web_page(url, num_keywords=5, num_sentences=10):

    text = extract_text(url)

    entities = analyze_text(text)

    entity_summary = summarize_entities(entities)
    # Extract main keywords
    keywords = [entity for entity, _ in entity_summary.most_common(num_keywords)]
    # Summarize text using most frequent words and important sentences
    summary = summarize_text(text, keywords, num_sentences)
    
    # Print the summary
    print("======================================================================")
    print("                       MAIN KEYWORDS SUMMARY")
    print("======================================================================")
    for entity, count in entity_summary.most_common(num_keywords):
        print(f"{entity.capitalize()} (Count: {count})")
    
    print("\n======================================================================")
    print("                        OVERALL PAPER SUMMARY")
    print("======================================================================")
    print(summary)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize_web_page.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    # Summarize the web page
    summarize_web_page(url)


# In[ ]:




