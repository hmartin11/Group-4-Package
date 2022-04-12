# group4package

A package for running Group 4's data analysis

## Installation

*Note: This package requires python version 3.9.1 or greater*

```bash
$ pip install group4package
```

## Usage

The following functions in this package were created for Group 4's Project [Predicting Defaults of Credit Card Clients](https://github.com/DSCI-310/DSCI-310-Group-4)
However, they are useful for any data analysis that involves pre-processing data and calculating classification metrics and statistics. 

**`calculate_metrics(FP, TN, TP)`**
-  calulates Recall, F1-Score and Precision for a classification model 

Example:

```python 
from group4package import metrics_function as cm
TN, FP, FN, TP = confusion_matrix(y_test, predict).ravel()
res = cm.calculate_metrics(FP, FN, TP)
```
 
**`get_summary_stats(df)`**
- calculates summary statistics including mean, std, min, and max of numeric columns of a dataframe

Example:

```python 
from group4package import summary_stats_function as ss
ss.get_summary_stats(train_df)
```

- count_plot
- pre-process data 



## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`group4package` was created by Hannah, Jordan, Diana, and Shravan. It is licensed under the terms of the MIT license.

## Credits

`group4package` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
