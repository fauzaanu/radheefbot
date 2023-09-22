import requests
from google_translate import translate

def get_radheef_val(word):
    if len(word.split()) > 1:
        return translate(word)
    elif len(word.split()) == 1:
        word = translate(word)
        print(word)

        url = "https://www.radheef.mv/api/basfoiy/search_word"

        # generated code from insomnia

        payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"searchText\"\r\n\r\n{word}\r\n-----011000010111000001101001--\r\n"
        headers = {
            "cookie": "ci_session=e2cals79khosk6e9nbcubpkednnl5rq9",
            "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
        }

        payload = payload.encode()
        response = requests.request("POST", url, data=payload, headers=headers)
        # print(response.json())

        if response.json()['data']:
            return [resp for resp in response.json()['data']]
        else:
            return word
    else:
        return "Please enter a valid word"


if __name__ == "__main__":
    pass
    # print(get_radheef_val(''))