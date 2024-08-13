# FinTech101 Task B.1 Report

Student Name: Thomas VO
Student ID: 103488272

## Task B.1: Setup

### 1. Introduction
This report summarizes the setup process for the FinTech101 project, including environment setup, testing of provided code bases, and initial understanding of the project structure.

### 2. Environment Setup

I set up a virtual environment for the project using the following steps:

```bash
python -m venv .venv
source .venv/bin/activate
```

__OR__ <br>
Bash file I have created to automate the set up the environment and downloading requirements files.
```bash
./init.sh
```
<hr>
I created a `requirements.txt` file with the following contents:

```
numpy
pandas
matplotlib
scikit-learn
tensorflow
yfinance
pandas_datareader
mplfinance
```

To install the required packages, I ran:

```bash
pip install -r requirements.txt
```

### 3. Code Implementation

For this task, I focused on setting up and testing the provided code bases:

1. v0.1 (`stock-prediction.py`) - provided
2. P1 (https://github.com/x4nth055/pythoncode-tutorials/tree/master/machine-learning/stock-prediction)

I cloned both repositories to my local machine and ensured they were runnable within the virtual environment.

### 4. Testing and Results

#### v0.1 (stock-prediction.py)

I successfully ran the v0.1 code. Here's a summary of the results:

- The code downloads stock data for CBA.AX (Commonwealth Bank of Australia) from 2020-01-01 to 2023-08-01.
- It trains an LSTM model to predict stock prices.
- The model makes predictions for the period 2023-08-02 to 2024-07-02.
- A plot is generated comparing actual and predicted prices.

![image](https://github.com/user-attachments/assets/f5737221-d461-419b-8b23-93f6ecb02e94)

#### P1

I also tested the code from the P1 repository. This implementation includes:

- More sophisticated data preprocessing
- A different model architecture
- Additional visualization options

[Insert screenshot of P1 results here]

### 5. Challenges and Solutions

1. Challenge: Deprecation warnings for pandas-datareader
   Solution: Updated the code to use yfinance instead of pandas-datareader for downloading stock data.

2. Challenge: Ensuring consistent environments across v0.1 and P1
   Solution: Created a comprehensive requirements.txt file that satisfies the dependencies of both projects.

### 6. Conclusions and Next Steps

I successfully set up the development environment and tested both v0.1 and P1 code bases. The initial v0.1 code provides a basic framework for stock prediction, while P1 offers more advanced techniques that could be incorporated into our project.

Next steps:
1. Analyze the differences between v0.1 and P1 to identify potential improvements.
2. Begin implementing data processing improvements as outlined in Task B.2.
3. Consider how to incorporate more advanced features from P1 into our project structure.