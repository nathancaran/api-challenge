import requests as re

def genre_response(number = 1):
        url = f"https://binaryjazz.us/wp-json/genrenator/v1/genre/{number}"

        response = re.get(url)

        if response.ok:
            return response.text
        else:
            return f"There was an error: {response.status_code}"

def story_response(number = 1):

        url = f"https://binaryjazz.us/wp-json/genrenator/v1/story/{number}"

        response = re.get(url)

        if response.ok:
             return response.text
        else:
             return f"There was an error: {response.status_code}"