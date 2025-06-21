def calculate_overlap(active_ranks, passive_ranks, k=5): 
    overlap = len(set(active_ranks[:k]) & set(passive_ranks[:k])) / k
    return overlap
    
    


def evaluate_retrieval(results):
    recall_at_active = {i: [] for i in range(1, 6)}
    recall_at_passive = {i: [] for i in range(1, 6)}
    mrr_scores = []
    dropout_counts = {1: 0, 3: 0}
    overlap_at = {1: 0, 3: 0, 5: 0}
    total_queries = 0

    for qid, retrieved in results.items():
        total_queries += 1
        correct = qid  # gold ID matches query ID

        active_ranks = retrieved["active"]
        passive_ranks = retrieved["passive"]

        # 1. Recall@K
        for k in range(1, 6):
            recall_at_active[k].append(1 if correct in active_ranks[:k] else 0)
            recall_at_passive[k].append(1 if correct in passive_ranks[:k] else 0)

        # 2. MRR
        try:
            rank = active_ranks.index(correct) + 1
            mrr_scores.append(1 / rank)
        except ValueError:
            mrr_scores.append(0)

        # 3. Overlap@K
        for k in [1, 3, 5]:
            overlap = len(set(active_ranks[:k]) & set(passive_ranks[:k])) / k
            overlap_at[k] += overlap

        # 4. Dropout Analysis
        if correct in active_ranks[:3] and correct not in active_ranks[:1]:
            dropout_counts[1] += 1
        if correct in active_ranks[:5] and correct not in active_ranks[:3]:
            dropout_counts[3] += 1

    metrics = {
        **{
            "MRR": round(sum(mrr_scores) / total_queries, 4),
            "AvgOverlap@1": round(overlap_at[1] / total_queries, 4),
            "AvgOverlap@3": round(overlap_at[3] / total_queries, 4),
            "AvgOverlap@5": round(overlap_at[5] / total_queries, 4),
            "Dropout@1→3": dropout_counts[1],
            "Dropout@3→5": dropout_counts[3],
            "Total": total_queries,
        },
        **{
            f"Recall@{k}_active": round(sum(recall_at_active[k]) / total_queries, 4)
            for k in range(1, 6)
        },
        **{
            f"Recall@{k}_passive": round(sum(recall_at_passive[k]) / total_queries, 4)
            for k in range(1, 6)
        },
    }

    return metrics