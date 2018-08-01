from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            # check to make sure the item doesn't already exist
            self.assertIsNone(ItemModel.find_by_name('test'))
            # save the item to the database
            item.save_to_db()
            # verify that the item exists
            self.assertIsNotNone(ItemModel.find_by_name('test'))
    def test_json(self):
        item = ItemModel('test', 19.99)
        expected = {'name':'test', 'price':19.99}
        self.assertEqual(item.json(), expected)

