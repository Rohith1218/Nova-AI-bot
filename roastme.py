import requests
import mindsdb

session = requests.Session()
session.post('cloud.mindsdb.com', json={
    'email': 'your mail',
    'password': 'passkey'
})


def roastme():
    while True:
        inp = input("user: ")

        if inp.lower() == 'exit':
            break

        # Query
        query = f"""SELECT response from mindsdb.roastme_model 
                    WHERE author_username = "dude" 
                    AND text='{inp}'"""

        mresp = session.post('cloud.mindsdb.com', json={'query': query})

        mock_data = mresp.json()
        mdata = mock_data['data'][0]
        trimmed_data = [sentence[17:] for sentence in mdata]
        print(*trimmed_data)



#call your function here
