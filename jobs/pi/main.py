from operator import add
from jobs.pi.helper import trial
from jobs.pi.config import settings

def perform(spark, args):
    execution_day = args['date']
    sample_size = settings.sample_size
    partitions = settings.partitions
    print(f'Running Pi estimation for {execution_day} with sample_size: {sample_size}, partitions: {partitions}')
    count = spark.sparkContext.parallelize(range(sample_size)).map(trial).reduce(add)
    print('Pi is roughly %f' % (4.0 * count / sample_size))