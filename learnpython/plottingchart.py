import pandas as pd
import numpy as np

from bokeh.plotting import figure, show, output_file, vplot
from bokeh.models import ColumnDataSource, HoverTool, BoxSelectTool

df=pd.read_csv(r"C:\Users\Alok Satpathy\Desktop\state\namebystate\namebystate\learnpython\Sample_DSC_Data.txt", sep='\t', skiprows=78, header=None)

x = df[0]
y = df[1]


TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,hover,resize,crosshair"

p1 = figure(title="Time vs Temperature", tools=TOOLS)

p1.circle(x, y, legend="time-temperature", size=1)
p1.xaxis.axis_label = "Time"
p1.yaxis.axis_label = "Temperature"

x1 = df[2]
y1 = df[1]

p2 = figure(title="Heat Flow vs Temperature", tools=TOOLS)

p2.circle(x1, y1, legend="Heat Flow - Temperature", fill_color=None, line_color="green", size=1)
p2.xaxis.axis_label = "Heat Flow"
p2.yaxis.axis_label = "Temperature"

output_file("graph.html", title="Graph")

show(vplot(p1, p2))  # open a browser