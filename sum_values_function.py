from pyspark.sql import DataFrame

def sum_values(df: DataFrame, column: str) -> float:
    """Sum the values of a numeric column in the DataFrame."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    dtype = dict(df.dtypes)[column]
    if dtype not in ("int", "bigint", "double", "float", "decimal", "long", "short"):
        raise TypeError(f"Column '{column}' is not numeric (found type '{dtype}')")
    df.createOrReplaceTempView("_tmp_sum_values")
    # Use Spark SQL to compute the sum of the specified column from the temporary view
    result = df.sql_ctx.sql(f"SELECT SUM({column}) as total FROM _tmp_sum_values").collect()[0]["total"]
    return result
