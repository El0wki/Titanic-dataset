import pandas as pd
import matplotlib.pyplot as plt
from dataset import DataSet

datasetName = "yasserh/titanic-dataset"
datasetPath = "Titanic-Dataset.csv"

dataset = DataSet(datasetName, datasetPath)
dataset.sampleData()
dataset.cleanseData()