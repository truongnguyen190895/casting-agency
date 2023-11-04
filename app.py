import os
from flask import Flask, jsonify, request
from models import setup_db, Actor, Movie
from flask_cors import CORS
from auth import requires_auth


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
    @requires_auth("get:actors")
    def get_actors():
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]
        return jsonify(
            {
                "success": True,
                "actors": formatted_actors,
                "total": len(formatted_actors)
            }
        )

    @app.route("/movies", methods=["GET"])
    @requires_auth("get:movies")
    def get_movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]
        return jsonify(
            {
                "success": True,
                "movies": formatted_movies,
                "total": len(formatted_movies)
            }
        )

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
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
    @requires_auth("delete:movies")
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
    @requires_auth("post:actors")
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
    @requires_auth("post:movies")
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
    @requires_auth("patch:actors")
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
    @requires_auth("patch:movies")
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

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "Resource Not Found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return (
            jsonify(
                {"success": False, "error": 422, "message": "Unprocessable Content"}
            ),
            422,
        )

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (
            jsonify({"success": False, "error": 405, "message": "Method Not Allowed"}),
            405,
        )

    @app.errorhandler(400)
    def method_not_allowed(error):
        return (
            jsonify({"success": False, "error": 400, "message": "Bad Request"}),
            400,
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
