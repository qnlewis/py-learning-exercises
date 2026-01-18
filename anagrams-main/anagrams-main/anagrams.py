

def anagrams(str1, str2):
    """ Check if two strings are anagrams of each other.

    Args:
        str1: First string to compare
        str2: Second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise"""
        
    def normalize(string):
        return [characters.lower() for characters in string if characters.isalpha()]
    
    chars1 = normalize(str1)
    chars2 = normalize(str2)
    
    if len(chars1) != len(chars2):
        return False
    
    from collections import defaultdict
    count1 = defaultdict(int)
    count2 = defaultdict(int)
    
    for characters in chars1:
        count1[characters] += 1
    
    for characters in chars2:
        count2[characters] += 1
    
    return count1 == count2