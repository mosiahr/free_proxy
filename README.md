#**Free Proxy List**

Scraping free proxy list and use sqlalchemy to save it to database.

You can get a proxy list just by writing:
    ```
    FreeProxyScraper(URL).scraping()
    ```

You'll get: ```[{'ip_address': '47.74.84.13', 'port': 443, 'code': 'AU', 'country': 'Australia', 'anonymity': 'anonymous', 'google': 'no', 'https': 'no', 'last_checked': '9 seconds ago'}, {'ip_address': '174.137.49.135', 'port': 3128, 'code': 'US', 'country': 'United States', 'anonymity': 'anonymous', 'google': 'no', 'https': 'no', 'last_checked': '9 seconds ago'}, {'ip_address': '77.34.60.182', 'port': 8080, 'code': 'RU', 'country': 'Russian Federation', 'anonymity': 'anonymous', 'google': 'no', 'https': 'no', 'last_checked': '9 seconds ago'}, ...```

To **save list to the database**, you need to use an instance DB. He needs to give the scheme, user, password, host, db_name, limit, echo.
    
    The string form of the URL is
    ``dialect[+driver]://user:password@host/dbname[?key=value..]``, where
    ``dialect`` is a database name such as ``mysql``, ``oracle``,
    ``postgresql``, etc., and ``driver`` the name of a DBAPI, such as
    ``psycopg2``, ``pyodbc``, ``cx_oracle``, etc.  Alternatively,
    the URL can be an instance of :class:`~sqlalchemy.engine.url.URL`.
    
    limit: Parameter that sets the maximum number of rows in the table
    
    echo=False: if True, the Engine will log all statements
        as well as a ``repr()`` of their parameter lists to the default log
        handler, which defaults to ``sys.stdout`` for output.   If set to the
        string ``"debug"``, result rows will be printed to the standard output
        as well. The ``echo`` attribute of ``Engine`` can be modified at any
        time to turn logging on and off; direct control of logging is also
        available using the standard Python ``logging`` module. 
