import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import re

# =====================================
# DATA PREPROCESSING FUNCTIONS
# =====================================

# Initialize NLTK components (run once)
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Comprehensive text cleaning with HTML parsing, stopword removal, and lemmatization
    
    Args:
        text (str): Raw text to clean
        
    Returns:
        str: Cleaned text
    """
    if pd.isna(text):
        return ""
    
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters (keep letters, numbers, spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Split into words
    words = text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    
    # Lemmatize words
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join back into text
    return ' '.join(words)

def standardize_dataset(df, text_col, label_col):
    """
    Standardize dataset format
    
    Args:
        df (pd.DataFrame): Input dataframe
        text_col (str): Name of text column
        label_col (str): Name of label column
        
    Returns:
        pd.DataFrame: Standardized dataframe
    """
    df_clean = df.copy()
    
    # Rename columns to standard names
    df_clean = df_clean.rename(columns={
        text_col: 'text',
        label_col: 'label'
    })
    
    # Keep only necessary columns
    df_clean = df_clean[['text', 'label']].copy()
    
    # Remove rows with missing text
    df_clean = df_clean.dropna(subset=['text'])
    
    # Preprocess text
    df_clean['text'] = df_clean['text'].apply(clean_text)
    
    # Remove empty texts after preprocessing
    df_clean = df_clean[df_clean['text'].str.len() > 0]
    
    return df_clean


def convert_labels_to_binary(df, label_mapping=None):
    """Convert labels to binary format (0=real, 1=fake)"""
    df_binary = df.copy()
    
    # Default label mapping based on your data
    if label_mapping is None:
        label_mapping = {
            # Product reviews (Kaggle)
            'OR': 0,   # Original = real
            'CG': 1,   # Computer Generated = fake
            
            # Hotel reviews (DOSC)
            'truthful': 0,    # Real reviews
            'deceptive': 1,   # Fake reviews
            
            0: 0,
            1: 1,
            '0': 0,
            '1': 1,
        }
    
    # Apply mapping
    df_binary['label'] = df_binary['label'].map(label_mapping)
    
    # Remove rows with unmapped labels
    df_binary = df_binary.dropna(subset=['label'])
    df_binary['label'] = df_binary['label'].astype(int)
    
    return df_binary