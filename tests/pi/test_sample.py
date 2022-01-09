from tests import PySparkTestCase
from jobs.pi.helper import trial

class TestSampleClass(PySparkTestCase):


    def test_pyspark_apis(self):
        """TestSampleClass.test_pyspark_apis: demo tests on pyspark apis should pass
        """
        df = self.spark.createDataFrame(data=[[1, 'a'], [2, 'b']], schema=['c1', 'c2'])
        self.assertEqual(df.count(), 2)

    def test_trial(self):
        """TestSampleClass.test_trial: the trial result should be either 0 or 1
        """
        result = trial(None)
        self.assertIn(result, [0, 1])