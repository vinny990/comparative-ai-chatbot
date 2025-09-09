import sqlite3
import pandas as pd
from textblob import TextBlob

def analyze_responses():
    conn = sqlite3.connect("responses.db")
    df = pd.read_sql_query("SELECT * FROM responses", conn)
    conn.close()
    
    # Calculate response length
    df['openai_length'] = df['openai_response'].apply(len)
    df['claude_length'] = df['claude_response'].apply(len)
    df['gemini_length'] = df['gemini_response'].apply(len)
    
    # Sentiment analysis
    df['openai_sentiment'] = df['openai_response'].apply(lambda x: 
TextBlob(x).sentiment.polarity if not x.startswith('Error') else 0)
    df['claude_sentiment'] = df['claude_response'].apply(lambda x: 
TextBlob(x).sentiment.polarity if not x.startswith('Error') else 0)
    df['gemini_sentiment'] = df['gemini_response'].apply(lambda x: 
TextBlob(x).sentiment.polarity if not x.startswith('Error') else 0)
    
    # Correlation: Prompt length vs. sentiment
    df['prompt_length'] = df['prompt'].apply(len)
    correlation = df[['prompt_length', 'openai_sentiment', 
'claude_sentiment', 'gemini_sentiment']].corr()
    return {
        'avg_lengths': {
            'openai': df['openai_length'].mean(),
            'claude': df['claude_length'].mean(),
            'gemini': df['gemini_length'].mean()
        },
        'avg_sentiments': {
            'openai': df['openai_sentiment'].mean(),
            'claude': df['claude_sentiment'].mean(),
            'gemini': df['gemini_sentiment'].mean()
        },
        'correlation': correlation.to_dict()
    }
