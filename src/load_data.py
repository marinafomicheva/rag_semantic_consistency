import pandas as pd

def load_data(language):
    df = pd.read_csv("rag_dataset_template.csv", sep=';')
    df = df[df['language']==language]
    return df