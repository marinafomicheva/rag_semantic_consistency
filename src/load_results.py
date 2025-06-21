import json
def load_results(language, model_name):
    with open(f"results/retrieval_results_{language}_{model_name}.json", "r") as f:
        return json.load(f)