class node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_word = False

    def insert_word(self, word: str):
        if word is None or len(word) == 0:
            self.is_word = True
        else:
            letter = word[0]
            suffix = word[1:]

            letter_node = self.children.get(letter)
            if not letter_node:
                # add the letter as a valid child
                letter_node = node(letter)
                self.children[letter] = letter_node

            letter_node.insert_word(suffix)

    def get_child_node(self, letter: str):
        # given a letter, returns the child at that index or null
        return self.children.get(letter)

    def add_suffix(self, suffix: str):
        if not suffix:
            self.is_word = True
        else:
            prefix = suffix[0]
            remainder = suffix[1:]

            prefix_child = self.children.get(prefix)
            if not prefix_child:
                prefix_child = node(prefix)
            prefix_child.add_suffix(remainder)

    def __repr__(self):
        return self.value
