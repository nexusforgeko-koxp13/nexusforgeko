import tempfile
import unittest
from pathlib import Path
from route_efficiency import summarize

HEADER = "session,total_minutes,travel_minutes,npc_minutes,bank_minutes,repair_minutes,other_minutes\n"


class RouteEfficiencyTest(unittest.TestCase):
    def read(self, rows, header=HEADER):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.csv"
            path.write_text(header + rows, encoding="utf-8-sig")
            return summarize(path)

    def test_duration_weighted_result_and_fractional_minutes(self):
        result = self.read("A,60,6,3,2,1,3\nB,30,2.5,1,1,0.5,0\n")
        self.assertEqual(result["sessions"], 2)
        self.assertEqual(result["remaining_minutes"], 70)
        self.assertEqual(result["remaining_percent"], 77.78)

    def test_invalid_data_is_rejected_instead_of_fabricating_a_result(self):
        for row in ["", "A,60,50,20,0,0,0\n", "A,0,0,0,0,0,0\n",
                    "A,60,-1,0,0,0,0\n", "A,60,NaN,0,0,0,0\n",
                    "A,60,Infinity,0,0,0,0\n", "A,60,,0,0,0,0\n",
                    "A,60,1,5,0,0,0,0\n"]:
            with self.subTest(row=row), self.assertRaises(ValueError):
                self.read(row)
        with self.assertRaises(ValueError):
            self.read("A,60\n", "session,total_minutes\n")


if __name__ == "__main__":
    unittest.main()
