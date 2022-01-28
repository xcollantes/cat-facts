import requests
import json
from absl import app


def main(argv):
    print("Hello there!! This is a text.")
    res = requests.get("https://catfact.ninja/fact")
    text = json.loads(res.content)
    print(text["fact"])
    
if __name__ == "__main__":
    app.run(main)
