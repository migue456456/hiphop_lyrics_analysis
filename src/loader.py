import os  # Used for building file paths and working with the filesystem
from cleaning import TextCleaner  # Import your TextCleaner class for cleaning text

class CorpusLoader:
    """
    Class for loading and storing text corpora from multiple files (e.g., rap albums).

    Attributes:
        cleaner (TextCleaner): instance of TextCleaner for loading and cleaning text
        corpus (dict): dictionary mapping file names to raw text
    """

    def __init__(self):
        # Initialize the TextCleaner
        self.cleaner = TextCleaner()
        # Dictionary to store loaded text
        self.corpus = {}

    def load_albums(self, album_files, data_dir="data_raw"):
        """
        Loads multiple text files from a directory into the corpus dictionary.

        Args:
            album_files (list): List of album file names (strings)
            data_dir (str): Directory where the text files are stored
        """
        for file in album_files:
            # Build full path to the text file
            path = os.path.join(data_dir, file)

            # Load the text from the file using TextCleaner
            text = self.cleaner.load_text(path)

            # Add text to the corpus dictionary, keyed by file name
            self.corpus[file] = text

            # Optional: print a confirmation for each loaded file
            print(f"Loaded {file} ({len(text)} characters)")

    def preview_album(self, file_name, n_chars=500):
        """
        Returns a preview (first n_chars characters) of a loaded album.

        Args:
            file_name (str): Name of the file in the corpus dictionary
            n_chars (int): Number of characters to preview
        Returns:
            str: First n_chars characters of the text
        """
        if file_name in self.corpus:
            return self.corpus[file_name][:n_chars]
        else:
            return f"File '{file_name}' not found in corpus."
