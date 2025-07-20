# EAMCET College Predictor

A Python Tkinter-based application to predict eligible engineering colleges based on your EAMCET rank, gender, caste/category, and branch preference.

## Features

- User-friendly GUI
- Filter by rank, gender, caste/category, and branch
- Displays eligible colleges from a data file

## How to Use
1. Make sure you have Python 3 installed.
2. Place your `colleges_full.txt` file (with data in `|`-separated format) in the      project folder.
3. Run the application:
    ```bash
    python main.py
    ```
4. Enter your details in the GUI and click "Predict Colleges" to see results.

## Data File Format

Your `colleges_full.txt` should have lines like:
```
College Name|Branch|Category|Gender|Cutoff Rank
JNTU College of Engineering, Hyderabad|CSE|OC|M|10011
...
```

## Requirements

- Python 3.x

