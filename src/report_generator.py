def generate_report(df):
    return {
        "Total Records": len(df),
        "Average Age": round(df["age"].mean(), 2),
        "Average Salary": round(df["salary"].mean(), 2),
        "Department Count": df["department"].value_counts().to_dict()
    }
