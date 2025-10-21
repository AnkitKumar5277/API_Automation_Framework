Python API Automation Framework
Hybrid Custom API Automation Framework include the proper folder structure.

<img width="1265" height="653" alt="image" src="https://github.com/user-attachments/assets/433f6250-b7c7-4620-88c7-704d5c1bc41b" />

Tech Stack

    Python 3.13
    Requests - HTTP Requests
    PyTest - Testing Framework
    Reporting - Allure Report, PyTest HTML
    Test Data - CSV, Excel
    Parallel Execution - x distribute (xdist)
    Advance API Testcase - jsonschema

How to Install Packages

    pip install requests pytest pytest-html faker allure-pytest jsonschema

How to run your Testcase Parallel pip install pytest-xdist

How to run the Basic Test with Allure report

    pytest tests/tests/crud/test_create_booking.py  --alluredir=allure_result -s

**API Automation Framework  (Python)**

1. ** src - parent**
    1. constants - It is a class containing the URLs
    2. helpers 
        1. payload manager - which will keep the payload - json
        2. common verification - assertions methods which can be reused.
        3. api request wrapper -> pre built methods to make the POST, PUT, PATCH, DELETE.
    3. tests
        1. which will contain your testcases
            1. crud - individual test cases ( positive, negative)
            2. e2e - end to end test cases (. e.g create booking ->  update booking -> delete booking ->. verify that it is deleted)
    4. utils 
        1. utilities, csv fie reading, extra extra....

### **Why do we need Framework?**
1. Folder structure. 
2. maintenance will be easy
3. Reuse



