import requests

url = 'https://qvhuvdz1l4.execute-api.eu-central-1.amazonaws.com/inference'
# url = 'http://localhost:5000/inference'


def test(uri):
    raw_data = {'s3_uri': uri}
    try:
        response = requests.get(url, json=raw_data)
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    test('s3://glean-demo-bucket/img.png')
    test('s3://glean-demo-bucket/ocrscan.pdf')
