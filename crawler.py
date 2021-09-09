import requests

from bs4 import BeautifulSoup

r = requests.get("https://computer-nach-mass.de/html/firmenprofil.html")

html = """<html> <p>Ich bin ein Absatz</p><p>Hier ist noch ein Absatz!</p>

            </html>
            """


doc = BeautifulSoup(html,"html.parser")

print(doc.find_all("p"))

for x  in doc.find_all("p"):
    print(x.attrs)