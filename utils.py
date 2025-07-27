import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Loaded data with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def row_to_text(row: pd.Series) -> str:
    return (
        f"Applicant ID: {row['Loan_ID']}. "
        f"Gender: {row['Gender']}, Married: {row['Married']}, Dependents: {row['Dependents']}. "
        f"Education: {row['Education']}, Self-Employed: {row['Self_Employed']}. "
        f"Applicant Income: {row['ApplicantIncome']}, Co-applicant Income: {row['CoapplicantIncome']}, "
        f"Loan Amount: {row['LoanAmount']}, Loan Term: {row['Loan_Amount_Term']}. "
        f"Credit History: {row['Credit_History']}, Property Area: {row['Property_Area']}. "
        f"Loan Status: {row.get('Loan_Status', 'Unknown')}."
    )

def dataframe_to_docs(df: pd.DataFrame) -> list:
    return [row_to_text(row) for _, row in df.iterrows()]

def is_meaningful_text(text):
    import enchant
    d = enchant.Dict("en_US")
    words = text.strip().split()
    meaningful_words = sum(1 for word in words if d.check(word))
    return meaningful_words >= len(words) / 2