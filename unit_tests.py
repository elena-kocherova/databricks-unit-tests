import pytest
from pyspark.sql import SparkSession

class TestSumValues:
    @pytest.fixture(scope="class")
    def spark(self):
        return SparkSession.builder.appName("TestSumValues").getOrCreate()

    @pytest.fixture(scope="class")
    def sample_df(self, spark):
        data = [(3,), (7,), (10,)]
        return spark.createDataFrame(data, ["value"])

    def test_sum_values(self, sample_df):
        result = sum_values(sample_df)
        assert result == 20

