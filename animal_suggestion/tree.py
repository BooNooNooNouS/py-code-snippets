import queue

from animal_suggestion.node import node


class tree:

    def __init__(self):
        # Initialize the tree with a root node '*'
        self.root = node('*')

    def insert_word(self, word):
        self.root.insert_word(word)

    def get_with_prefix(self, word):
        # First we find the node corresponding to the prefix
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if not node:
                return None

        # Now that we're at the node corresponding to the prefix,
        # find any word by traversing the tree.  Since we only
        # want one answer, we can use a naive approach of navigating
        # using the first child until

        suffix = ''
        while node:
            suffix += node.value

            # There's no need to continue down if
            if node.is_word:
                break

            # pop any 1 item, we don't really care at this point.
            # we use an iterator since it's more efficient ( O(1) )
            next_key = next(iter(node.children))
            node = node.children.get(next_key)

        # make sure we don't duplicate the last character of the word, since
        # it's also the first character of the suffix
        return word[:-1] + suffix






