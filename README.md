# url-mapping-service

A simple project providing database structure and web interface allowing persistent creation of custom redirects (AKA url shortener):

```yoursite.example.com/<custom_string> -> https://othersite.example.com```

For example:

```yoursite.example.com/wiki -> https://www.wikipedia.org/```


Currently has a very basic web ui and lacks proper input verification, and thus is not recommended to host this site for the general public.

## External dependencies
This project uses the [flask framework](https://github.com/pallets/flask) with ```flask-login```, ```flask-sqlalchemy``` and ```flask_wtf``` extensions.

## Present features
- Simple web ui
    - no javascript
    - some inline css
- Redirects
    - creation
    - deletion (if tied to an account)
    - and also using them
- Optional account creation
    - ties redirects to your account and lets you delete them
    - session management isn't properly implemented yet

## Running
Just launch ```starty.py``` with a python3 interpreter. If not already present, you'll have to download aforementioned flask packages.
```
pip install flask flask_login flask_sqlalchemy flask_wtf
```

By default is hosted at `localhost:5000` or `127.0.0.1:5000`.
