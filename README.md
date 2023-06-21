
# About The Project
A dictionary api for performing CRUD operations and Search specific words .

# Setup Instructions

1 . Clone the repository ```git clone https://github.com/Sahal-Rasheed/dictionary_api.git```

2 . Navigate to the working directory

3 . Open the project from the code editor

4 . Create virtual environment ```python -m venv env```

5 . Activate the virtual environment ```source env/Scripts/activate```

6 . Install the required packages to run the project ```pip install -r requirements.txt```

7 . Run the server ```python manage.py runserver```

# Features 
1 . User should be able to add record to the dictionary.

API - ```http://127.0.0.1:8000/dictionary/``` , ```METHOD - POST```

2.1 User should be able to search a word in the dictionary (partial words should also function, expecting get call with query param for label search)

API - ```http://127.0.0.1:8000/dictionary/?search='query'``` , ```METHOD - GET```

2.2 User should be able to view list of all words in the dictionary.

API - ```http://127.0.0.1:8000/dictionary/``` , ```METHOD - GET```

'Implemented both features ```searching``` and ```listing``` all words in a single method ```list```, so we can use single API for this, based on the value in query param the desired functionality will work. i.e if there is no query param then all words will be listed otherwise the word in the query param will be displayed'

3 . User should be able to update a particular record based on id provided in route.

API - ```http://127.0.0.1:8000/dictionary/id/``` , ```METHOD - PUT```

4 . User should be able to remove a particular record based on id provided in route.

API - ```http://127.0.0.1:8000/dictionary/id/``` , ```METHOD - DELETE```



    