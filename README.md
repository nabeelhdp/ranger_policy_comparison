# ranger_policy_comparison
Compare the policies in two Ranger export json files and list missing entries

python3 ranger_compare.py DR-Ranger_Policies_20240425_215850.json Prod-Ranger_Policies_20240425_215841.json

```sh
nmoidu@22232 Downloads % python3 ranger_compare.py DR-Ranger_Policies_20240425_215850.json Prod-Ranger_Policies_20240425_215841.json
```
```
Running ranger_compare.py  on files: DR-Ranger_Policies_20240425_215850.json and Prod-Ranger_Policies_20240425_215841.json
==============================================================
Ranger apache version on policy file DR-Ranger_Policies_20240425_215850.json  is: 2.1.0.7.1.7.2047-1
Ranger Admin Hostname on policy file DR-Ranger_Policies_20240425_215850.json  is: xxx.xx.xxx.com
Ranger Policy count on policy file DR-Ranger_Policies_20240425_215850.json  is: 272
Service name on policy file DR-Ranger_Policies_20240425_215850.json  is: cm_hive
==============================================================
Ranger apache version on policy file Prod-Ranger_Policies_20240425_215841.json  is: 2.1.0.7.1.7.2047-1
Ranger Admin Hostname on policy file Prod-Ranger_Policies_20240425_215841.json  is: yyy.yy.xxx.com
Ranger Policy count on policy file Prod-Ranger_Policies_20240425_215841.json  is: 274
Service name on policy file Prod-Ranger_Policies_20240425_215841.json  is: cm_hive
==============================================================
Comparing xxx.xx.xxx.com  against  yyy.xx.xxx.com
Missing policy: ID: 251 Name: exploratory_fraud Description: Hive database access policy for usecase - exploratory_fraud
Missing policy: ID: 252 Name: exploratory_fraud_url Description: HDFS url access policy for RW usecase group - exploratory_fraud
Missing policy: ID: 253 Name: exploratory_dsateam Description: Hive database access policy for usecase - exploratory_dsateam
Missing policy: ID: 254 Name: exploratory_dsateam_url Description: Hive database access policy for usecase - exploratory_dsateam
Comparing yyy.xx.xxx.com  against  xxx.xx.xxx.com
Missing policy: ID: 286 Name: erm_analytics Description: Hive database access policy for usecase - erm_analytics
Missing policy: ID: 287 Name: erm_analytics_url Description: HDFS url access policy for RW usecase group - erm_analytics
Missing policy: ID: 290 Name: Empl_learning Description: Hive database access policy for usecase - Empl_learning
Missing policy: ID: 291 Name: Empl_learning_url Description: HDFS url access policy for RW usecase group - Empl_learning
Missing policy: ID: 304 Name: exceptionsexpress Description: Hive database access policy for usecase - exceptionsexpress
Missing policy: ID: 305 Name: exceptionsexpress_url Description: HDFS url access policy for RW usecase group - exceptionsexpress
```
