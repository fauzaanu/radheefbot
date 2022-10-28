import requests


def get_radheef_val(word):
    url = "https://www.radheef.mv/api/basfoiy/search_word"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"searchText\"\r\n\r\n{word}\r\n-----011000010111000001101001--\r\n"
    # headers were generated code from insomnia
    headers = {
        "cookie": "ci_session=e2cals79khosk6e9nbcubpkednnl5rq9",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }



    payload = payload.encode()
    response = requests.request("POST", url, data=payload, headers=headers)

    if response.json()['data']:
        return [resp["meaning_text"] for resp in response.json()['data']]
    else:
        return None


if __name__ == "__main__":
    pass
    # print(get_radheef_val(''))