# Overview

**requests-loop** builds requests for Python's requests library and gets them in a loop to easily **scrape the data available in an API**

# Executive Summary

* Build list of requests using `requests.Request(...).prepare`
* Scrape an API
* Save the data of each endpoint into its own CSV
* Log info of each request: successful vs failed, datetime, etc.

# Prerequisites

1. Operating System\
   This code has only been tested on Ubuntu 20.04.1 LTS.
2. Infrastructure
   Python 3.8.0
3. Knowledge
   - requests
   - API

# Example

The example usage is set up to download a random Chuck Norris joke from each joke category available in the Chuck Norris Jokes API (see Resources below). Get the jokes with the following:
`python scrub_manager.py`

# Warning

This repo is for demonstration purposes only. Its only intended use is to demonstrate a robust framework for scraping an API. Please respect the individual terms and conditions of any API you interact with.

# Resources

* Chuck Norris Jokes API<br>
[https://api.chucknorris.io/](https://api.chucknorris.io/)
* Prepared Requests<br>
[https://requests.readthedocs.io/en/master/user/advanced/#prepared-requests](https://requests.readthedocs.io/en/master/user/advanced/#prepared-requests)