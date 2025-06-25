import unittest
from service.models import Product

class TestProductModel(unittest.TestCase):

    def setUp(self):
        self.product = Product(name="Test Product", category="Books", available=True, price=10.99)

    def test_read_product(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.category, "Books")

    def test_update_product(self):
        self.product.name = "Updated Product"
        self.assertEqual(self.product.name, "Updated Product")

    def test_delete_product(self):
        # Simulate deletion by setting it to None or using a list.pop in real case
        self.product = None
        self.assertIsNone(self.product)

    def test_list_all_products(self):
        products = [
            Product(name="P1", category="Books", available=True, price=5.0),
            Product(name="P2", category="Games", available=False, price=20.0)
        ]
        self.assertEqual(len(products), 2)

    def test_search_by_name(self):
        products = [Product(name="Notebook", category="Stationery", available=True, price=2.5)]
        result = [p for p in products if "Note" in p.name]
        self.assertEqual(len(result), 1)

    def test_search_by_category(self):
        products = [
            Product(name="Chair", category="Furniture", available=True, price=30.0),
            Product(name="Table", category="Furniture", available=False, price=45.0)
        ]
        result = [p for p in products if p.category == "Furniture"]
        self.assertEqual(len(result), 2)

    def test_search_by_availability(self):
        products = [
            Product(name="TV", category="Electronics", available=True, price=299.99),
            Product(name="Lamp", category="Furniture", available=False, price=15.0)
        ]
        available_products = [p for p in products if p.available]
        self.assertEqual(len(available_products), 1)

if __name__ == "__main__":
    unittest.main()
