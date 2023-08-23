import unittest


class TestBesco(unittest.TestCase):
    """
    high level support for doing this and that.
    """
    def test_import(self):
        import besco

    def test_version(self):
        import besco
        print(besco.__version__)

    def test_classifcation(self):
        class_gt = 0
        class_pred = 0
        self.assertEqual(class_gt, class_pred, "Should be 0")


if __name__ == '__main__':
    unittest.main()
