import pytest
from polygon import Polygon

class TestPolygon(pytest,TestCase):
    def test_polygon_initialization(self):
        polygon = Polygon("Triangle", [3, 3, 3])
        self.assertEqual(polygon.get_name(), "Triangle")
        self.assertEqual(polygon.get_sides(), [3, 3, 3])

    def test_get_name(self):
        polygon = Polygon("Square", [4, 4, 4, 4])
        self.assertEqual(polygon.get_name(), "Square")

    def test_set_name(self):
        polygon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])
        polygon.set_name("Pentagon")
        self.assertEqual(polygon.get_name(), "Pentagon")

    def test_get_sides(self):
        polygon = Polygon("Triangle", [3, 3, 3])
        self.assertEqual(polygon.get_sides(), [3, 3, 3])

    def test_set_sides(self):
        polygon = Polygon("Square", [4, 4, 4, 4])
        polygon.set_sides([5, 5, 5, 5])
        self.assertEqual(polygon.get_sides(), [5, 5, 5, 5])

if __name__ == '__main__':
    pytest.main()
