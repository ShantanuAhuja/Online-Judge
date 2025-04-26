# Code Submission System

## Overview

The **Code Submission System** allows users to submit their code for execution and comparison with predefined test cases. The system supports multiple programming languages, including **C**, **C++**, **Java**, and **Python**. The submitted code is compiled and executed, and the system provides feedback on whether the code passes the test cases.

## Features

### 1. User Code Submission
- Users can submit their code by selecting a programming language and entering their code into an editor.
- The system processes the code by compiling or interpreting it based on the selected programming language.

### 2. Multiple Language Support
- The system supports various programming languages, such as **C**, **C++**, **Java**, and **Python**.
- Each language has its own compilation and execution procedure.

### 3. Code Evaluation
- The submitted code is executed against predefined test cases.
- The system verifies the output of the code and compares it to the expected output.

### 4. Result Feedback
- After code execution, the system provides feedback in the form of a **verdict** (Accepted, Wrong Answer, Time Limit Exceeded, or Compilation Error).
- Users can review the output and compare it to the expected results.

### 5. Time-Limited Execution
- The system executes code submissions with a strict time limit (default: **5 seconds** per test case).
- If the code exceeds the time limit, the system returns a **Time Limit Exceeded** verdict.

## Process Flow

### 1. User Interface (Frontend)
- The **Code Submission Page** allows users to select a language, input code, and provide test case inputs.
- The form sends a **POST** request to the backend for processing.

### 2. Backend Logic (Django)
- The backend view `submitCode` handles the code submission. It processes the request, runs the code, and returns the output result.
- The code is saved in the server's file system and executed based on the selected programming language.

### 3. Running the Code
- The `runCode` function handles different languages:
  - **C/C++**: Code is compiled with **GCC/Clang++** and executed.
  - **Java**: Code is compiled with **javac** and executed with the `java` command.
  - **Python**: Code is executed with **Python 3**.

### 4. Output Verification
- The code is tested against the problem's test cases. The system compares the output with the expected output and returns the verdict accordingly.

## Code Submission Process

### Step 1: Submit Code
- The user submits their code via the form. The selected programming language, code, and test case input are sent to the backend for processing.

### Step 2: Backend Processing
- The backend stores the code in a temporary directory and compiles or runs it based on the language selected.
- The output is saved to a file, and the result is compared with the expected output.

### Step 3: Result Feedback
- After the code execution, the system provides feedback to the user, indicating whether the submission was **Accepted**, had a **Wrong Answer**, or encountered a **Time Limit Exceeded** or **Compilation Error**.

## Example Directory Structure


