# generator.py
import pandas as pd
import numpy as np
import re
import enchant

spell_checker = enchant.Dict("en_US")

def is_scribble_or_nonsense(text: str) -> bool:
    words = re.findall(r"\b\w+\b", text.lower())
    if not words:
        return True
    gibberish_ratio = sum(not spell_checker.check(w) for w in words) / len(words)
    return gibberish_ratio > 0.7

def generate_answer(query: str, df: pd.DataFrame) -> str:
    q = query.lower()

    try:
        # Loan amount average
        if "average loan amount" in q:
            avg = df["LoanAmount"].dropna().mean()
            return f"The average loan amount is approximately ₹{avg:.2f}K."

        # Loan term average
        elif "loan term" in q and "average" in q:
            avg_term = df["Loan_Amount_Term"].dropna().mean()
            return f"The average loan term is {avg_term:.0f} months."

        # Loan approval rate
        elif "approval rate" in q:
            approved = df[df["Loan_Status"] == "Y"]
            if "female" in q:
                approved = approved[df["Gender"] == "Female"]
                total = df[df["Gender"] == "Female"]
            elif "male" in q:
                approved = approved[df["Gender"] == "Male"]
                total = df[df["Gender"] == "Male"]
            else:
                total = df
            rate = len(approved) / len(total) * 100 if len(total) else 0
            return f"The loan approval rate is {rate:.2f}%."

        # Count of graduates
        elif "graduates" in q:
            count = len(df[df["Education"] == "Graduate"])
            return f"There are {count} graduate applicants in the dataset."

        # How many married/self-employed
        elif "how many" in q:
            if "married" in q:
                count = len(df[df["Married"] == "Yes"])
                return f"There are {count} married applicants."
            elif "self-employed" in q:
                count = len(df[df["Self_Employed"] == "Yes"])
                return f"There are {count} self-employed applicants."
            elif "male" in q:
                count = len(df[df["Gender"] == "Male"])
                return f"There are {count} male applicants."
            elif "female" in q:
                count = len(df[df["Gender"] == "Female"])
                return f"There are {count} female applicants."
            elif "credit history" in q:
                count = len(df[df["Credit_History"] == 1.0])
                return f"{count} applicants have a credit history."

        # Average income
        elif "average applicant income" in q:
            avg = df["ApplicantIncome"].dropna().mean()
            return f"The average applicant income is ₹{avg:.2f}."

        elif "average coapplicant income" in q:
            avg = df["CoapplicantIncome"].dropna().mean()
            return f"The average coapplicant income is ₹{avg:.2f}."

        # Approval rate by credit history
        elif "approval rate" in q and "credit history" in q:
            with_credit = df[df["Credit_History"] == 1.0]
            approved = with_credit[with_credit["Loan_Status"] == "Y"]
            rate = len(approved) / len(with_credit) * 100 if len(with_credit) else 0
            return f"The loan approval rate for applicants with credit history is {rate:.2f}%."

        # fallback
        return "That's a valid question, but I don’t have logic yet to answer it. Try asking about loan amounts, approvals, income, or applicants."

    except Exception as e:
        return "Sorry, I ran into a problem while processing your request."
