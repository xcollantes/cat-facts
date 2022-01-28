import requests


def main():
    print("Hello there!! This is a text.")
    res = requests.get("https://catfact.ninja/fact")
    print(res.text)
    
if __name__ == "__main__":
    main()
