import unittest
import main
class TestResult(unittest.TestCase):
    
    def test_res(self):
        self.assertEqual(main.hello(), "Hello, Jenkins")
        
        
if __name__ == "__main__":
    unittest.main()
