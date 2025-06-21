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
- Retrieval model evaluation (`Overlap@K`, `MRR`, `Recall`)
- Paraphrase sensitivity analysis
- Contrastive fine-tuning benchmarks

---

