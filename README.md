# Loan Approval System

This project is a **Loan Approval System** that uses a machine learning model to predict the approval of loans based on various input features. The system is implemented as a web application where users can explore the data, make predictions, and gain insights into the loan approval process.

## Project Structure

- **`xgb_model.pkl`**: Pre-trained XGBoost model used for predicting loan approvals.
- **`loan_approval_dataset.csv`**: Dataset used for training and testing the model.
- **`iip/`**: Contains the core application code:
  - **`app.py`**: The main entry point for the web application.
  - **`explore_page.py`**: Script to explore the dataset and visualize insights.
  - **`predict_page.py`**: Script to input new data and predict loan approval.
  - **`requirements.txt`**: List of Python packages required to run the application.

## Getting Started

### Prerequisites

- **Python 3.8 or higher**: Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
- **Pip**: Ensure you have `pip` installed to manage Python packages.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/iip_capstone_project.git
    cd iip_capstone_project/iip_capstone_project/iip
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Launch the web application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
   Open your web browser and navigate to `https://loan-approval-system.streamlit.app/`. Here, you can explore the dataset and make loan approval predictions.

## Usage

### Exploring the Data

- Navigate to the "Explore" section of the application to visualize and analyze the loan approval dataset. You can interact with various graphs and charts to understand the data distribution and feature importance.

### Predicting Loan Approval

- In the "Predict" section, you can input various details about an applicant, and the model will predict whether the loan will be approved or not.

## Model Details

- The machine learning model used is an XGBoost classifier, which is well-suited for handling tabular data and is known for its performance in prediction tasks. The model was trained on a dataset that includes various features related to loan applicants, such as credit history, income, loan amount, etc.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements, whether they are related to the code, documentation, or any other aspect of the project.

## License

This project is licensed under the MIT License. See the [MIT](https://choosealicense.com/licenses/mit/) file for more details.

## Acknowledgments

- Thanks to [Industry Immersion Africa](https://iiafrica.org/) for providing the resources and support for this project.
- Special thanks to the developers and contributors of the XGBoost library.

---

