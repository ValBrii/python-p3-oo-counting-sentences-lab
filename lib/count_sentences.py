#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            self._value = ""
            print("The value must be a string.")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            self._value = ""
            print("The value must be a string.")

    def is_sentence(self):
        """Returns True if the string ends with a period, otherwise False."""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if the string ends with a question mark, otherwise False."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark, otherwise False."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Returns the number of sentences in the string."""
        
        modified_value = re.sub(r'[!?.]+', '.', self.value)
        sentences = modified_value.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

      
