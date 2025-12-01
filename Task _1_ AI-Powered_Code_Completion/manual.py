def sort_list_of_dicts_manual(data, key):
    """
    Manually implemented function to sort a list of dictionaries by specific key
    """
    # Using sorted() with lambda function as key
    return sorted(data, key=lambda x: x[key])

# Example usage
data = [
    {'name': 'Samuel', 'age': 24},
    {'name': 'Eglay', 'age': 32},
    {'name': 'Eustine', 'age': 22}
]

sorted_data = sort_list_of_dicts_manual(data, 'age')
print(sorted_data)