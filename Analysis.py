import pandas as pd
import re
from collections import defaultdict
from collections import Counter


def get_fail_https(df):
    failure = df[df.isnull().T.any()]
    return failure


data1 = pd.read_csv("data/hku.csv")
fail1 = get_fail_https(data1)
data2 = pd.read_csv("data/ln.csv")
fail2 = get_fail_https(data2)
data3 = pd.read_csv("data/ust.csv")
fail3 = get_fail_https(data3)
data4 = pd.read_csv("data/eduhk.csv")
fail4 = get_fail_https(data4)
fail = {
    'hku': (len(data1), len(data1)-len(fail1), len(fail1)),
    'ln': (len(data2), len(data2)-len(fail2), len(fail2)),
    'ust': (len(data3), len(data3)-len(fail3), len(fail3)),
    'eduhk': (len(data4), len(data4)-len(fail4), len(fail4))
}
print(fail)
a = Counter(data1['与用户建立连接所使用的加密算法'])
print(a.most_common())
a = Counter(data2['与用户建立连接所使用的加密算法'])
print(a.most_common())
a = Counter(data3['与用户建立连接所使用的加密算法'])
print(a.most_common())
a = Counter(data4['与用户建立连接所使用的加密算法'])
print(a.most_common())

a = Counter(data1['证书持有者公钥算法'])
print(a.most_common())
a = Counter(data2['证书持有者公钥算法'])
print(a.most_common())
a = Counter(data3['证书持有者公钥算法'])
print(a.most_common())
a = Counter(data4['证书持有者公钥算法'])
print(a.most_common())


# 统计证书有效时间
def get_validate(string):
    pattern = re.compile("\?(\d+)\?年\?(\d+)\?月\?(\d+)\?日")
    return pattern.findall(string)


def get_date(data):
    date = []
    for i in data['有效期']:
        temp = get_validate(str(i))
        date.append(temp)
    return date


def get_date_distribution(date_list):
    date = defaultdict(int)
    for i in date_list:
        if i == [] or len(i) < 2: continue
        i = i[0][0] + "年" + i[0][1] + '月' + i[0][2] + '日 - ' + \
            i[1][0] + "年" + i[1][1] + '月' + i[1][2] + '日'
        date[i] += 1
    date_column1 = list(date.keys())
    date_column2 = list(date.values())
    return date, date_column1, date_column2


def get_date_df(data, name):
    date = get_date(data)
    date_distri, date_column1, date_column2 = get_date_distribution(date)
    date_csv = {'name': [name] * len(date_column1), 'date': date_column1, 'times': date_column2}
    date_df = pd.DataFrame.from_dict(date_csv)
    date_df = date_df.sort_values(by="times", ascending=False)
    date_df.reset_index(inplace=True)
    date_df.drop(columns='index', inplace=True)
    return date_df

a = get_validate('?2018?年?1?月?10?日 8:00:00 ?2020?年?10?月?1?日'
                 ' 20:00:00,sha256RSA')

date1 = get_date_df(data1, 'hku')
date2 = get_date_df(data2, 'ln')
date3 = get_date_df(data3, 'ust')
date4 = get_date_df(data4, 'eduhk')

date = date1.append([date2, date3, date4], ignore_index=True)
print(date)
date.to_excel("certificate_date.xls", encoding='gbk', index_label='index')


# 统计颁发组织与被颁发组织
def get_orgname(string):
    pattern = re.compile("O = (\w+)")
    return pattern.findall(string)


def get_org_distribution(data):
    org = []
    for i in data['颁发者完整名称']:
        temp = get_orgname(str(i))
        org.extend(temp)
    org_dict = defaultdict(int)
    for i in org:
        if i == []: continue
        if i == 'Let': i = "Let's Encrypt"
        if i =='COMODO': i = "COMODO CA"
        org_dict[i] += 1
    org_column1 = list(org_dict.keys())
    org_column2 = list(org_dict.values())
    return org_dict, org_column1, org_column2


def get_org_df(data, name):
    org_distri, org_column1, org_column2 = get_org_distribution(data)
    org_csv = {'name': [name] * len(org_column1), 'org': org_column1, 'times': org_column2}
    org_df = pd.DataFrame.from_dict(org_csv)
    org_df = org_df.sort_values(by="times", ascending=False)
    org_df.reset_index(inplace=True)
    org_df.drop(columns='index', inplace=True)
    return org_df

find = get_orgname('OU = http://certs.godaddy.com/repository/O = GoDaddy.com, Inc. L = Scottsdale S = Arizona C = US","CN = *.hkuspace.hku.hk')
org1 = get_org_df(data1, 'hku')
org2 = get_org_df(data2, 'ln')
org3 = get_org_df(data3, 'ust')
org4 = get_org_df(data4, 'eduhk')

org = org1.append([org2, org3, org4], ignore_index=True)
print(org)
org.to_excel("org.xls", index_label="index", encoding='gbk')

# 统计证书持有者名称


def get_holdername(string):
    pattern = re.compile("CN = (\w+)")
    return pattern.findall(string)


def get_holder_distribution(data):
    org = []
    for i in data['被颁发人完整名称']:
        temp = get_holdername(str(i))
        org.extend(temp)
    org_dict = defaultdict(int)
    for i in org:
        if i == []: continue
        if i == 'Let': i = "Let's Encrypt"
        if i =='COMODO': i = "COMODO CA"
        org_dict[i] += 1
    org_column1 = list(org_dict.keys())
    org_column2 = list(org_dict.values())
    return org_dict, org_column1, org_column2


def get_holder_df(data, name):
    org_distri, org_column1, org_column2 = get_holder_distribution(data)
    org_csv = {'name': [name] * len(org_column1), 'org': org_column1, 'times': org_column2}
    org_df = pd.DataFrame.from_dict(org_csv)
    org_df = org_df.sort_values(by="times", ascending=False)
    org_df.reset_index(inplace=True)
    org_df.drop(columns='index', inplace=True)
    return org_df


holder1 = get_holder_df(data1, 'hku')
print(data2["证书持有者公钥算法"])