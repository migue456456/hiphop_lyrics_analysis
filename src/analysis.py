from .categories import categories

def sort_counts(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

def category_totals(word_counts):
    totals = {}
    for name, words in categories.items():
        totals[name] = sum(word_counts.get(w, 0) for w in words)
    return totals
