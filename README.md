# Free Proxy List

Scraping free proxy list and use SQLAlchemy to save it to database.

## Getting Started
1. Clone this repo with command:  
     `git clone git@github.com:mosiahr/free_proxy.git`  
     `cd free_proxy/`
2. Create a virtual environment (either `pipenv`, `virtualenv` or `venv`)
3. Install requirements (either with `pipenv` or `pip install -r requirements.txt`)
4. Run the command to get help:  
    `python3 main.py --help`
    
## Save proxies to CSV file
Run command: `python3 main.py --file csv`  
or with short option: `python3 main.py -f csv`

## Save proxies to SQLite database
Run command: `python3 main.py --database sqlite`  
or with short option `python3 main.py -db sqlite`
 
## Save proxies to MySQL database
1. Before run program you need to set variables 
`SCHEMA_MYSQL, USER_MYSQL, PASS_MYSQL, HOST_MYSQL, DB_NAME_MYSQL` in `settings.py`  

2. Run command: `python3 main.py --database mysql`  
    or with short option `python3 main.py -db mysql`

## How to use proxies in your program?
You can get a proxy list just by writing:  
`scraper = FreeProxyScraper()`   
`proxies = scraper.scraping()`

## Use echo
That see logs use argument: `--echo yes`  
For example:  
  `python3 main.py -db sqlite --echo yes`
