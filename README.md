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
  "movies": [
    {
      "age": 48,
      "gender": "female",
      "id": 1,
      "name": "Angelina Jolie"
    },
  ],
  "success": true,
  "total": 1
}
```

#### POST /actors

- General:
  - Creates a new actor using the submitted name, age and gender. Returns the id of the created actor, success value.
- `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{"name":"Angelina Jolie", "age":48, "gender":"female"}'`

```
{
  "success": true,
  "created_actor_id": 1,
}
```

#### DELETE /actors/{actor_id}

- General:
  - Deletes the actor of the given ID if exists. Returns the id of the deleted actor and success value.
- `curl -X DELETE http://127.0.0.1:5000/actors/1`

```
{
  "success": true,
  "deleted_actor_id": 1,
}
```

#### PATCH /actors/{actor_id}

- General:
  - Updates the information of the specified actor. Returns the success value and id of the modified actor.
- `curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"name":"Maria"}'`

```
{
  "updated_actor_id": 1,
  "success": true
}
```

#### GET /movies

- General:
  - Returns a list of movie objects, success value, and total number of movies
- Sample: `curl http://127.0.0.1:5000/movies`

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "2023-11-04",
      "title": "Avengers"
    },
  ],
  "success": true,
  "total_books": 1
}
```

#### POST /movies

- General:
  - Creates a new movie using the submitted title, and release date. Returns the id of the created movie, success value.
- `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json" -d '{"title":"Angelina Jolie", "release_date":"2023-11-11"}'`

```
{
  "success": true,
  "created_movie_id": 1,
}
```

#### DELETE /movies/{movie_id}

- General:
  - Deletes the movie of the given ID if exists. Returns the id of the deleted movie and success value.
- `curl -X DELETE http://127.0.0.1:5000/movies/1`

```
{
  "success": true,
  "deleted_movie_id": 1,
}
```

#### PATCH /movies/{movie_id}

- General:
  - Updates the information of the specified movie. Returns the success value and id of the modified movie.
- `curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"title":"Maria"}'`

```
{
  "updated_movie_id": 1,
  "success": true
}
```

## Deployment N/A

## Authors

Yours truly, Truong Nguyen from FPT Software
