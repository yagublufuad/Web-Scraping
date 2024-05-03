# Web Scraping
## AmazonWebScraping
### Goal
The script `Amazon_web_scraper.py` demonstrates a simple example of Web Scraping using Amazon Website. With the link of an arbitrary item, we are tracking the price and writing to a `CSV` file.
The frequency of checking the price could be specified by the user.
### Usage
The script requires three arguments:
- URL of the desired item
-  user agent
-  path to the `CSV` file to write the tracked prices.

One can access the unique user agent using `https://httpbin.org/get`.

## Crypto Currency analysis
### Goal
This project showcases an example of web scraping utilizing the Python API of a website dedicated to real-time tracking of cryptocurrency fluctuations and its visualization.<br/>
### Usage
The script `automated_API_runner.py` enables retrieval of crypto currency fluctuation during a desired period of time with a given frequency. The dataset could be saved to a `CSV` file. <br/>
The script requires following arguments: URL to the webpage that lists fluctuations, the number of currencies to be retrieved, API key, path to the `CSV` file to write the fluctuations, the number of iterations and the frequency of retrievals.<br/>
The Jupyter notebook `Analyze Crypto Currencies.ipynb` shows several methods to read, pre-process and visualize the data saved in `CSV` file. <br/>
An example dataset is also included in the folder as `Coinmarket_15Currencies_12hr_30Apr.csv`. It is retrieved by tracking fluctuations of 15 currencies for 12 hours with a 30 minutes frequency. <br/>

More about the website, its API, and the generation of API key can be found [here](https://coinmarketcap.com/api/documentation/v1/#).

#### Example call of the script from command line
```python automated_API_runner.py --url "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" --limit 15 --api_key "" --csv_file "path_to_csv.csv" --num_iterations 4 --sleep_duration_minutes 0.05```


