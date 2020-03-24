from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def Home(request):
    df = pd.read_csv("C:/Users/arpit pandey/Desktop/Machine Learning/Data_Jobs.csv")

    if request.method == "POST":
        skills = []
        count = []
        data = request.POST
        s1 = data["s1"]
        s2 = data["s2"]
        s3 = data["s3"]
        skills = [s1, s2, s3]
        for i in skills:
            new_df = df[df["Word"] == i.lower()]
            count.append(new_df["Count"].values)
        final = zip(skills, count)
        return render(request, "output.html", {"data":final})

    return render(request, "home.html")