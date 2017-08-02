#!/usr/bin/env python
import LSD, gzip
import pandas as pd, numpy as np
from os.path import expanduser, exists
from itertools import count
from LSD import storeDatasetLocally, datadir, Dataset

def get_NB39():
    """
    39 neuroblastoma cell lines + RPE1 and HU.FETAL.BRAIN

    Reference: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89413
    Source: https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE89413&format=file&\
file=GSE89413%5F2016%2D10%2D30%2DNBL%2Dcell%2Dline%2DSTAR%2Dfpkm%2Etxt%2Egz
    """
    exprdata = pd.read_table(
        gzip.open(
            datadir+'GEO/NB39_celllines_Maris/GSE89413_2016-10-30-NBL-cell-line-STAR-fpkm.txt.gz',
            'rt',encoding='UTF-8'
        ),
        index_col='GeneID'
    )

    return Dataset(exprdata=exprdata)