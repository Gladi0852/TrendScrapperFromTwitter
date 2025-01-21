from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proxy_rotate import rotateProxyList
import re
from datetime import datetime
from database import saveData, getData
from flask import Flask, jsonify
from flask_cors import CORS
import os
import time
from login import login

app = Flask(__name__)
CORS(app)

@app.route('/get-trending', methods=['GET'])
def getTrendingTopics():
    trending_topics = []
    proxy = rotateProxyList("Webshare_10_proxies.txt")
    options = webdriver.ChromeOptions()

    profile_path = os.path.join(os.path.expanduser("~"), "selenium_profile")  # it's created in the home directory
    options.add_argument(f"--user-data-dir={profile_path}")  
    options.add_argument("--disable-popup-blocking") 
    options.add_argument("--headless")
    options.add_argument(f'--proxy-server=http://{proxy}')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://x.com/home")
        # time.sleep(5)

        if "Home / X" not in driver.title:
            print("Not logged in. Logging in...")
            login(driver)            
        
        driver.get("https://x.com/explore/tabs/trending")
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='trend']"))
        )
        trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")
        for trend in trends:
            content = trend.text.splitlines()
            topic = content[-2]
            if re.match(r'^[A-Za-z0-9\s#]*$', topic):
                if len(trending_topics) < 5:
                    trending_topics.append(topic)
                else:
                    break
                
        if len(trending_topics) < 5:
            raise ValueError(f"Expected at least 5 trending topics, but got {len(trending_topics)}")
        
        data = {
            "trend1": trending_topics[0],
            "trend2":trending_topics[1],
            "trend3":trending_topics[2],
            "trend4":trending_topics[3],
            "trend5":trending_topics[4],
            "timestamp": datetime.now().strftime("%d %B %Y, %I:%M %p"),
            "ip":proxy
        }
        id = saveData(data)
        return getData(id)


    except Exception as e:
        print(f"Error: {e}")
        return {"message": f"Error - {e}"}

    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(debug=True)