import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data.decode("utf-8")

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        expected_result = '{"imie": "Grazyna", "msg": "Hello World!"}'
        self.assertEqual(expected_result, rv.data.decode("utf-8"))

    def test_name(self):
        rv = self.app.get('/?name=apolonia&output=json')
        expected_result = '{"imie": "apolonia", "msg": "Hello World!"}'
        self.assertEqual(expected_result, rv.data.decode("utf-8"))
