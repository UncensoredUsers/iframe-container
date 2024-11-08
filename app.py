from flask import Flask, render_template
from threading import Timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

# 전역 변수로 URL을 저장
url_to_load = None

@app.route("/")
def index():
    return render_template("index.html", url=url_to_load)

def open_chromium():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("http://127.0.0.1:5000")

if __name__ == "__main__":

    url_to_load = input("Enter the website URL you want to view: ")
    if not url_to_load.startswith("http"):
        url_to_load = "https://" + url_to_load

    Timer(1, open_chromium).start()
    app.run(debug=True)
