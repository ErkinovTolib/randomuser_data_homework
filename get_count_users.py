import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    sum = 0
    results = data["results"]
    for i in results:
        sum += 1
    return sum

    

f = open('randomuser_data.json','r')
data = f.read()
print(get_count_users(data))