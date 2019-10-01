import requests

answer = {"answer": open("answer2.json", "rb")}
response = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=89dc8e7e8ab5e49a9edde1d885fb601fa627e4c8", files=answer)
print(response.json())