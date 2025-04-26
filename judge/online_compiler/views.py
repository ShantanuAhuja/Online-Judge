from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess
import os
from pathlib import Path
from django.conf import settings
from problems.models import Problem
from django.http import HttpResponse
from problems.models import CodeSubmission
from problems.models import Problem
from problems.models import Testcase
import uuid
import shutil
import re



@login_required
def submitCode(request):
    if request.method == 'POST':
        languageSelect = request.POST.get('language-select')
        problemName = request.POST.get('problem-name')
        codeEditor = request.POST.get('code-editor')
        testcaseInput = request.POST.get('testcase-input')
        action = request.POST.get('action')
        print(languageSelect)
        print(problemName)
        outputResult, codeFilePath = runCode(languageSelect, codeEditor, testcaseInput, action, problemName)
        print(outputResult)
        
        user = request.user

        if action == "submit":
            submission = CodeSubmission(
                ProblemName=problemName,
                user=user,
                language=languageSelect,
                code=codeFilePath,
                verdict=outputResult,
            )
            submission.save()

    return render(request, 'codeSubmission.html', {
        "languageSelect": languageSelect,
        "codeEditor": codeEditor,
        "testcaseInput": testcaseInput,
        "outputData": outputResult,
    })


def runCode(languageSelect, codeEditor, testcaseInput, action, problemName):
    from subprocess import TimeoutExpired

    project_path = Path(settings.BASE_DIR) / "submissions"
    directories = ["inputs", "outputs", "codes"]

    # Ensure directories exist
    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())
    code_file_name = f"{unique}.{languageSelect.lower()}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    # Save the code and input files
    with open(code_file_path, "w") as code_file:
        code_file.write(codeEditor)

    with open(input_file_path, "w") as input_file:
        input_file.write(testcaseInput)

    with open(output_file_path, "w") as output_file:
        pass

    TIME_LIMIT_SECONDS = 5  # timeout for code execution

    if action == "submit":
        req_problem = Problem.objects.get(name=problemName)
        testcases = req_problem.testcases.all()[2:]

    # ========== C++ ==========
    if languageSelect.lower() == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["clang++", str(code_file_path), "-o", str(executable_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if compile_result.returncode == 0:
            if action == "run":
                try:
                    with open(input_file_path, "r") as input_file:
                        with open(output_file_path, "w") as output_file:
                            subprocess.run(
                                [str(executable_path)],
                                stdin=input_file,
                                stdout=output_file,
                                stderr=subprocess.PIPE,
                                timeout=TIME_LIMIT_SECONDS
                            )
                except TimeoutExpired:
                    return ("Time Limit Exceeded", code_file_path)
            else:
                for tc in testcases:
                    input_data = tc.input
                    expected_output = tc.output.strip()
                    try:
                        process = subprocess.run(
                            [str(executable_path)],
                            input=input_data,
                            text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            timeout=TIME_LIMIT_SECONDS
                        )
                        actual_output = process.stdout.strip()
                        if actual_output != expected_output:
                            return ("Wrong Answer", code_file_path)
                    except TimeoutExpired:
                        return ("Time Limit Exceeded", code_file_path)

                return ("Accepted", code_file_path)
        else:
            with open(output_file_path, "w") as output_file:
                error_message = compile_result.stderr.strip() or "Compilation failed."
                output_file.write(error_message)

    # ========== Python ==========
    elif languageSelect.lower() == "py":
        if action == "run":
            try:
                with open(input_file_path, "r") as input_file:
                    with open(output_file_path, "w") as output_file:
                        process = subprocess.run(
                            ["python3", str(code_file_path)],
                            stdin=input_file,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            timeout=TIME_LIMIT_SECONDS
                        )
                        if process.returncode == 0:
                            output_file.write(process.stdout.strip())
                        else:
                            output_file.write(process.stderr.strip())
            except TimeoutExpired:
                return ("Time Limit Exceeded", code_file_path)
        else:
            for tc in testcases:
                input_data = tc.input
                expected_output = tc.output.strip()
                try:
                    process = subprocess.run(
                        ["python3", str(code_file_path)],
                        input=input_data,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        timeout=TIME_LIMIT_SECONDS
                    )
                    actual_output = process.stdout.strip()
                    if actual_output != expected_output:
                        return ("Wrong Answer", code_file_path)
                except TimeoutExpired:
                    return ("Time Limit Exceeded", code_file_path)

            return ("Accepted", code_file_path)

    # ========== Java ==========
    elif languageSelect.lower() == "java":
        class_name = "Main"
        temp_java_file = code_file_path.parent / f"{class_name}.java"

        # Step 1: Copy content from original file to Main.java
        shutil.copy(code_file_path, temp_java_file)

        # Step 2: Compile Main.java
        compile_result = subprocess.run(
            ["javac", str(temp_java_file)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if compile_result.returncode != 0:
            with open(output_file_path, "w") as output_file:
                output_file.write(compile_result.stderr.strip())
        else:
            if action == "run":
                try:
                    with open(input_file_path, "r") as input_file:
                        with open(output_file_path, "w") as output_file:
                            run_result = subprocess.run(
                                ["java", "-cp", str(code_file_path.parent), class_name],
                                stdin=input_file,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                timeout=TIME_LIMIT_SECONDS
                            )
                            output = run_result.stdout.strip() if run_result.returncode == 0 else run_result.stderr.strip()
                            output_file.write(output)
                except TimeoutExpired:
                    with open(output_file_path, "w") as output_file:
                        output_file.write("Time Limit Exceeded")
                finally:
                    class_file = code_file_path.parent / f"{class_name}.class"
                    if class_file.exists():
                        class_file.unlink()
                    if temp_java_file.exists():
                        temp_java_file.unlink()

            elif action == "submit":
                print("submit")
                for tc in testcases:
                    input_data = tc.input
                    expected_output = tc.output.strip()
                    print(input_data)
                    print(expected_output)
                    try:
                        run_result = subprocess.run(
                            ["java", "-cp", str(code_file_path.parent), class_name],
                            input=input_data,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            timeout=TIME_LIMIT_SECONDS
                        )

                        actual_output = run_result.stdout.strip()
                        if actual_output != expected_output:
                            return ("Wrong Answer", code_file_path)
                    except TimeoutExpired:
                        return ("Time Limit Exceeded", code_file_path)

                return ("Accepted", code_file_path)
            
        


    # ========== C ==========
    elif languageSelect.lower() == "c":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["gcc", str(code_file_path), "-o", str(executable_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if compile_result.returncode == 0:
            if action == "run":
                try:
                    with open(input_file_path, "r") as input_file:
                        with open(output_file_path, "w") as output_file:
                            subprocess.run(
                                [str(executable_path)],
                                stdin=input_file,
                                stdout=output_file,
                                stderr=subprocess.PIPE,
                                timeout=TIME_LIMIT_SECONDS
                            )
                except TimeoutExpired:
                    return ("Time Limit Exceeded", code_file_path)
            else:
                for tc in testcases:
                    input_data = tc.input
                    expected_output = tc.output.strip()
                    try:
                        process = subprocess.run(
                            [str(executable_path)],
                            input=input_data,
                            text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            timeout=TIME_LIMIT_SECONDS
                        )
                        actual_output = process.stdout.strip()
                        if actual_output != expected_output:
                            return ("Wrong Answer", code_file_path)
                    except TimeoutExpired:
                        return ("Time Limit Exceeded", code_file_path)

                return ("Accepted", code_file_path)
        else:
            with open(output_file_path, "w") as output_file:
                error_message = compile_result.stderr.strip() or "Compilation failed."
                output_file.write(error_message)

    # ========== Read and Return Final Output ==========
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return (output_data, "")

