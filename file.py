import json
import hashlib
import requests

def to_alphabet(ascii_num):
    ascii_first_letter_pos = 96
    return ascii_num - ascii_first_letter_pos

def to_ascii(alphabet_num):
    ascii_first_letter_pos = 96
    return alphabet_num + ascii_first_letter_pos

def is_letter(ascii_num):
    ascii_last_letter_pos = 123
    ascii_first_letter_pos = 96
    if (ascii_num > ascii_first_letter_pos) and (ascii_num < ascii_last_letter_pos):
        return True
    else:
        return False

def write_file(data):
    with open("answer2.json", "w") as file:
        json.dump(data, file)

def submit_solution():
    answer = {"answer": open("answer2.json", "r")}
    response = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=89dc8e7e8ab5e49a9edde1d885fb601fa627e4c8", files=answer)
    return response

response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=89dc8e7e8ab5e49a9edde1d885fb601fa627e4c8")
data = response.json()
decrypted = ""
encrypted = data["cifrado"]
shift_num = data["numero_casas"]
alphabet_letters_qtd = 26

for letter in encrypted:
    ascii_num = ord(letter)
    if is_letter(ascii_num):
        alphabet_num = to_alphabet(ascii_num)
        alphabet_num -= shift_num
        decrypted += chr(to_ascii(alphabet_num % alphabet_letters_qtd))
    else:
        decrypted += letter    
file_json = {
	"numero_casas": shift_num,
	"token": data["token"],
	"cifrado": encrypted,
	"decifrado": decrypted,
	"resumo_criptografico": hashlib.sha1(decrypted).hexdigest()
}

write_file(file_json)

score = submit_solution()
print(score.json())
