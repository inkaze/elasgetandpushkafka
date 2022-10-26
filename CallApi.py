from urllib import response
from fastapi import FastAPI
import requests

def getResultFromApi(text):
 response = requests.get("http://127.0.0.1:8000/test/" + text)
 return response.text



def main():
    getResultFromApi("chao ban minh den tu hom qua")

if __name__ == "__main__":
    main()
