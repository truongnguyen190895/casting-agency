import os
from flask import Flask, jsonify, request
from models import setup_db, Actor, Movie
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, PATCH"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        return response

    @app.route("/")
    def get_greeting():
        greeting = "Hello !!!!! You are doing great in this Udacity project."

        return greeting

    @app.route("/actors", methods=["GET"])
    def get_actors():
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]
        return jsonify(
            {
                "success": True,
                "actors": formatted_actors,
            }
        )

    @app.route("/movies", methods=["GET"])
    def get_movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]
        return jsonify(
            {
                "success": True,
                "movies": formatted_movies,
            }
        )

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Actor not found",
                    }
                ),
                404,
            )

        actor.delete()
        return jsonify(
            {
                "success": True,
                "deleted_actor_id": actor.id,
            }
        )

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Movie not found",
                    }
                ),
                404,
            )

        movie.delete()
        return jsonify(
            {
                "success": True,
                "deleted_movie_id": movie.id,
            }
        )

    @app.route("/actors", methods=["POST"])
    def create_actor():
        data = request.get_json()

        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")

        if not name or not age or not gender:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Please provide valid name, age, and gender for the actor.",
                    }
                ),
                400,
            )

        actor = Actor(name=name, age=age, gender=gender)
        actor.insert()

        return jsonify(
            {
                "success": True,
                "created_actor_id": actor.id,
            }
        )

    @app.route("/movies", methods=["POST"])
    def create_movie():
        data = request.get_json()

        title = data.get("title")
        release_date = data.get("release_date")

        if not title or not release_date:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Please provide a valid title and release date for the movie.",
                    }
                ),
                400,
            )

        movie = Movie(title=title, release_date=release_date)
        movie.insert()

        return jsonify(
            {
                "success": True,
                "created_movie_id": movie.id,
            }
        )

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    def update_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Actor not found",
                    }
                ),
                404,
            )

        data = request.get_json()

        if "name" in data:
            actor.name = data["name"]

        if "age" in data:
            actor.age = data["age"]

        if "gender" in data:
            actor.gender = data["gender"]

        actor.update()

        return jsonify(
            {
                "success": True,
                "updated_actor_id": actor.id,
            }
        )

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    def update_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": "Movie not found",
                    }
                ),
                404,
            )

        data = request.get_json()

        if "title" in data:
            movie.title = data["title"]

        if "release_date" in data:
            movie.release_date = data["release_date"]

        movie.update()

        return jsonify(
            {
                "success": True,
                "updated_movie_id": movie.id,
            }
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
