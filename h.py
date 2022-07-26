import csv
import statistics
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()

height_mean=statistics.mean(height_list)
height_median=statistics.median(height_list)
height_mode=statistics.mode(height_list)
height_stdev=statistics.stdev(height_list)

height_first_std_deviation_start, height_first_std_deviation_end=height_mean-height_stdev,height_mean+height_stdev
height_second_std_deviation_start, height_second_std_deviation_end=height_mean-(2*height_stdev),height_mean+(2*height_stdev)
height_third_std_deviation_start, height_third_std_deviation_end=height_mean-(3*height_stdev),height_mean+(3*height_stdev)

height_list_of_data_within_1_std_deviation=[result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation=[result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation=[result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

print("mean={}".format(height_mean))
print("median={}".format(height_median))
print("mode={}".format(height_mode))
print("stdev={}".format(height_stdev))
print("{}% of data lies in 1 std deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data lies in 2 std deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data lies in 3 std deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
