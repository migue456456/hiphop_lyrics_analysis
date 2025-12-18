from .categories import categories

class Analysis:
    '''
    Represents basic analysis on word-count data
    attribute: word_counts (dictionary of word frequencies)
    '''

    def __init__(self, word_counts):
        self.word_counts = word_counts  # store the word-count dictionary

    def sort_counts(self):
        '''
        Sorts word counts from largest to smallest
        returns: list of (word, count) tuples
        '''
        # sort items in descending order by count
        return sorted(
            self.word_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

    def category_totals(self):
        '''
        Computes total counts for each category
        returns: dictionary of category totals
        '''
        totals = {}  # start empty dictionary

        for name, words in categories.items():  # loop over each category
            total = 0  # start count at 0
            for w in words:  # loop over words in category
                total = total + self.word_counts.get(w, 0)  # add count if word exists
            totals[name] = total  # save total for this category

        return totals
