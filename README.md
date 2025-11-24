💰 Rule-Based Loan Risk Predictor

🌟 Project Overview

This project is a lightweight, command-line application developed in Python to assess the potential risk of a loan applicant defaulting. It is designed as an academic demonstration of a Rule-Based Expert System (also known as a Heuristic System) for financial risk analysis.

The system bypasses complex Machine Learning models and external dependencies (like NumPy or Scikit-learn) to prioritize transparency and portability. It uses predefined financial rules based on an applicant's Income, Loan Amount, and Credit Score to make instantaneous risk predictions.

✨ Key Features

Zero External Dependencies: Runs on standard Python 3.x using only the built-in csv module. No external libraries or installations (pip install) are required.

Heuristic Engine: Employs a set of logical if-else rules (heuristics) to calculate the loan default status (High Risk / Low Risk).

Transparent Decision Making: Provides a clear prediction result and the explicit reason (the rule) that triggered the decision.

Data Validation: Includes robust input validation to handle non-numeric data gracefully.

CLI Interface: Simple, interactive command-line interface for assessing new applicants.

⚙️ Technologies Used

Technology

Role in Project

Python 3.x

Core language for application development and execution.

csv Module

Used for reading the static historical data (loan_data_simple.csv).

Command Line Interface (CLI)

The interface for all user interaction and output display.

🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing and demonstration purposes.

Prerequisites

You only need Python 3.x installed on your operating system.

Installation and File Setup

Clone or Download: Get the simple_predictor.py file and save it in a dedicated folder.

Create Data File: In the same folder, create a file named loan_data_simple.csv and populate it with the following data:

Income,Loan Amount,Credit Score,Default
60,100,7,0
80,120,9,0
45,80,5,1
100,200,8,0
50,110,6,1
90,150,8,0
30,70,4,1
70,130,7,0
40,90,5,1
110,250,9,0


Execute the Script: Open your terminal, navigate to the project directory, and run the script:

python simple_predictor.py


🧪 Testing and Validation

The system requires manual testing to verify that the rule-based logic is functioning correctly.

Logic Test Scenarios

Run the script and enter the following input sets to confirm the expected outcomes based on the internal rules:

Scenario

Income (K)

Loan Amt (K)

Score (1-10)

Expected Result

Triggering Rule

Low Risk (TC1)

150

100

9

LOW RISK

Rule 3: High Credit Score

High Ratio Risk (TC2)

50

150

7

HIGH RISK

Rule 1: High Loan vs. Income

Low Score Risk (TC3)

40

50

4

HIGH RISK

Rule 2: Low Score and Low Income

Input Validation Test

Test the application's stability by attempting to enter non-numerical data (e.g., typing ten instead of 10) when prompted. The system should gracefully handle the error and ask you to re-enter the input.

📊 Sample Result

A successful run of the application will display the following output structure on the console:

--- New Loan Applicant Assessment (Simple Rule-Based) ---
Enter Annual Income (in thousands, e.g., 75 for $75,000): 40
Enter Loan Amount Requested (in thousands, e.g., 150 for $150,000): 130
Enter Simplified Credit Score (e.g., 1 to 10): 5

-------------------------------------------
APPLICANT DATA: Income=40.0K, Loan=130.0K, Score=5.0
RESULT: 🚨 HIGH RISK - Predicted to DEFAULT
REASON: High Loan vs. Income
-------------------------------------------

--- Training Data Snapshot (From CSV) ---
Columns: Income, Loan Amount, Credit Score, Default
['60', '100', '7', '0']
...
Total rows read: 10


📝 Future Enhancements

Potential areas for future development include:

Machine Learning Integration: Incorporating libraries like NumPy and Scikit-learn to train a more accurate Logistic Regression or Decision Tree model.

GUI Implementation: Developing a desktop GUI (e.g., using Tkinter) to replace the command-line interface.

Database: Integrating a lightweight database (like SQLite) for persistent storage of application results.
