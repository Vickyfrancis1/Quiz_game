import unittest

def best_score(filename):
    best = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                result = line.strip().split("| ")[1]
                got = int(result.split("/")[0])
                if got > best:
                    best = got
    except FileNotFoundError:
        return 0
    return best

class TestBestScore(unittest.TestCase):
    
    def test_missing_file(self):
        self.assertEqual(best_score("no_such_file.txt"), 0)
        
    def test_finds_highest(self):
        with open("temp_scores.txt", "w") as file:
            file.write("2026-10-15 11:30 | 2/5\n")
            file.write("2026-10-15 11:34 | 4/5\n")
            file.write("2026-10-15 11:40 | 3/5\n")
        self.assertEqual(best_score("temp_scores.txt"), 4)
        
unittest.main(exit=False)   