import pytest
from pyspark.sql import DataFrame, SparkSession
from sum_values_function import sum_values

class TestSumValues:
    @pytest.fixture(scope="class")
    def spark(self) -> SparkSession:
     return SparkSession.builder.appName("TestSumValues").getOrCreate()

    @pytest.fixture(scope="class")
    def sample_df(self, spark: SparkSession) -> DataFrame:
        data = [(3,), (7,), (10,)]
        return spark.createDataFrame(data, ["value"])
    
    def test_sum_values(self, sample_df: DataFrame) -> None:
        try:
            result = sum_values(sample_df, column="value")
            assert result == 20
        except TypeError as e:
            pytest.fail(f"TypeError occurred: {e}")
        except Exception as e:
            pytest.fail(f"Unexpected exception occurred: {e}")
