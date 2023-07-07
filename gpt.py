import requests
import mindsdb

session = requests.Session()
session.post('cloud.mindsdb.com', json={
    'email': 'your email',
    'password': 'your passkey'
})


def gpt():
    while True:
        inp = input("user: ")

        if inp.lower() == 'exit':
            print("i guess that's helpful")
            break

        # Query
        query = f"""SELECT response FROM mindsdb.gpt_model
                   WHERE author_username = 'Bro'
                   AND text = '{inp}'"""

        resp = session.post('cloud.mindsdb.com', json={'query': query})

        resp_data = resp.json()
        data = resp_data['data'][0]
        print(*data)


#call your function here
