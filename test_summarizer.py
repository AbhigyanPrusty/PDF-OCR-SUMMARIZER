import unittest
import os
from dotenv import load_dotenv
from utils.summarizer import summarize_text

# Load environment variables from .env file
load_dotenv()

class TestSummarizer(unittest.TestCase):

    def test_summarize_text(self):
        # Test input text for summarization
        test_text = """
        Hugging Face is a company based in New York. It is known for its work in machine learning, particularly natural language processing (NLP). The company developed the popular open-source library called Transformers. This library contains implementations of many state-of-the-art models, such as BERT, GPT, and T5. Hugging Face has become a key player in the AI community, especially in the domain of NLP, offering resources, datasets, and pre-trained models.
        """

        # Call summarize_text to get a summary
        summary = summarize_text(test_text)

        # Check that the summary is not empty
        self.assertIsNotNone(summary)
        self.assertGreater(len(summary), 0)

        # Check if the summary contains expected keywords or structure
        self.assertIn("Hugging Face", summary)
        self.assertIn("machine learning", summary)
        self.assertIn("NLP", summary)

if __name__ == "__main__":
    unittest.main()
