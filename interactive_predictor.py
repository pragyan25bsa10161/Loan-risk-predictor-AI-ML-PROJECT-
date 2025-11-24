import csv

# --- 1. Rule-Based Prediction Function (Model Replacement) ---

def predict_loan_status(income, loan_amount, credit_score):
    """
    Simple Rule-Based Predictor for Loan Default.
    This replaces the complex Machine Learning model.
    """
    
    # Rule 1: High Loan Amount relative to Income (Risk Ratio)
    # If loan is more than 1.8 times the income OR loan is very high (>= 200)
    risk_ratio = loan_amount / income if income > 0 else float('inf')
    if risk_ratio > 1.8 or loan_amount >= 200:
        return 1, "High Loan vs. Income" # 1 means Default Risk

    # Rule 2: Very Low Credit Score and Low Income
    # If credit score is low (<= 5) AND income is low (<= 60)
    if credit_score <= 5 and income <= 60:
        return 1, "Low Score and Low Income" # 1 means Default Risk
        
    # Rule 3: Very High Credit Score (Low Risk)
    if credit_score >= 8 and risk_ratio < 1.5:
        return 0, "High Credit Score" # 0 means Safe

    # Default to Safe if no strong risk rules are triggered
    return 0, "Moderate Profile"

# --- 2. Data Loading (Checking the file) ---

def get_user_input():
    """Prompts the user for the three features and ensures input is valid."""
    print("--- New Loan Applicant Assessment (Simple Rule-Based) ---")
    
    while True:
        try:
            # Gather user inputs
            income = float(input("Enter Annual Income (in thousands, e.g., 75 for $75,000): "))
            loan_amount = float(input("Enter Loan Amount Requested (in thousands, e.g., 150 for $150,000): "))
            credit_score = float(input("Enter Simplified Credit Score (e.g., 1 to 10): "))
            
            # Basic validation
            if income <= 0 or loan_amount <= 0 or credit_score < 1 or credit_score > 10:
                print("Error: Input values must be positive and Credit Score must be 1-10. Please try again.")
                continue

            # Return the validated inputs
            return income, loan_amount, credit_score
        except ValueError:
            print("Invalid input. Please enter numerical values only.")

# --- 3. Run the Program and Display Results ---

# Get the user's data
income, loan_amount, credit_score = get_user_input()

# Make the prediction using the simple rule-based system
default_status, reason = predict_loan_status(income, loan_amount, credit_score)

print("\n-------------------------------------------")
print(f"APPLICANT DATA: Income={income}K, Loan={loan_amount}K, Score={credit_score}")

if default_status == 1:
    print("RESULT: 🚨 HIGH RISK - Predicted to DEFAULT")
    print(f"REASON: {reason}")
else:
    print("RESULT: ✅ LOW RISK - Predicted NOT to Default")
    print(f"REASON: {reason}")
    
print("-------------------------------------------")

# Optional: Load and display the training data (just to show file reading)
def load_and_display_data(file_path):
    print("\n--- Training Data Snapshot (From CSV) ---")
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            print(f"Columns: {', '.join(header)}")
            for i, row in enumerate(csv_reader):
                if i < 3: # Display only first 3 rows
                    print(row)
                elif i == 3:
                    print("...")
            print(f"Total rows read: {i + 1}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

load_and_display_data('loan_data_simple.csv')
