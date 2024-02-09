# Python online shopping site automation project

This file contains the steps to download/clone and run the selenium and pyTest based project

## Installation of required libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the  requirements from the requirements.txt file

For Windows 
```bash
pip install -r requirements.txt
```
For Linux
```bash
pip3 install -r requirements.txt
```
# Running the test cases
To run the test cases using allure-pytest, use the following command
```bash
pytest --alluredir="./reports"
```
in the same directory where your test case is located

Then to generate allure report use the following command
```bash
allure serve "path of reports"
```
where path of reports is the location of your reports folder.

If you just want to run the test cases using pytest and generate the normal pytest html reports then use the command:
```bash
pytest -v --html=your-report-name.html
```
replace your-report-name with the name that you want to give for your HTML report
