import requests as re

def genre_response():
        url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"

        response = re.get(url)

        if response.ok:
                return response.text
        else:
                return f"There was an error: {response.status_code}"

def story_response():

        url = "https://binaryjazz.us/wp-json/genrenator/v1/story/"    

        response = re.get(url)

        if response.ok:
             print(response.text)
        else:
             print(f"There was an error: {response.status_code}")