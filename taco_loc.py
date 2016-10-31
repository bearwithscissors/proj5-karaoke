def get_locations():
    """
    Return with the provided location list at data/tacobell.text
    (could be extended to take location as argument)
    Args: None
    Returns: locations
    """
    places = [ ]
    tacolist = "data/tacobell.txt"
    ls = open(tacolist, 'r')

    for line in ls:
        line = line.strip()
        line_data = line.split(",")
        places.append(line_data)
    places.sort()
    return places

print(get_locations())
