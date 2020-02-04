import json
import requests

def getReq(word):
    try:
        url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=b7177fa6-0e13-4426-b7ab-851c7b69400b"
        resp = requests.get(url)
        return resp.json()
    except requests.exceptions.ConnectionError:
        return False

def getWordMean(word):
    data = getReq(word)
    if data is not False:
        try:
            gramList = []
            for indc in range(len(data)):
                toAdd = {
                        "word": data[indc]['meta']['id'],
                        "pos":  data[indc]['fl'],
                        "defn": data[indc]['shortdef']
                        }
                gramList.append(toAdd)
            return toAdd
        except KeyError:
            return toAdd
        except TypeError:
            return data
    else:
        return "No internet"
