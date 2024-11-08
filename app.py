from flask import Flask, render_template
from threading import Timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # 자동으로 드라이버 관리

app = Flask(__name__)

# 전역 변수로 URL을 저장
url_to_load = None

@app.route("/")
def index():
    return render_template("index.html", url=url_to_load)

def open_chromium():
    # Chrome 옵션 설정 (필요에 따라 크롬 옵션을 추가할 수 있습니다.)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 브라우저를 최대화로 시작
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("http://127.0.0.1:5000")  # Flask 서버의 URL로 이동

if __name__ == "__main__":
    # Python 콘솔에서 사용자에게 URL을 입력받습니다.
    url_to_load = input("Enter the website URL you want to view: ")
    if not url_to_load.startswith("http"):
        url_to_load = "https://" + url_to_load

    # Flask 서버가 시작된 후 1초 뒤에 Selenium을 통해 크로미움 기반 브라우저를 엽니다.
    Timer(1, open_chromium).start()
    app.run(debug=True)
