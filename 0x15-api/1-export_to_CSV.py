#!/usr/bin/python3
# Python scipt to run Employee ID and return TODO list form REST API

if __name__ == "__main__":
    import requests as re
    import json
    import csv
    from sys import argv

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = re.get(url + '/{}'.format(user_id)).json()
    todo = re.get(url + '/{}/todos'.format(user_id)).json()
    with open("{}.csv".format(user_id), 'w') as csvfile:
        fil = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            fil.writerow([user_id,
                          user.get('name'),
                          task.get('completed'),
                          task.get('title')])
