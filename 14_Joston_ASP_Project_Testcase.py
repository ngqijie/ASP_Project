import unittest
import result as prog

class TestMyProgram(unittest.TestCase):

    def test_total(self):
        data = [12946711, 11363486, 7085418,  5469237, 1180258, 1402976, 1051425, 922636, 180249, 88012, 34626,  24763, 13402, 4029 ]
        result = prog.AspProject.total(data)
        self.assertEqual(result, 34681804)

    def test_mean(self):
        data = [12946711, 11363486, 7085418,  5469237, 1180258, 1402976, 1051425, 922636, 180249, 88012, 34626,  24763, 13402, 4029 ]
        result = prog.AspProject.mean(data)
        self.assertEqual(result,)

