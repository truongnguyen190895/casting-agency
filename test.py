import unittest
from app import create_app
from models import setup_db, Movie, Actor
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

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_actor(self):
        response = self.app.post(
            "/actors", json={"name": "John Doe", "age": 30, "gender": "Male"}
        )
        self.assertEqual(response.status_code, 200)
        # Add assertions to verify the response

    # Add more test cases for other endpoints and scenarios


if __name__ == "__main__":
    unittest.main()
