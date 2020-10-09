from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import time
import re


def scrape_all():
    """Call all other functions"""
    # Initiate headless driver for deployment
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path)
    news_title, news_paragraph = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "main_image": featured_image(browser),
        "hemispheres": scrape_hemi(browser),
        "weather": twitter_weather(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
        }
    browser.quit()
    return data






# # {
# #  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "from splinter import Browser\n",
#     "from bs4 import BeautifulSoup as bs\n",
#     "import pandas as pd\n",
#     "import datetime as dt\n",
#     "import time\n",
#     "import re\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 2,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       "C:\\Users\\Boston\\anaconda3\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:493: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
#       "  FutureWarning,\n"
#      ]
#     },
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "{'news_title': \"NASA Readies Perseverance Mars Rover's Earthly Twin \", 'news_paragraph': \"Did you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape.\", 'main_image': 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA14934_hires.jpg', 'hemispheres': 'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg', 'weather': 'InSight sol 611 (2020-08-15) low -93.8ºC (-136.9ºF) high -15.9ºC (3.4ºF)\\nwinds from the WNW at 7.3 m/s (16.3 mph) gusting to 17.9 m/s (40.2 mph)\\npressure at 7.90 hPa', 'facts': '<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Description</th>\\n      <th>value</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>', 'last_modified': datetime.datetime(2020, 9, 8, 0, 52, 54, 709314)}\n"
#      ]
#     }
#    ],
#    "source": [
#     "def scrape_all():\n",
#     "    \"\"\"Call all other functions\"\"\"\n",
#     "    # Initiate headless driver for deployment\n",
#     "    executable_path = {'executable_path': 'chromedriver.exe'}\n",
#     "    browser = Browser('chrome', **executable_path)\n",
#     "    news_title, news_paragraph = mars_news(browser)\n",
#     "\n",
#     "    data = {\n",
#     "        \"news_title\": news_title,\n",
#     "        \"news_paragraph\": news_paragraph,\n",
#     "        \"main_image\": featured_image(browser),\n",
#     "        \"hemispheres\": scrape_hemi(browser),\n",
#     "        \"weather\": twitter_weather(browser),\n",
#     "        \"facts\": mars_facts(),\n",
#     "        \"last_modified\": dt.datetime.now()\n",
#     "        }\n",
#     "    browser.quit()\n",
#     "    return data\n",
#     "\n",
#     "\n",
#     "def mars_news(browser):\n",
#     "    \"\"\"Scrape Mars NEws\"\"\"\n",
#     "    #Website Location\n",
#     "    url=\"https://mars.nasa.gov/news/\"\n",
#     "    browser.visit(url)\n",
#     "    #puteverything in a beautiful soup\n",
#     "    html = browser.html\n",
#     "    soup=bs(html, 'html.parser')\n",
#     "    try:\n",
#     "        slide = soup.select_one(\"ul.item_list li.slide\")\n",
#     "        #captured all of the titles \n",
#     "        news_title=slide.find('div', class_=\"content_title\").get_text() \n",
#     "        #capturing the paragraph below title\n",
#     "        news_paragraph=slide.find('div', class_=\"article_teaser_body\").get_text()\n",
#     "    except AttributeError:\n",
#     "        return None, None\n",
#     "    return news_title, news_paragraph\n",
#     "    \n",
#     "\n",
#     "def featured_image(browser):\n",
#     "    \"\"\"Collect Main Image\"\"\"\n",
#     "    # Define URL & Visit\n",
#     "    url=\"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
#     "    browser.visit(url)\n",
#     "    # Find and click the full image button\n",
#     "    full_image_elem = browser.find_by_id('full_image')\n",
#     "    full_image_elem.click()\n",
#     "    # Find the more info button and click that\n",
#     "    browser.is_element_present_by_text('more info', wait_time=1)\n",
#     "    more_info_elem = browser.find_link_by_partial_text('more info')\n",
#     "    more_info_elem.click()\n",
#     "    #Scraping image page\n",
#     "    soup=bs(browser.html, 'html.parser')\n",
#     "    test=soup.body.find('img', class_=\"main_image\")\n",
#     "    image_address=test['src']\n",
#     "    main_image=f'https://www.jpl.nasa.gov{image_address}'\n",
#     "    return main_image\n",
#     "\n",
#     "def twitter_weather(browser):\n",
#     "    \"Mars Weather\"\n",
#     "    \n",
#     "    #Define URL\n",
#     "    twit_url = 'https://twitter.com/marswxreport?lang=en'\n",
#     "    browser.visit(twit_url)\n",
#     "    while True:\n",
#     "        if not browser.is_element_not_present_by_tag('article'):\n",
#     "            break\n",
#     "    twit_html = browser.html\n",
#     "    soup = bs(twit_html, 'html.parser')\n",
#     "    tweets = soup.find('article')\n",
#     "    \n",
#     "    for tweet in tweets:\n",
#     "        spans = tweet.find_all(\"span\")\n",
#     "        mars_weather = spans[4].get_text()\n",
#     "        #Replacing all paragraph breaks\n",
#     "        # weather = weather.replace('\\n', \" \")\n",
#     "        return mars_weather\n",
#     "\n",
#     "def mars_facts():\n",
#     "    \"\"\"Mars Facts\"\"\"\n",
#     "    url=\"https://space-facts.com/mars/)\"\n",
#     "    mars_table=pd.read_html(url)\n",
#     "    ctable=mars_table[0]\n",
#     "    final_table=ctable.rename(columns={0:'Description',1: \"value\"})\n",
#     "    return final_table.to_html(header=True, index=True)\n",
#     "\n",
#     "def scrape_hemi(browser):\n",
#     "    \"\"\"Collect Hemispheres\"\"\"\n",
#     "    hems=['Cerberus Hemisphere','Schiaparelli Hemisphere Enhanced','Syrtis Major Hemisphere Enhanced','Valles Marineris Hemisphere Enhanced']\n",
#     "    hems_url=[]\n",
#     "\n",
#     "    for info in hems: \n",
#     "        home_url=\"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
#     "        browser.visit(home_url)\n",
#     "        browser.is_element_present_by_text(info, wait_time=1)\n",
#     "        more_info_elem = browser.find_link_by_partial_text(info)\n",
#     "        more_info_elem.click()\n",
#     "        full_image_elem = browser.find_by_id('wide-image-toggle')\n",
#     "        full_image_elem.click()\n",
#     "        soup=bs(browser.html, 'html.parser')\n",
#     "        photo1=soup.body.find('img', class_='wide-image')\n",
#     "        photo_src=photo1['src']\n",
#     "        photo_url1=f\"https://astrogeology.usgs.gov{photo_src}\"\n",
#     "        hems_url.append(photo_url1)  \n",
#     "        return(photo_url1)\n",
#     "\n",
#     "    hemisphere_image_urls = [\n",
#     "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": hems_url[0]},\n",
#     "    {\"title\": \"Cerberus Hemisphere\", \"img_url\":hems_url[1]},\n",
#     "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": hems_url[2]},\n",
#     "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": hems_url[3]},]\n",
#     "    return hemisphere_image_urls\n",
#     "\n",
#     "if __name__ == \"__main__\":\n",
#     "    print(scrape_all())\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.7.6"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 4
# }
