'''
The following python script downloads data from a set of webpages.
This is a classic example of downloading webpages and the standard for introducing concurrency.
'''

import requests
import time

def download_site(url):
    with requests.get(url) as response:
        return len(response.content)

def download_all_sites(urls):
    for url in urls:
        print("For URL: ", url, download_site(url))
        
    
if __name__ == "__main__":
    start_time = time.time()

    links = ["https://twitter.com","https://facebook.com", "https://www.linkedin.com"] * 10
    download_all_sites(links)
    
    end_time = time.time()
    print("Time taken: ", end_time - start_time, "Seconds")
