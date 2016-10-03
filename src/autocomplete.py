
class AutoCompleter(object):
    """Create an auto compeleter."""

    def __init__(self, vocab, max_completions=5):
        """Initilizae auto completer."""
        self.vocab = vocab
        self.max_completions = max_completions
        if not isinstance(self.vocab, list):
            raise TypeError("Must enter a list of words.")
        
        for item in self.vocab:
            if not isinstance(item, str):
                raise TypeError("List must contain strings.")
        
    def __call__(self,input):
        """Call method of AutoCompleter."""
        if not isinstance(input, str):
            raise TypeError('Must enter a string.')
        result = []
        counter = 0
        for item in self.vocab:
            if item.startswith(input) and counter < self.max_completions:
                result.append(item)
                counter += 1
        return result

