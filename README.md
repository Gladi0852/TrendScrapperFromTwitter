This project is a Twitter Trending Topics Scraper, built to collect and store the current trending topics on Twitter. It uses Selenium to interact with Twitter's website and MongoDB to store the scraped data.

Key Features:

1. Trending Topics Scraping:
  Automatically fetches the top 5 trending topics from Twitter.
  Uses Selenium to navigate and extract the data from the "Explore" section on Twitter.

2. Proxy Rotation:
  Rotates proxies from a file to avoid IP bans and maintain anonymity during scraping.

3. Data Storage:
  Stores the scraped topics in a MongoDB database with the relevant timestamp and proxy used.

4. Login Handling:
  If the user is not logged in in twitter, it triggers the login process using Selenium.

5. Error Handling:
  Handles exceptions and ensures the scraping process runs smoothly, even when issues occur.

Steps to run:

Download the zip file and extract
    #Go to the backend folder, open terminal in backend
1. create a virtual environment and activate that
2.     pip install -r requirements.txt
3. if want to send using proxy then get your own proxy list and save it to a .txt file that you can give it here  - "proxy = rotateProxyList("file_name.txt")" or if don't want to send request using proxy then
4.   comment out above line and "options.add_argument(f'--proxy-server=http://{proxy}')" this line
5.   create a .env file and fill this
6.     email = "twitter username or email"
7.     password = "twitter_password"
8.     your_username = "twitter_username"
9.     mongo_url = "your_mongo_atlas_url"

10. create a database named = "ScrappingTwitter"
11. and collection named = "trending_topics"

Now you are good to go. run the python server using - python app.py

  #Go to the frontend folder, open terminal in frontend
1.     npm install
2.     npm run dev

and you are done with running the project. If you are facing problem while logging then open backend folder and uncomment

    options.add_argument("--headless") 
this line now you can see what's happing.

If you are seeing some problem while its logging(all automatic and once after once successful logging it will not happen again) go to backend folder and search for 

    time.sleep(5) 
in every python folder. All are commented out, so just uncomment that

-----If still facing issue feel free to connect with me----

Thank You
