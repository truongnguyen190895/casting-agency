# Casting Agency

This project models a company that is responsible for creating movies and managing and assigning actors to those movies

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

## Getting Started

### Pre-requisites and Local Development

Developers using this project should already have Python3, pip and node installed on their local machines.

#### Virtual Environments

Installing virtualenv

For Unix/MacOS, run the following command:

```
python3 -m pip install --user virtualenv
```

For Windows:

```
py -m pip install --user virtualenv
```

Creating a virtual environment

To create a virtual environment, go to your project’s directory and run venv.

For Unix/MacOS, run the following command:

```
python3 -m venv env
```

For Windows:

```
py -m venv env
```

Activate a virtual environment, from the root directory, run:

For Unix/MacOS, run the following command:

```
source env/bin/activate
```

For Windows:

```
.\env\Scripts\activate
```

#### Backend

From the root directory run `pip install requirements.txt`. All required packages are included in the requirements file.

To run the application run the following commands:

```
python app.py
```

These commands put the application in development mode. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.

The application is run on `http://127.0.0.1:5000/` by default.

### Tests

In order to run tests:

```
python test.py
```

All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Unprocessable Content
- 405: Method Not Allowed

### Endpoints

#### GET /actors

- General:
  - Returns a list of actor objects, success value, and total number of actors
- Sample: `curl http://127.0.0.1:5000/actors`

```{
  "books": [
    {
      "age": 48,
      "gender": "female",
      "id": 1,
      "name": "Angelina Jolie"
    },
  ],
"success": true,
"total_books": 1
}
```

#### POST /books

- General:
  - Creates a new book using the submitted title, author and rating. Returns the id of the created book, success value, total books, and book list based on current page number to update the frontend.
- `curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'`

```
{
  "books": [
    {
      "author": "Neil Gaiman",
      "id": 24,
      "rating": 5,
      "title": "Neverwhere"
    }
  ],
  "created": 24,
  "success": true,
  "total_books": 17
}
```

#### DELETE /books/{book_id}

- General:
  - Deletes the book of the given ID if it exists. Returns the id of the deleted book, success value, total books, and book list based on current page number to update the frontend.
- `curl -X DELETE http://127.0.0.1:5000/books/16?page=2`

```
{
  "books": [
    {
      "author": "Gina Apostol",
      "id": 9,
      "rating": 5,
      "title": "Insurrecto: A Novel"
    },
    {
      "author": "Tayari Jones",
      "id": 10,
      "rating": 5,
      "title": "An American Marriage"
    },
    {
      "author": "Jordan B. Peterson",
      "id": 11,
      "rating": 5,
      "title": "12 Rules for Life: An Antidote to Chaos"
    },
    {
      "author": "Kiese Laymon",
      "id": 12,
      "rating": 1,
      "title": "Heavy: An American Memoir"
    },
    {
      "author": "Emily Giffin",
      "id": 13,
      "rating": 4,
      "title": "All We Ever Wanted"
    },
    {
      "author": "Jose Andres",
      "id": 14,
      "rating": 4,
      "title": "We Fed an Island"
    },
    {
      "author": "Rachel Kushner",
      "id": 15,
      "rating": 1,
      "title": "The Mars Room"
    }
  ],
  "deleted": 16,
  "success": true,
  "total_books": 15
}
```

#### PATCH /books/{book_id}

- General:
  - If provided, updates the rating of the specified book. Returns the success value and id of the modified book.
- `curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'`

```
{
  "id": 15,
  "success": true
}
```

## Deployment N/A

## Authors

Yours truly, Coach Caryn

## Acknowledgements

The awesome team at Udacity and all of the students, soon to be full stack extraordinaires!
