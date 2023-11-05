import unittest
from app import create_app
from models import setup_db
from flask_sqlalchemy import SQLAlchemy
import unittest
import json
from settings import DATABASE_URL_TEST

class TestApp(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = DATABASE_URL_TEST
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.executive_producer_jwt_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZBSW9wNGlacVdRS2hJblRYRzdoSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMWN6YmMxMXJ2ZnhtaXA4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODQyNTQ3Njk0MjI3MDg3MTA5MiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2OTkxMDk5NTAsImV4cCI6MTY5OTE5NjM1MCwiYXpwIjoib3dwTWt1NUcxa09ta1M5blN0NlBwblRYbGdEODRUTDEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.kF8ZggLRdObEJZIggS3Sd3P9hsomibB_a2QfI3EfXB8U2i1EQgjF6a8Mhc2HsvfEMgmK1HfVMW1mzPLGTb62G6lverBg5qxdU3eUMH03fF-SUKUzg8r0eSsSifb3kJiyjgNdysEHOnc0xvMucrVZrEar3KafQG38Zmpjw8XEFPk3I2PIqhBCVwM3re3myxIbOD9D0dAOlK7r9mU-_kBi9KgH9NwSpdkkY42sm760VMmYvQCebOFFojUdSOTHZEsX157atoSiwiFeZJkYlC4TRQPfnzh2DEJCTO5HoSjQWd2ldCWpQF6L-RSPSodstbpAiEt6FBenxqRN-XWd44sLdg"
        self.casting_director_jwt_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZBSW9wNGlacVdRS2hJblRYRzdoSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMWN6YmMxMXJ2ZnhtaXA4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODQyNTQ3Njk0MjI3MDg3MTA5MiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2OTkxMTAxMDgsImV4cCI6MTY5OTE5NjUwOCwiYXpwIjoib3dwTWt1NUcxa09ta1M5blN0NlBwblRYbGdEODRUTDEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.ux0AZ1wQNaqZcehcKxmdywCX8599tpxjn9fShGBRh6ijLVkcqPueaKLGs7_d0IcfEjpiHY1-MCcMA8TlEYXAdhyNukHqAz-53PqZmMbQ_a6uk3YwTxVpViJe7tPRQwxNtykWO5thf2pDVFQCSL5XRT5gh_AnC43bvHfDnaoWwaA9-ETYHYIA_ISvFe0AM9fhsEfPPuZuMn1TKGkcLt7-f7pyw2dktJJ5x5XWxKqvCrhyqiFrBVbUw3vb4D49uAeNS4EjWOiE0dY9waE0jlE9GjOK--K0TvuAYV5cKK0LPwIVK_WhkJjEKXymBsA5BKJkG0l4XGXHptmILjNlSLmmwA"
        self.casting_assistant_jwt_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlZBSW9wNGlacVdRS2hJblRYRzdoSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMWN6YmMxMXJ2ZnhtaXA4LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwODQyNTQ3Njk0MjI3MDg3MTA5MiIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2OTkxMTAyMjMsImV4cCI6MTY5OTE5NjYyMywiYXpwIjoib3dwTWt1NUcxa09ta1M5blN0NlBwblRYbGdEODRUTDEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.N6etb7dMe2qOfEk37jOlpzCf4nQ8oUFeh5qFeX54AZjooKPTr4X6nNBCEdCFfKjrnV8a3qi_9VMpFHTpLNt4V--Em_TTUagU3d_e-P06BHTi0QHDHD8rKJ5r_BMzkiBewsmOR1usEnwMXrhoawfCw5wDrF_yRo38EVGZb6eFRJILUxqWzFHXQNgFn6ReDx7SsCB8suMM9nxYkTLOIqS6nG80ggFnmc1f8D8Lnb2KBK5QWk5IWNtJngThl1SGoy3RTDJwTqJ6TO-Q6qvCkitaYaCktnKDdIiTGJK7puDqHVefwowgrMDK6F_U9Ca4rd1THnuRw2IzTkMR1FTgOUpYrA"

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors_success(self):
        response = self.client().get(
            "/actors", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["actors"])

    def test_get_actors_fail(self):
        response = self.client().get("/actors")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertTrue(data["error"])

    def test_get_movies_success(self):
        response = self.client().get(
            "/movies", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["movies"])

    def test_get_movies_fail(self):
        response = self.client().get("/movies")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertTrue(data["error"])

    def test_delete_actors_fail(self):
        response = self.client().delete(
            "/actors/4000", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertTrue(data["error"])

    def test_delete_actors_success(self):
        response = self.client().delete(
            "/actors/2", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted_actor_id"], 2)

    def test_delete_movies_fail(self):
        response = self.client().delete(
            "/movies/4000", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertTrue(data["error"])

    def test_delete_movies_success(self):
        response = self.client().delete(
            "/movies/2", headers={"Authorization": self.executive_producer_jwt_token}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["deleted_movie_id"], 2)

    def test_post_actor_success(self):
        # Data for the new actor to be created
        new_actor_data = {"name": "John Doe", "age": 30, "gender": "Male"}

        # Send a POST request to the /actors endpoint with the new actor data and authorization header
        response = self.client().post(
            "/actors",
            json=new_actor_data,
            headers={"Authorization": self.executive_producer_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["created_actor_id"])

    def test_post_actor_fail(self):
        # Data for the new actor to be created
        new_actor_data = {"name": "John Doe", "gender": "Male"}

        # Send a POST request to the /actors endpoint with the new actor data and authorization header
        response = self.client().post(
            "/actors",
            json=new_actor_data,
            headers={"Authorization": self.executive_producer_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 400)
        self.assertTrue(data["error"])

    def test_post_movies_success(self):
        # Data for the new actor to be created
        new_movie_data = {"title": "New Movie", "release_date": "2023-01-01"}

        # Send a POST request to the /actors endpoint with the new actor data and authorization header
        response = self.client().post(
            "/movies",
            json=new_movie_data,
            headers={"Authorization": self.executive_producer_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["created_movie_id"])

    def test_post_movies_fail(self):
        # Data for the new actor to be created
        new_movie_data = {"title": "John Doe"}

        # Send a POST request to the /actors endpoint with the new actor data and authorization header
        response = self.client().post(
            "/movies",
            json=new_movie_data,
            headers={"Authorization": self.executive_producer_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 400)
        self.assertTrue(data["error"])

    def test_patch_actors_success(self):
        # Create a new actor (for testing purposes)
        new_actor_data = {"name": "John Doe updated"}
        response = self.client().patch(
            "/actors/5",
            json=new_actor_data,
            headers={"Authorization": self.casting_director_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["updated_actor_id"], 5)

    def test_patch_actors_fail(self):
        new_actor_data = {"name": "John Doe updated"}
        response = self.client().patch(
            "/actors/5",
            json=new_actor_data,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_patch_movies_success(self):
        # Create a new movie (for testing purposes)
        new_movie_data = {"title": "Peaky Blinders", "release_date": "2020-01-01"}
        response = self.client().patch(
            "/movies/1",
            json=new_movie_data,
            headers={"Authorization": self.casting_director_jwt_token},
        )

        data = json.loads(response.data)

        # Assert the response for the success scenario
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(data["updated_movie_id"], 1)

    def test_patch_movies_fail(self):
        new_movies_data = {"title": "John Doe updated"}
        response = self.client().patch(
            "/movies/1",
            json=new_movies_data,
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_casting_assistant_get_movies_success(self):
        response = self.client().get(
            "/movies",
            headers={"Authorization": self.casting_assistant_jwt_token},
        )
        data = json.load(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_casting_assistant_get_actors_success(self):
        response = self.client().get(
            "/actors",
            headers={"Authorization": self.casting_assistant_jwt_token},
        )
        data = json.load(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])


if __name__ == "__main__":
    unittest.main()
