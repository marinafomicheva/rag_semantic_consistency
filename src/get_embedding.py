import torch

def get_embedding_transformer(tokenizer, model, text, pooling_method = 'mean'): 
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    last_hidden = outputs.last_hidden_state
    attention_mask = inputs["attention_mask"].unsqueeze(-1).expand(last_hidden.shape)
    masked_hidden = last_hidden * attention_mask
    if pooling_method == 'mean':
        mean_embedding = masked_hidden.sum(1) / attention_mask.sum(1)
        return mean_embedding.squeeze().numpy()
    else:
        return None

def get_embedding_sentence_transformer(model, text):
    return model.encode(text, convert_to_numpy=True)


def get_embedding(model_type, tokenizer = None, model = None, text = '', pooling_method = 'mean'):
    if model_type == 'transformer':
        return get_embedding_transformer(tokenizer, model, text, pooling_method)
    elif model_type == 'sentence-transformer':
        return get_embedding_sentence_transformer(model, text)