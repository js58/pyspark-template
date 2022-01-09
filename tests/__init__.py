import unittest

try:
    import pyspark
except:
    import findspark
    findspark.init()
    import pyspark


class PySparkTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = pyspark.sql.SparkSession\
                    .builder\
                    .master("local[*]")\
                    .appName('testing')\
                    .getOrCreate()