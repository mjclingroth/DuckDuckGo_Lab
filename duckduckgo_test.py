# Max Clingroth
# L09 DuckDuckGo

import requests

url = "https://api.duckduckgo.com"
presidents = ["washington", "adams", "jefferson", "madison", "monroe",
              "jackson", "buren", "harrison", "tyler", "polk", "taylor",
              "fillmore", "pierce", "buchanan", "lincoln", "johnson",
              "grant", "hayes", "garfield", "arthur", "cleveland",
              "mckinley", "roosevelt", "taft", "wilson", "harding",
              "coolidge", "hoover", "truman", "eisenhower", "kennedy",
              "nixon", "ford", "carter", "reagan", "bush", "clinton",
              "obama", "trump", "biden"]


def test_ddg():
    response = requests.get(url + "/?q=Presidents+of+the+United+States&format=json")

    # Stores text of RelatedTopics in a list
    response_text = []
    for item in response.json()["RelatedTopics"]:
        response_text.append(item["Text"].lower())

    # Checks if each president's last name is present in response_text
    # and adds to a list if true
    president_check = []
    for president in presidents:
        for item in response_text:
            if president in item:
                president_check.append(president)
                break

    # Asserts all presidents have been found in response_text
    for president in presidents:
        assert president in president_check
