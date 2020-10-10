import setuptools

setuptools.setup(
    name="bmiankdos",
    version="0.0.2",
    author="Ankur Pandey",
    author_email="ankurpan96@gmail.com",
    description="Simple BMI calculator for large JSON files",
    url="https://github.com/AnkDos/code-20201010-ankurpandey.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'ijson',
          'pandas',
          'pytest'
      ]
)