## Retrieval and Evaluation

This repository investigates **semantic consistency** in Retrieval-Augmented Generation (RAG) systems, focusing on how encoder-only models handle **active/passive voice alternation** in English and Russian. It evaluates whether semantically equivalent queries retrieve overlapping sets of supporting passages.

---

### 📥 Retrieval Pipeline

Dense retrieval is conducted using FAISS-based indexing and query embedding.

## 📊 Evaluation Metrics

- **Overlap@K**: Degree of overlap in retrieved passages for active/passive forms
- **Recall@K**: Whether a gold passage appears within the top K results
- **MRR (Mean Reciprocal Rank)**: The Reciprocal of the rank of the first relevant passage retrieved

---

## 🤖 Models Evaluated

- `EuroBERT`, `EuroBERT_FT: nomic-ai/eurobert-210m-2e4-128sl-full-ft`
- `RuModernBERT`, `RuModernBERT_USER2_FT: deepvk/USER2-base`
- `BERT-multilingual`, `MiniLM`, `LaBSE`, `E5`, `Granite`, `GTE`.


## 📚 Dataset: Active/Passive Queries for English and Russian

This dataset supports research on **semantic consistency** and **retrieval quality** in encoder-only models under syntactic variation — specifically, active vs. passive voice.  
It was developed as part of a Master's thesis:

> _**Semantic Consistency in RAG: Evaluating Modern Encoder-Only Models on Active and Passive Voice in English and Russian**_

---

### 📁 File

- `rag_dataset_active_passive.csv`  
  A UTF-8 encoded CSV using `;` as the delimiter.

---

### 📄 Format

Each row represents a bilingual factual question pair with corresponding support information.

| **Column Name**     | **Description**                                                                |
|---------------------|--------------------------------------------------------------------------------|
| `id`                | Unique ID (e.g., `en_001`, `ru_135`)                                           |
| `language`          | Language code (`en` for English, `ru` for Russian)                             |
| `query_active`      | Active-voice version of the question                                           |
| `query_passive`     | Passive-voice paraphrase of the same question                                  |
| `answer`            | Gold-standard answer (named entity or fact)                                    |
| `support_passage`   | Supporting passage containing the answer, used for retrieval evaluation        |

---

### 🌍 Languages

- **English** — 250 question pairs  
- **Russian** — 250 question pairs

---

### 🔍 Use Cases

Designed for evaluating how sentence embeddings generalize across syntactic paraphrases in **Retrieval-Augmented Generation (RAG)** pipelines.

**Especially useful for:**
- Retrieval model evaluation (`Overlap@K`, `MRR`, `Recall@K`)
- Paraphrase sensitivity analysis
- Contrastive fine-tuning benchmarks

---

