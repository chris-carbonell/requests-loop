# requests
base_path = "https://api.chucknorris.io/jokes/random/" # end with /
timeout = 30

# set headers
dict_headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br'
    }

# scrubbing
str_filename_scrub_file = "./input/scrub_file.csv"
str_filename_output_root = "./output/"
str_filename_error_log = "./logs/error_log.txt"
str_filename_success_log = "./logs/success_requests.txt"