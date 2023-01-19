from setuptools import setup, find_packages

NAME = 'churn_prediction'
DESCRIPTION = " This is to predict churn"
AUTHOR = "rahul"

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    package_dir={" ": 'churn_model'},
    package_data={"churn_model": ["data/raw/*.csv", "models/*.pkl", '*.yaml']},
    include_package_data=True,
    license='BSD-3'

)
