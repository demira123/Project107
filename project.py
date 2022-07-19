import pandas as pd
import plotly.express as pe

data=pd.read_csv("c107/data.csv")

mean=data.groupby(["student_id" , "level"] , as_index=False)["result"].mean()

sgraph=pe.scatter(mean, x= "student_id", y= "level",  size="result", color="result")


sgraph.show()


