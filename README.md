#### steem-username-autocomplete-api

This is a auto-complete backend for steem usernames. Almost all 3rd-party 
steem services asks users their account names. However, most of them
don't have any autocomplete.

For [steem.rocks](http://steem.rocks) I have needed this in the landing page where
users types their account names. This will be used in the frontend soon.

This app uses Flask to serve the API, redis to store usernames and auto-completion
functionality.

#### Installation

```
$ git clone https://github.com/emre/steem-username-autocomplete-api.git
$ cd steem-username-autocomplete-api
$ virtualenv -p python3.6 autocomplete-api-env
$ source autocomplete-api-env/bin/activate
$ pip install -r requirements.txt
```

#### Indexing the database

```
$ FLASK_APP=autocomplete_api/app.py flask initdb
```

**Note**: Indexing all steem usernames takes 10 minutes on my development setup.

### Serving the api

```
$ FLASK_APP=autocomplete_api/app.py flask run
```

### Try it live

[autocomplete.steem.rocks/?username=emr](http://autocomplete.steem.rocks/?username=emr)
