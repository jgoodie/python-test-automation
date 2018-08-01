from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest

import json

class StoreTest(BaseTest):

    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/test')
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name':'test', 'items':[]},json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                response = client.post('/store/test')
                self.assertEqual(response.status_code, 400)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'message': "A store with name 'test' already exists."},
                                     json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                response = client.delete('/store/test')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},json.loads(response.data))
                self.assertIsNone(StoreModel.find_by_name('test'))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                response = client.get('/store/test')
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name':'test', 'items':[]}, json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/store/test')
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data ))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                ItemModel('test', 19.99, 1).save_to_db()
                resp = client.get('/store/test')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'name':'test','items':[{'name':'test', 'price':19.99}]},
                                     json.loads(resp.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                resp = client.get('/stores')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'stores':[{'name':'test', 'items':[]}]},
                                    json.loads(resp.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/test')
                ItemModel('test', 19.99, 1).save_to_db()
                resp = client.get('/stores')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'stores':[{'name':'test', 'items':[{'name':'test', 'price':19.99}]}]},
                                    json.loads(resp.data))