# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:23:42 2021

@author: Siamak Khatami
@Email: siamak.khatami@ntnu.no
@License: https://creativecommons.org/licenses/by-nc-sa/4.0/
          Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
@Source: https://github.com/copatrec
@document: https://github.com/copatrec
@Cite:
"""
try:
    from copatrec import Copatrec  # If package is installed
except ImportError:
    from src.copatrec import Copatrec  # If package files cloned
import pandas as pd
import pickle

data = pd.read_pickle("../Data/Data.pkl")
data = data[['year', 'countryname', 'gdppc', 'Government Integrity']]
time_Col = 'year'
category_column = 'countryname'
data.columns
Dep_Var = 'gdppc'
data = data.astype({'gdppc':float,
                    'Government Integrity':float,
                    'year':str,
                    'countryname':str})

SM = Copatrec(data, Dep_Var, time_Col, category_column, True, False)





intervals, outliers = SM.panel_outliers(method='beta', plot_pairs = True, plot_hists = True, plot_outliers_name=True)
intervals, outliers = SM.panel_outliers(method='normal', plot_pairs = True, plot_hists = True, plot_outliers_name=True)
intervals, outliers = SM.panel_outliers(method='IQR', plot_pairs = True, plot_hists = True, plot_outliers_name=True)

intervals, outliers = SM.time_series_outliers(sl=0.05, method='beta', plot_pairs=True, plot_hists = True, plot_outliers_name=True)
intervals, outliers = SM.time_series_outliers(sl=0.05, method='normal', plot_pairs=True, plot_hists = True, plot_outliers_name=True)
intervals, outliers = SM.time_series_outliers(sl=0.05, method='IQR', plot_pairs=True, plot_hists = True, plot_outliers_name=True)

intervals, outliers = SM.cross_sectional_outliers(sl=0.05, method='beta', plot_pairs=True, plot_hists=True, plot_outliers_name=True)
intervals, outliers = SM.cross_sectional_outliers(sl=0.05, method='normal', plot_pairs=True, plot_hists=True, plot_outliers_name=True)
intervals, outliers = SM.cross_sectional_outliers(sl=0.05, method='IQR', plot_pairs=True, plot_hists=True, plot_outliers_name=True)

Opt_Forms_Dict, All_Forms_Dict, Error_Terms = SM.panel(max_epochs=8000,
                                                       alpha=0.05,
                                                       standardization=True,
                                                       plot=True,
                                                       show_time_label=False,
                                                       show_category_label=False,
                                                       drop_outliers=True,
                                                       show_outliers=True,
                                                       plot_predicted_outliers=True,
                                                       outlier_method='beta')
Opt_Forms_Dict, All_Forms_Dict, Error_Terms = SM.time_series(max_epochs=8000,
                                                       alpha=0.05,
                                                       standardization=True,
                                                       plot=True,
                                                       show_time_label=False,
                                                       show_category_label=False,
                                                       drop_outliers=False,
                                                       show_outliers=True,
                                                       plot_predicted_outliers=True,
                                                       outlier_method='beta')
Opt_Forms_Dict, All_Forms_Dict, Error_Terms = SM.cross_sectional(max_epochs=8000,
                                                             alpha=0.05,
                                                             plot=True,
                                                             drop_outliers=False,
                                                             show_outliers=True,
                                                             plot_predicted_outliers=True,
                                                             show_time_label=False,
                                                             outlier_method='beta',
                                                             plot_only_best=True)


All_Forms_Dict['Government Integrity']['sin'].save("test")
All_Forms_Dict['Government Integrity']['sin'].summary_items()
All_Forms_Dict['Government Integrity']['sin'].Data
All_Forms_Dict['Government Integrity']['sin'].Independent_Var
All_Forms_Dict['Government Integrity']['sin'].report()
All_Forms_Dict['Government Integrity']['sin'].help()

file = open('test.pickle', 'rb')
summ = pickle.load(file)
summ.report()
