import pandas as pd
from pathlib import Path
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

def _fetch_UCI_dataset(url, usecache=True):
    """
    Fetch a specific dataset from the University of California Irvine Machine Learning Repository.
    
    Parameters
    ----------
    url : str
        URL for the zip archive of the dataset on the UCI website.
    
    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing the specified dataset.
    """
    name = url.rsplit('/', 1)[-1].replace('+', "_")
    cacheloc = (Path("../data/") / name).with_suffix('.pkl')
    df = None
    if usecache:
        if cacheloc.exists():
            df = pd.read_pickle(cacheloc, compression='gzip')
            
    if df is None:
        resp = urlopen(url)
        zipfile = ZipFile(BytesIO(resp.read()))
        df = pd.concat([pd.read_csv(zipfile.open(file)) for file in zipfile.namelist() if file.endswith('.csv')])
    
    if usecache:
        df.to_pickle(cacheloc, compression='gzip')
    return df

def fetch_beijing_AQ_data():
    """
    Fetch the Beijing Air Quality Dataset from the University of California Irvine Machine Learning Repository.
    
    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing the multi-site data for the air quality dataset.
    
    Notes
    -----
    See the relevant page for more info (https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data),
    including an overview of the dataset variables and a citation.
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00501/PRSA2017_Data_20130301-20170228.zip"
    return _fetch_UCI_dataset(url)

def fetch_flue_gas_data():
    """
    Fetch the Gas Turbine CO and NOx Emission Dataset from the University of California Irvine 
    Machine Learning Repository.
    
    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing the data for the multi-year emission dataset.
    
    Notes
    -----
    See the relevant page for more info (https://archive.ics.uci.edu/ml/datasets/Gas+Turbine+CO+and+NOx+Emission+Data+Set),
    including an overview of the dataset variables and a citation.
    """    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00551/pp_gas_emission.zip"
    return _fetch_UCI_dataset(url)


def fetch_gas_sensor_data():
    """
    Fetch the gas sensor array temperature modulation Dataset from the University of California Irvine 
    Machine Learning Repository.
    
    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing the data for the multi-day experimental dataset.
    
    Notes
    -----
    See the relevant page for more info (https://archive.ics.uci.edu/ml/datasets/Gas+sensor+array+temperature+modulation),
    including an overview of the dataset variables and a citation.
    """    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00487/gas-sensor-array-temperature-modulation.zip"
    return _fetch_UCI_dataset(url)