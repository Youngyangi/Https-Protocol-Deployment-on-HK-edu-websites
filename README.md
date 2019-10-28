# Https-Protocol-Deployment-on-HK-edu-websites
Msc course Cryptography project, data analysis part.  
对各个网站的证书与加密数据进行分析：
1. user_connection统计了网站与当前用户的连接加密方式，nan代表https部署失败
2. certificate_org统计了各网站证书的颁发人
3. certificate_date统计了各网站证书的有效期分布
4. 部署https成功的网站，‘证书签名算法’均为sha256RSA
5. 部署https成功的网站，‘证书持有者公钥算法’均为RSA加密
6. failure保存了https部署失败的网站  
  
  Deployment overview:  
  (n,m,f) denotes n = total website numbers of each school, 
  m = sccusses deployment numbers, 
  f = failure deployment numbers
  
 {'hku': (96, 77, 19),   
'ln': (95, 95, 0),   
'ust': (98, 50, 48),   
'eduhk': (94, 92, 2)}