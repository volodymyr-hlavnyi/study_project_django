import unittest
from text_processor import Text_Processor


class TestTextProcessor(unittest.TestCase):

    def test_clean_text_removes_non_alpha(self):
        processor = Text_Processor("Hello, World!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "hello world")

    def test_clean_text_to_lowercase(self):
        processor = Text_Processor("123 ABC!!!")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "abc")

    def test_clean_text_empty_string(self):
        processor = Text_Processor("")
        processor.clean_text()
        self.assertEqual(processor.cleaned_text, "")

    def test_remove_stop_words(self):
        processor = Text_Processor("this is a test")
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_without_clean_text(self):
        processor = Text_Processor("this is a test")
        processor.remove_stop_words(['this', 'is'])
        self.assertEqual(processor.cleaned_text, "a test")

    def test_remove_stop_words_no_stop_words(self):
        processor = Text_Processor("hello world")
        processor.remove_stop_words([])
        self.assertEqual(processor.cleaned_text, "hello world")


if __name__ == '__main__':
    unittest.main()
