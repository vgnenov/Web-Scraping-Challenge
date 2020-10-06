{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import dependencies\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with windowsapi reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Boston\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3339: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "# Create an instance of Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use PyMongo to establish Mongo connection\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mars\")\n",
    "\n",
    "# create home route and define home function\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    # Find one record of data from the mongo database\n",
    "    mars_info = mongo.db.mars_collection.find_one()\n",
    "\n",
    "    # Return template and data\n",
    "    return render_template(\"index.html\", mars_data=mars_info)\n",
    "\n",
    "# create scrape route \n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    # run the scrape function\n",
    "    mars_data = scrape_mars.scrape()\n",
    "\n",
    "    # insert the mars data in to the collection\n",
    "    mongo.db.mars_collection.update({}, mars_data, upsert=True)\n",
    "\n",
    "    # go back to the home page\n",
    "    return redirect(\"/\")\n",
    "\n",
    "# run the app\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
