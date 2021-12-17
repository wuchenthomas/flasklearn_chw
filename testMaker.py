import csv
import numpy as np
import pandas as pd

fields = ['x1']


def test1():
    data = data1 = data2 = []
    df1 = pd.read_csv("csvtest1.csv", usecols=fields)
    df2 = pd.read_csv("csvtest2.csv", usecols=fields)
    # df1 = pd.read_csv("csvtest1.csv")
    # df2 = pd.read_csv("csvtest2.csv")
    # print(df1.apply(tuple,1))
    array1 = np.array(df1)
    array2 = np.array(df2)

    df_CSV_1 = pd.DataFrame(array1, columns=fields)
    df_CSV_2 = pd.DataFrame(array2, columns=fields)

    df_CSV_1.index += 1
    df_CSV_2.index += 1

    # print(df_CSV_1.eq(df_CSV_2).to_string(index=True))

    a = df1[df1.eq(df2).all(axis=1) == False]
    a.index += 1
    print(a.to_string(index=True))
    # print(df1.apply(tuple, 1).isin(df2.apply(tuple, 1)))
    # print(type(df1.apply(tuple, 1).isin(df2.apply(tuple, 1))))


def test2():
    print("test2")
    df1 = pd.read_csv("csvtest1.csv", usecols=fields)
    df2 = pd.read_csv("csvtest2.csv", usecols=fields)
    df_CSV_1 = pd.DataFrame(df1, columns=fields)
    df_CSV_2 = pd.DataFrame(df2, columns=fields)
    ret = pd.merge(df_CSV_1, df_CSV_2, on='x2')
    print(ret)


def test3():
    print("test3")
    df1 = pd.read_csv("csvtest1.csv", usecols=fields)
    df2 = pd.read_csv("csvtest2.csv", usecols=fields)

    df1['LayerCheck'] = np.where(df1['x1'] == df2['x1'], 'True', 'True')
    df1.index += 1
    df2_x2 = df2['x1']
    df2_x2 = pd.Series(df2_x2)
    df1 = df1.assign(df2_x2=df2_x2.values)
    print(df1.to_string(index=True))


def test4():
    df1 = pd.read_csv("csvtest1.csv", usecols=fields)
    df2 = pd.read_csv("csvtest2.csv", usecols=fields)
    # result1 = df1[~df1.apply(tuple, 0).isin(df2.apply(tuple, 0))]
    # result1 = df1.apply(tuple, 0).isin(df2.apply(tuple, 0))
    # print(result1)
    print(df1.apply(tuple, 0))
    print(df2.apply(tuple, 0))
    print(df1.apply(tuple, 0).isin(df2.apply(tuple, 0)))


def test5(csv1, csv2, Layer1, Layer2, skip_header1=0, skip_header2=0, RFFE_Nr1=0, RFFE_Nr2=0, Layer_col1=0,
          Layer_col2=0):
    df1 = pd.read_csv(csv1, skiprows=skip_header1)
    # print(df1.columns[Deg_col1])
    df2 = pd.read_csv(csv2, skiprows=skip_header2)
    # print(df2.columns[Deg_col2])
    df1 = df1.rename(columns={df1.columns[RFFE_Nr1]: 'RFFE_Nr', df1.columns[Layer_col1]: 'Layer'})
    df2 = df2.rename(columns={df2.columns[RFFE_Nr2]: 'RFFE_Nr', df2.columns[Layer_col2]: 'Layer'})
    # df1.columns[Deg_col] = 'Designator'
    # print(df2.columns[Deg_col2])
    # df1.columns[Layer] = 'Layer'
    # df2.columns[Deg_col] = 'Designator'
    # df2.columns[Layer] = 'Layer'
    # print(df1[df1['Layer'].isin([Layer1])]['RFFE_Nr'])
    df1_layer_slt = df1[df1['Layer'].isin([Layer1])]
    # print(df2['Layer'])
    # print(df2[df2['Layer'].isin([Layer2])]['RFFE_Nr'])
    df2_layer_slt = df2[df2['Layer'].isin([Layer2])]
    # print(df2_layer_slt)
    complist = []
    comp_rffe_nr = df2_layer_slt['RFFE_Nr']
    # print(comp_rffe_nr)
    for i in comp_rffe_nr:
        if i and type(i) == str:
            complist.append(i)
    comp_stay = df1_layer_slt[df1_layer_slt['RFFE_Nr'].isin(complist)].values.tolist()
    for comp in comp_stay:
        print(comp)
    return comp_stay


def test6():
    df1 = pd.read_csv('Sample Pick and Place CSV 1.csv', skiprows=12)
    df2 = pd.read_csv('Sample Pick and Place CSV 2.csv', skiprows=11)
    # print(df1.columns.values)
    # print(df2.columns.values)
    # print(df1.columns.values[8])
    # print(df2.columns.values[7])
    df1_layer_slt = df1[df1['Layer'].isin(['TopLayer'])]
    df2_layer_slt = df2[df2['Layer'].isin(['TopLayer'])]
    print(df1_layer_slt.columns)
    print(df1_layer_slt.values[1])
    print(df1_layer_slt)
    print(df2_layer_slt)
    comp_rffe_nr = df2_layer_slt['RFFE_PartNo']
    complist = []
    # print(comp_rffe_nr)
    for i in comp_rffe_nr:
        if i and type(i) == str:
            complist.append(i)
    print(df1_layer_slt['RFFE_PartNo'].isin(['C-xx100N-X50402-01']))
    comp_stay = df1_layer_slt[df1_layer_slt['RFFE_PartNo'].isin(complist)].values.tolist()
    print(comp_stay)

def test7():
    print(type('A') == str)

csv1 = "Sample Pick and Place CSV_UTF8.csv"
csv2 = "Sample Pick and Place CSV_UTF8.csv"
test5(csv1,csv2,'TopLayer','TopLayer',12,12,8,8,2,2)