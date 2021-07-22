from animal_suggestion.tree import tree


# Driver Code
if __name__ == "__main__":
    t = tree()
    t.insert_word('ant')
    t.insert_word('antelope')
    t.insert_word('bird')

    for prefix in ['a', 'bir', 'elephan', 'ante']:
        print(f"Recommendation for animals that start with {prefix:15}: {t.get_with_prefix(prefix)}")

