# Taipei Mixed Martial Art Project

## Background
After I finished implementing the ERP system for this company in May, 2018, TMMA asked me to add several extra functions, including report and batch processing. 

After adding five new functions, executing individual code started to become tedious. 

Therefore, I created an application to organize all the extra functions to be more productive.

This project spent around 10 months and eventually they can fully utilize ERP sytem.


## File introduction
### [1. TMMAinfo.txt](https://github.com/red574890/TMMA-report-project/blob/main/TMMAinfo/TMMAinfo.txt)
This file works as a config file. It records the following information for the MSSQL database.

serverid      &nbsp;&nbsp;&nbsp;&nbsp;   __*// SQL server id*__

user           &nbsp;&nbsp;&nbsp;&nbsp;   __*// SQL user account*__

passward      &nbsp;&nbsp;&nbsp;&nbsp;    __*// SQL account*__

database      &nbsp;&nbsp;&nbsp;&nbsp;     __*// target database*__

apploginpwd    &nbsp;&nbsp;&nbsp;&nbsp;    __*// the password to login into this application. (They need some safety control)*__

fontpath      &nbsp;&nbsp;&nbsp;&nbsp;    __*// for special font*__

outputpath     &nbsp;&nbsp;&nbsp;&nbsp;   __*// sometimes their staff need to create some plots by themselves. So this path where output excel file will go*__

### [2. TMMA.py](https://github.com/red574890/TMMA-report-project/blob/main/login/TMMA.py)
This file is a login interface.


### [3. TMMA_program.py](https://github.com/red574890/TMMA-report-project/blob/main/main_code/TMMA_program.py)
This file is for all the logic and commend for the application.

### [4. All the .sql](https://github.com/red574890/TMMA-report-project/tree/main/SQLcode)
I created a lot of store procedures in the database. Those .sql files are to call those store procedures when they click certain buttons.
1. Buyonegetonefree.sql  &nbsp;&nbsp;&nbsp;&nbsp; __*// Automatically insert cretain genre of products to a buy one get on free table*__

2. Adjustmin.sql        &nbsp;&nbsp;&nbsp;&nbsp;   __*// Automatically adjust the POS system's price of certain product*__

3. posall.sql          &nbsp;&nbsp;&nbsp;&nbsp;  __*// Automatically insert cretain genre of products to a pos buy one get on free table*__

4. All the store procedure will be put in [All store procedures!](https://github.com/red574890/TMMA-report-project/tree/main/SQLcode/all%20store%20procedures)


## Check here to see the [Application Instruction!](https://github.com/red574890/TMMA-report-project/blob/main/interface_guide/interface_guide.md)

