def sum_values(df):
    return df.selectExpr("sum(value) as total").collect()[0]["total"]
