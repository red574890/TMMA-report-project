# Taipei Mixed Martial Art Project

## Background
After I finished implementing the ERP system for this company. They asked me to add in several extra functions, including report and batch processing. 
After 5 new functions, executing individul code started to become tedious. 
Therefore, I created a application to organize all the extra functions so that they can be more productive.


## file introduction
### 1. TMMAinfo.txt
This file works as a config file. It records the following information for MSSQL database.
serverid           // SQL server id

user               // SQL user account

passward           // SQL account

database           // target database

apploginpwd        // the password to login into this application. (They need some safety control)

fontpath           // for special font

outputpath         // sometimes their staff need to create some plots by themselves. So this path where output excel file will go

### 2. TMMA.py
This file is a login interface.


### 3. TMMA_program.py
This file is for all the logic and commend for the application.

### 4. All the .sql
I created a lot of store procedures in the database. Those .sql files are to call those store procedures when they click certain buttons.
1. Buyonegetonefree.sql    // Automatically insert cretain genre of products to a buy one get on free table
2. Adjustmin.sql           // Automatically adjust the POS system's price of certain product
3. posall.sql              // Automatically insert cretain genre of products to a pos buy one get on free table



