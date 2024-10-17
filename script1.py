def flatten(nested_list):
    """
    Aplatit une liste imbriquée
    """
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

def find_duplicates(lst):
    """
    Trouve les éléments dupliqués dans une liste.
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
