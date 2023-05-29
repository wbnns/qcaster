import unittest
from app import app, db, Tweet

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_post_to_farcaster(self):
        with app.app_context():
            # Add a test tweet to the database
            tweet = Tweet(text="Test tweet")
            db.session.add(tweet)
            db.session.commit()

            # Make a POST request to the '/post_farcaster' route
            response = self.app.post('/post_farcaster')

            # Assert that the response status code is 200 (successful)
            self.assertEqual(response.status_code, 200)

            # Assert that the Farcaster post response status is 200 (successful)
            self.assertEqual(response.json['farcaster_status'], 200)

    def test_post_to_twitter(self):
        with app.app_context():
            # Add a test tweet to the database
            tweet = Tweet(text="Test tweet")
            db.session.add(tweet)
            db.session.commit()

            # Make a POST request to the '/post_twitter' route
            response = self.app.post('/post_twitter')

            # Assert that the response status code is 200 (successful)
            self.assertEqual(response.status_code, 200)

            # Assert that the Twitter post response status is 200 (successful)
            self.assertEqual(response.json['twitter_status'], 200)

if __name__ == '__main__':
    unittest.main()

