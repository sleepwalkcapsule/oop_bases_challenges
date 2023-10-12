"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        text_len = len(self.text)
        word_count = len(self.text.split())
        return f'Total text length: {text_len}, total number of words in the text: {word_count}'


if __name__ == '__main__':
    text = "Здесь кучка какого-то текста"

    text_processor = TextProcessor(text)

    print("Text Processor:")
    print("Uppercase text:", text_processor.to_upper())
    print(text_processor.summarize())
    advanced_text_processor = AdvancedTextProcessor(text)
    print("\nAdvanced Text Processor:")
    print("Uppercase text:", advanced_text_processor.to_upper())
    print(advanced_text_processor.summarize())
