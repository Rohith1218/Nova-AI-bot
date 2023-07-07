def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('afplay output.mp3')
    os.remove('output.mp3')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred."




def get_news_articles(api_key):
    url = 'newsapi.org'
    params = {
        'apiKey': api_key,
        'country': 'in'  
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['status'] == 'ok':
        articles = data['articles']
        for article in articles:
            title = article['title']
            description = article['description']
            print(f'Title: {title}')
            print(f'Description: {description}')
            print('---')



session = requests.Session()
session.post('cloud.mindsdb.com', json={
    'email': 'your email',
    'password': 'your password'
})


def gpt():
    while True:
        inp = input("user: ")

        if inp.lower() == 'exit':
            say("i guess that's helpful")
            break

        # Query
        query = f"""SELECT response FROM mindsdb.gpt_model
                   WHERE author_username = 'Bro'
                   AND text = '{inp}'"""

        resp = session.post('cloud.mindsdb.com', json={'query': query})

        resp_data = resp.json()
        data = resp_data['data'][0]
        print(*data)
        say(*data)


def roastme():
    while True:
        inp = input("user: ")

        if inp.lower() == 'exit':
            say("Bye bro")
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
        say(*trimmed_data)


if __name__ == '__main__':
    print("Hello, how can I help you?")
    say("Hello, how can I help you?")
    while True:
        print("Listening...")
        query = takecommand()

        if "open" in query.lower():
            sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
                     ["linkedin", "https://www.linkedin.com"], ["chat GPT", "https://chat.openai.com"]]
            for site in sites:
                if site[0].lower() in query.lower():
                    say(f"Opening {site[0]} now...")
                    webbrowser.open(site[1])
                    break

        if "search" in query.lower():
            search_query = query.lower().replace("search", "").strip()
            say(f"Searching on Google: {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        if "the time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            hour = int(hour) - 12
            min = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour}:{min}")

        if "news" in query.lower():
            api_key = 'your API key here'
            say("Fetching the latest news headlines...")
            get_news_articles(api_key)

        if "activate gpt" in query.lower():
            say("activating GPT and deactivating voice assistant")
            gpt()

        if "roast me" in query.lower():
            say("you sure dude")
            roastme()

        if "stop" in query.lower():
            say("see you later")
            exit()
