 # Loan Qualifier

This is a python command-line interface application that allows users to see, filter and save qualifying loans from lenders quickly and easily. The application works by that taking in a `daily_rate_sheet` of loan criteria from various loan providers, asks the user a number of questions to evaluate their loan eligibility, and then returns to them a list of qualifying loans. At the end, it prompts dialogs to further confirm the result of findings and whether the user would like to save it into a CSV file. 

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [pytest](https://docs.pytest.org/en/stable/) - For basic assertion testing of financial calculators and filters, and filio.


---

## Installation Guide

The following dependencies are required to be installed before running the application.

```python
  pip install fire
  pip install questionary
  pip install pytest
  pip install mkdocs
```

---

## Usage

To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts. Attaching three screenshots for three different scenarios.

![Loan Qualifier Prompts If No Qualifying Loans](images/no_result.png)

![Loan Qualifier Prompts If Saving Results In A CSV File](images/not_saving_csv.png)

![Loan Qualifier Prompts If Not Saving Results In A CSV File](images/saving_csv.png)

---

## Contributors

Brought to you by Triology and Christine Guo (www.linkedin.com/in/christine-guo)

---

## License

NoNe
