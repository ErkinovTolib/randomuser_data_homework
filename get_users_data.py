import get_data

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    results = data["results"]
    list1 = []
    for i in results:
         list1.append({"first_name":i['name']['first'], "Last_name":i['name']['last'], "Phone":i['phone']})
    return list1

data = get_data('randomuser_data.json')
print(get_users_data(data))