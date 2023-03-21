# Payday calendar
CLI application to generate CSV file containing paydays and their respective reminder dates.

## Packages used
* holidays
* numpy
* pytest
    
## Usage
1. Clone the repository
2. Open terminal/cmd in dir
3. Install virtualenv
    ~~~sh
    > py -m pip install virtualenv
    ~~~
4. Create and activate a new virtual environment
    ~~~sh
    > py -m venv env
    > env\Scripts\activate
    ~~~
5. Install requirements
    ~~~sh
    > py -m pip install -r requirements.txt
    ~~~
6. Run
    * a. Tests
        ~~~sh
        > pytest test.py
        ~~~
    * b. Application
        ~~~sh
        > py app.py
        ~~~

## Test coverage
~~~sh
Name      Stmts   Miss  Cover
-----------------------------
app.py       31      1    97%
test.py      49      0   100%
-----------------------------
TOTAL        80      1    99%
~~~