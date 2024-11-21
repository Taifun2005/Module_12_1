import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = runner.Runner('Runner1')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = runner.Runner('Runner2')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = runner.Runner('Runner1')
        runner2 = runner.Runner('Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertEqual(runner1.distance != runner2.distance)

if __name__ == '__main__':
    unittest.main



