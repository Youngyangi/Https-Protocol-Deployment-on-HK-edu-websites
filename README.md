# Https-Protocol-Deployment-on-HK-edu-websites
Msc course Cryptography project, data analysis part.  
In the analysis, I analyzed the data by school order in following aspects:
1. Number of success in applying https and number of failure and stored the failed websites. 
2. The TLS/SSL method and encryption between website and current user.
3. The valid period of each’s certificate
4. Digital certificate algorithm.
5. Certificate holder’s public key encryption
6. Certificate issuer for each website
We used Python to collect over data from an excel file and applied statistic.   
___  
  From direct sense of the result, we could say  
1.	most schools have a https deployment rate over 70% (Lingnan University even have 100% deployment rate) while HKUST might be one exception with only 51% deployment rate.  
2.	TLS1.2 is commonly used upon websites that are able to deploy https protocol, which means the connection is well-secured upon those websites. 
3.	The validation of certificate varies from several months to around 2 years, while no certificate will be valid constantly for over 3 years, which requires websites to re-apply for certificate to stay secure. 
4.	The certificate algorithms of these websites are all sha256RSA
5.	The certificate holder’s public key encryptions are all using RSA
6.	The certificate issuers come from DigiCert, Let’s Encrypt, GoDaddy, Amazon, Sectigo, etc. a single school may contain several of these or use only one of them, 


 ___ 
  Deployment overview:  
  (n,m,f) denotes n = total website numbers of each school, 
  m = sccusses deployment numbers, 
  f = failure deployment numbers
  
 {'hku': (96, 77, 19),   
'ln': (95, 95, 0),   
'ust': (98, 50, 48),   
'eduhk': (94, 92, 2)}