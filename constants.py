"""
Created on Fri Nov 19 12:16:08 2021
@author: Siamak Khatami
@Email: siamak.khatami@ntnu.no
@License: https://creativecommons.org/licenses/by-nc-sa/4.0/
@Source: https://github.com/copatrec/copatrec
@document: https://github.com/copatrec/copatrec
@Cite:
"""


class CST:
    def __init__(self):
        pass

    Panel = 'Panel'
    Time_Series = 'Time_Series'
    Cross_Sectional = 'Cross_Sectional'
    Beta_Method = 'beta'
    Normal_Method = 'normal'
    IQR_Method = 'IQR'

    #  Data Types
    DataType_Series = 'Series'
    Outliers = 'outliers'

    #  Plots
    Hist_title = "Variable: {} | Method: {} \n Time: {} | Category: {}"

    #  General Strings
    ALL = 'ALL'
    Cat = 'Category'
    Time = 'Time'
    Github_URL = "https://github.com/copatrec/copatrec"
    Note = "Note: "
    Statistic = "Statistic: "
    P_val = "p_value:"


class Warns:
    def __init__(self):
        pass
    W101 = "It is highly recommended to drop outliers by an expert of the field."
    W102 = "Analysis error: The number of observations are less than 10."
    #  Result Messages
    R101 = "Fitted"
    R102 = "Done"

    #  Progress
    P101 = "Finding outliers for a {} analysis, Method:{}"

    #  Equation Forms
    EF101 = 'Warning: Here xb equation Represents tanh.'

    # Summary object warnings
    S100 = 'Copatrec aims to analyze complex behaviors.' \
           ' Complex functions can generate their unique curve or create a' \
           ' snapshot of a specific range. Thus, it would be beneficial' \
           'to compare the curve with the already known complex behaviors.' \
           ' For example, the logistic function is representative of' \
           ' S-shaped behavior. However, all other tasks like oscillator or' \
           ' sine can generate S-shape behavior in a specific range. So, ' \
           'while the generated function can be used for predictions' \
           '(so sensitive and dependent to the case), for interpretation' \
           ' of behavior, an expert should be involved.'
    S101 = 'Standard error of regression can be used' \
           ' to evaluate both linear and nonlinear regressions' \
           ' and is valid if it is less than desired' \
           ' significance level. This is the main evaluation' \
           ' criteria for best fitted models.'

    S102 = 'The normal test is using Skewness and ' \
           'kurtosis to evaluate whether estimation ' \
           'errors are distributed normally around zero or ' \
           'not. "Error Normal Test" is using p-value ' \
           'which means it should interpreted as "There ' \
           'are(not) enough evidence to claim errors are ' \
           'normally distributed" and should not used ' \
           'alone to accept or reject the functionality ' \
           'of a model.'


class Errs:
    def __init__(self):
        pass
    E000 = ""
    Ignore = "ignore"
    #  Basic Errors
    E101 = "RuntimeError"
    #  Package Errors
    E201 = "Cannot fit none of equation forms."
    E202 = "Cannot find any fitted function to plot."
    E203 = "All rows are null value and dropped."
    E204 = "All rows are outlier values and dropped."
    E205 = "Cannot convert data to numerical data type."
    E206 = "No intervals and values for (X={x}, Y={y}) pairs " \
           "in category = {c} and time = {t}.\n" \
           "This mostly happens if all items are 0 or None."
    E207 = "All rows are null/zero value and dropped for " \
           "variable = {}, category = {} and time = {}."
    E208 = "{} intervals could not been calculated. \n {}"
    E209 = "Cannot calculate SE_Params and T values."