import pandas as pd
import re
from collections import defaultdict

df = pd.read_csv('data.csv', encoding='utf8')
columns = df.columns
schools = ['hku', 'ust', 'ln', 'eduhk']
websites = df['网址'].values.tolist()
websites = [str(x) for x in websites]


def find_web(keyword, string):
    pattern = re.compile('\.{}\.'.format(keyword))
    find = pattern.findall(string)
    return False if find == [] else True


def get_schooldict():
    schools_dict = defaultdict(list)
    for school in schools:
        for i, web in enumerate(websites):
            if find_web(school, web):
                schools_dict[school].append(i)
    return schools_dict


def sep_by_school():
    schools_dict = get_schooldict()
    temp = []
    for web in schools_dict['hku']:
        temp.append(df[web:web + 1])
    df_hku = pd.concat(temp, axis=0)
    df_hku.to_csv("data/hku.csv", index=False)
    temp = []
    for web in schools_dict['ust']:
        temp.append(df[web:web + 1])
    df_ust = pd.concat(temp, axis=0)
    df_ust.to_csv("data/ust.csv", index=False)
    temp = []
    for web in schools_dict['ln']:
        temp.append(df[web:web + 1])
    df_ln = pd.concat(temp, axis=0)
    df_ln.to_csv("data/ln.csv", index=False)
    temp = []
    for web in schools_dict['eduhk']:
        temp.append(df[web:web + 1])
    df_eduhk = pd.concat(temp, axis=0)
    df_eduhk.to_csv("data/eduhk.csv", index=False)


sep_by_school()
failure = df[df.isnull().T.any()]
failure.to_excel('failure.xls', encoding='gbk', index=False)