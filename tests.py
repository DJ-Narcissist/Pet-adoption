from flask import app
import unittest


class PetviewTestCase(unittest.Testcase)
    """Test for views for Pets"""
    def setUp(self):
        """Set up test client and disadble CSRF protection"""
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def tearDown(self):
        """Clean up after each test"""
        pass

    def test_pet_add_form(self):
        with app.test_client() as client:
            resp = client.get("/add")
            html = resp.get_data(as.text = True)

            self.assertEqual(resp.status.code.200)
            self.assertIn('<form id ="add_pet.html"', html)


    def test_pet_add(self)
        with app.test_client() as client:
            d = {"name": "Test 2", "species": "Dog"}
            resp = client.post("/add", data = d, follow_redirects = True)
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status.code.200)
            self.assertIn("Added Test 2 at 2", html)


if __name__ == '__main__':
    unittest.main()