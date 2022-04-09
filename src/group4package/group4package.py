# ' Plot's a Countplots
# '
# 'Creates countplots for data frame with all the given x and y values,
# '
# ' @param A data frame with all the values of which we want the countplots
# ' @param string the column name heading for x-values
# ' @param string the name of the plot
# '
# ' @return An plot of the counts between two parameters of the given data frame.
# '         The plot should have a x label, a y label and a title.


from function_count_plot.py import count_plot

#' Calculate summary statistics
#'
#' Creates a new data frame with only the numerical columns of input and 4 rows,
#' listing the mean for each column present in the input data frame,
#' the standard deviation,
#' the minimum value for each column
#' and the maximum value for each column.
#' Columns in input that are categorical or not fully numerical are not included in returned dataframe
#'
#' @param data_frame A data frame with number values
#'
#' @return A data frame with four rows.
#'   The first row (named mean) lists the mean of each column from the input data frame.
#'   The second row (named std) lists the standard deviation of each column from the input data frame.
#'   It will have the same number of columns as the fully-numerical columns present in input data frame.

from summary_stats_function.py import get_summary_stats

