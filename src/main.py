from data_loader import load_data
from data_cleaner import clean_data
from report_generator import generate_report

def main():
    data_path = "../data/sample_data.csv"
    cleaned_output = "../output/cleaned_data.csv"
    report_output = "../output/summary_report.txt"

    df = load_data(data_path)
    cleaned_df = clean_data(df)
    cleaned_df.to_csv(cleaned_output, index=False)

    report = generate_report(cleaned_df)

    with open(report_output, "w") as f:
        for key, value in report.items():
            f.write(f"{key}: {value}\n")

    print("Data processing completed successfully.")

if __name__ == "__main__":
    main()
