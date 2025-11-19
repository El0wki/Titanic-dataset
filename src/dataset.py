def extractDataSet():
    import kagglehub
    from kagglehub import KaggleDatasetAdapter

    path = "Titanic-Dataset.csv"

    df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "yasserh/titanic-dataset",
    path
    )   
    return df

def startingSample(df, sampleNum=5):
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
    print(df.sample(sampleNum))

def cleanseData(df):


def filterDataBy(df):

