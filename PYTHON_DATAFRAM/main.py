import pandas as pd
from pandas.tests.io.parser.test_common import test_read_chunksize_and_nrows


class ReadCsv:
    def data_properties1(self):
       df= pd.read_csv("Vibration.csv")
       df["rolling_meam"]=df.Vibration_Az.rolling(window=2).mean()
       return df;

    def data_properties2(self):
       df= pd.read_csv("Vibration.csv")
       df["rolling_meam"]=df.Vibration_Az.rolling(window=2).mean()
       df["variation"] = df.Vibration_Az.var()
       df["standard_deviation"] = df.Vibration_Az.std()
       df["skewness"] = df.Vibration_Az.skew()
       df["kurtosis"] = df.Vibration_Az.kurtosis()



       return df;




    def data_variation(self):
        df = pd.read_csv("Vibration.csv")
        return df.var();

    def data_mean(self):
        df = pd.read_csv("Vibration.csv")
        return df.mean();

    def data_std(self):
        df = pd.read_csv("Vibration.csv")
        return df.std();

    def data_skew(self):
        df = pd.read_csv("Vibration.csv")
        return df.skew();

    def data_kurt(self):
        df = pd.read_csv("Vibration.csv")
        return df.kurtosis();


    def split_in_chunk(self,url):
       MyList=[]
       chunk_size=500
       batch=1
       for chunk in pd.read_csv(url,chunksize=chunk_size):
        MyList.append(chunk)
        batch= batch+1



        return MyList;






read=ReadCsv()

print(read.split_in_chunk())







