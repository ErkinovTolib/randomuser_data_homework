import get_data
import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = []
    f = open('randomuser_data.json')
    data = json.loads(f)
    results = data["results"]
    for e,v in results:
        if e == "email":
            emails.append(v)
    return emails

print(get_email('results'))