from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel

models = {
     "EuroBERT": {
        "model": AutoModel.from_pretrained("EuroBERT/EuroBERT-210m", trust_remote_code=True
        ),
        "tokenizer": AutoTokenizer.from_pretrained("EuroBERT/EuroBERT-210m", trust_remote_code=True
        ),
        "type": "transformer",
    },
        "LaBSE": {
        "model": AutoModel.from_pretrained("sentence-transformers/LaBSE"),
        "tokenizer": AutoTokenizer.from_pretrained("sentence-transformers/LaBSE"),
        "type": "transformer",
    },

       "EuroBERT_FT": {
        "model": AutoModel.from_pretrained("nomic-ai/eurobert-210m-2e4-128sl-full-ft", trust_remote_code=True
        ),
        "tokenizer": AutoTokenizer.from_pretrained("nomic-ai/eurobert-210m-2e4-128sl-full-ft", trust_remote_code=True
        ),
        "type": "transformer",
    },
        "RuModernBERT_USER2_FT": {
        "model": AutoModel.from_pretrained("deepvk/USER2-base"),
        "tokenizer": AutoTokenizer.from_pretrained("deepvk/USER2-base"),
        "type": "transformer",
    },
    "RuModernBERT": {
        "model": AutoModel.from_pretrained(
            "deepvk/RuModernBERT-base", output_attentions=True, trust_remote_code=True
        ),
        "tokenizer": AutoTokenizer.from_pretrained(
            "deepvk/RuModernBERT-base", trust_remote_code=True
        ),
        "type": "transformer",
    },

    "E5": {
        "model": AutoModel.from_pretrained("intfloat/multilingual-e5-base"),
        "tokenizer": AutoTokenizer.from_pretrained("intfloat/multilingual-e5-base"),
        "type": "transformer",
    },
    "MiniLM": {
        "model": SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2"),
        "type": "sentence-transformer",
    },
    "BERT-multilingual": {
        "model": AutoModel.from_pretrained("bert-base-multilingual-cased"),
        "tokenizer": AutoTokenizer.from_pretrained("bert-base-multilingual-cased"),
        "type": "transformer",
    },
    "gte-multilingual-base": {
        "model": AutoModel.from_pretrained(
            "Alibaba-NLP/gte-multilingual-base", trust_remote_code=True
        ),
        "tokenizer": AutoTokenizer.from_pretrained(
            "Alibaba-NLP/gte-multilingual-base", trust_remote_code=True
        ),
        "type": "transformer",
    },
    "Granite-Embedding-Multilingual": {
        "model": AutoModel.from_pretrained(
            "ibm-granite/granite-embedding-278m-multilingual"
        ),
        "tokenizer": AutoTokenizer.from_pretrained(
            "ibm-granite/granite-embedding-278m-multilingual"
        ),
        "type": "transformer",
    },
}