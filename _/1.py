import enum

import pandas as pd


class Column0Type(enum.Enum):
    GT3 = 1
    LE3 = 2


class Column1Type(enum.Enum):
    HOME = 1
    COURSE = 2
    REPUTATION = 3
    OTHER = 4


class ColumnParentType(enum.Enum):
    MOTHER = 1
    FATHER = 2
    OTHER = 3


class ColumnYesNoType(enum.Enum):
    YES = 1
    NO = 2


def read_csv(file="7"):
    path = r'data/' + file + '.csv'
    data = pd.read_csv(path, header=None, sep=';')
    print(data)
    consolidate_data(data)
    print(data)


def consolidate_data(df):
    for idx, row in df.iterrows():
        df.loc[idx, 0] = Column0Type[df.loc[idx, 0].upper()].value
        df.loc[idx, 1] = Column1Type[df.loc[idx, 1].upper()].value
        df.loc[idx, 2] = ColumnParentType[df.loc[idx, 2].upper()].value
        df.loc[idx, 5] = ColumnYesNoType[df.loc[idx, 5].upper()].value
        df.loc[idx, 6] = ColumnYesNoType[df.loc[idx, 6].upper()].value


if __name__ == '__main__':
    read_csv()
