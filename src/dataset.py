class DataSet:
    def __init__(self, datasetName, path):
        self.df = None
        self.name = datasetName
        self.path = path
        self.extractDataSet()

    def extractDataSet(self):
        import kagglehub
        from kagglehub import KaggleDatasetAdapter
        try:
            self.df = kagglehub.dataset_load(
                KaggleDatasetAdapter.PANDAS,
                self.name,
                self.path
            )   
        except Exception as e:
            print("Erro ao importar dados")
        
    def sampleData(self, sampleNum=5):
        try:
            print("shape:", self.df.shape)
            print("colunas:", self.df.columns)
            print("tipos:",self.df.dtypes)
            print("amostras:",self.df.sample(sampleNum))
        except Exception as e:
            print("Erro ao amostrar dados")
        

    def cleanseData(self):
        try:
            print("Valores nulos por coluna:")
            nulls = self.df.isnull().sum()
            print(nulls[nulls > 0])

            for col in self.df.columns:
                if self.df[col].isnull().any():
                    if self.df[col].dtype in ['float64', 'int64']:
                        self.df[col] = self.df[col].fillna(self.df[col].mean())
                    else:
                        self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        except Exception as e:
            print("Erro ao limpar dados")
    
    def filterData(self):
        try:
            print("sla")
        except Exception as e:
            print("Erro ao filtrar dados")
    
    def createNewColumn(self):
        try:
            print("sla")
        except Exception as e:
            print("Erro ao criar nova coluna")
    
    def groupBy(self):
        try:
            print("sla")
        except Exception as e:
            print("Erro ao agrupar dados")
    
    def graph(self):
        try:
            print("sla")
        except Exception as e:
            print("Erro ao filtrar dados")

