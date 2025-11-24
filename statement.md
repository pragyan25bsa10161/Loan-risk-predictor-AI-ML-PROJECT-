Project Statement: Rule-Based Loan Risk Predictor

1. Problem Statement

Banks and financial institutions face constant risks from loan defaults. The fundamental problem is the need for a system to efficiently and transparently assess the risk profile of new applicants.

The specific objective of this project is to develop a standalone, lightweight prediction utility, using only basic Python features, that applies logical, expert-defined criteria (heuristics) to classify an applicant as either High Risk (likely to Default) or Low Risk (Safe).

2. Scope of the Project

The scope of this project is limited to a Rule-Based Simulation of a financial risk system.

In Scope:

Developing and implementing simple, predefined business rules (heuristics) for risk assessment.

Implementing robust user input and validation in a Command-Line Interface (CLI).

Providing clear, explainable decision reasons based on the rules.

Demonstrating file handling capability (reading static CSV data).

Out of Scope:

Integration of external Machine Learning libraries (e.g., NumPy, Scikit-learn).

Training a statistically accurate model.

Development of a Graphical User Interface (GUI).

Real-time database integration (uses static CSV data).

3. Target Users

Target User

Primary Use Case

Academic Evaluators

To evaluate basic Python programming skills, understanding of conditional logic, and modular design.

Entry-Level Financial Analysts

As a quick, transparent tool to support initial loan decision-making using established criteria.

Developers

As a simple template for building portable, dependency-free Python applications.

4. High-Level Features

Rule-Based Prediction Engine: Calculates risk status (High/Low) using a set of logical IF-ELSE statements.

Transparent Decision Logic: Outputs the specific reason (rule) that triggered the prediction.

Zero-Dependency Execution: Requires only standard Python; no third-party installations needed.

Interactive CLI: Accepts three key inputs: Income, Loan Amount, and Credit Score.

Robust Input Validation: Ensures all data entered by the user is numerical and within acceptable ranges.
