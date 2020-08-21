'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    query = "th"

    # base case
    if len(word) < len(query):
        return 0
    
    if word[0:2] == query:
        # the query string was found, keep searching
        return 1 + count_th(word[1:])
    else:
        # not found, keep searching
        return 0 + count_th(word[1:])