USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[legprotection]    Script Date: 2021/3/5 上午 07:09:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[legprotection]
as
DECLARE  
@TotalNum INT, --執行次數
@Num INT,       --目前次數
@CC  int,
@date1 varchar(10),
@date2 varchar(10),
@createdate varchar(10),
@createtime varchar(8),
@productID varchar(40),
@pruductName varchar(60),
@pruductSpec varchar(60),
@pruductUnit varchar(4),
@productprice numeric(15,6),
@Gift1 varchar(40),
@GiftName1 varchar(60),
@GiftSpec1  varchar(60),
@GiftUnit1  varchar(4),
@Gift2 varchar(40),
@GiftName2 varchar(60),
@GiftSpec2  varchar(60),
@GiftUnit2  varchar(4),
@Gift3 varchar(40),
@GiftName3 varchar(60),
@GiftSpec3  varchar(60),
@GiftUnit3  varchar(4),
@Gift4 varchar(40),
@GiftName4 varchar(60),
@GiftSpec4  varchar(60),
@GiftUnit4  varchar(4),
@CodeDate varchar(15),
@snum      INT,
@eventcode   varchar(10),
@discount_membership numeric(10,6),   --20200212新增會員折扣
@discount_employee numeric(10,6),     --20200212新增員工折扣 
@discount_venter numeric(10,6)        --20200212新增經銷商折扣

select @TotalNum=count(MB001)  from INVMB 
left join POSMJ on POSMJ.MJ004=INVMB.MB001
where MB007='009' and MJ004 is null ;

--售價定價二 MB054 學員  三 MB055 員工 四 MB056 經銷

--設定迴圈參數

SET @Num =1;        --目前次數 
set @CC=100000;
set @date1='20190424';
set @date2='22000830';
set @createdate=  Convert(varchar(10),Getdate(),112);
set @Gift1='0103002400028'
set @Gift2='0103002400035'
--set @Gift3='AA00008'
--set @Gift4='AD000001'
set @createtime=  substring(convert(varchar(20),getdate(),113),11,9);
set @eventcode = '123'


--select @GiftName1=MB002,@GiftSpec1=MB003,@GiftUnit1=MB004 from INVMB where MB001=@Gift1;

--select @GiftName2=MB002,@GiftSpec2=MB003,@GiftUnit2=MB004 from INVMB where MB001=@Gift2;

--select @GiftName3=MB002,@GiftSpec3=MB003,@GiftUnit3=MB004 from INVMB where MB001=@Gift3;

--select @GiftName4=MB002,@GiftSpec4=MB003,@GiftUnit4=MB004 from INVMB where MB001=@Gift4;

--執行WHILE迴圈
WHILE @Num <= @TotalNum  --當目前次數小於等於執行次數
BEGIN 


select @snum = IIF(MAX(C.B) is null,1,MAX(C.B)) from (
SELECT   substring(MI003,1,6) as A , max(convert(int,substring(MI003,7,11))) as B
from POSMI 
where  substring(MI003,1,6)=  substring(Convert(varchar(10),Getdate(),112),1,6)
group by MI003 )C ;

set @CodeDate= substring(Convert(varchar(10),Getdate(),112),1,6)+ IIF(@snum+1 < 10,'00000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=10 and @snum+1 <100),'0000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=100 and @snum+1 <=999),'000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=1000 and @snum+1 <=9999),'00'+convert(varchar(5),@snum+1),IIF((@snum+1 >=10000 and @snum+1 <=99999),'0'+convert(varchar(5),@snum+1),IIF((@snum+1 >=100000 and @snum+1 <=999999),convert(varchar(6),@snum+1),'XXX'))))));




    select top 1  @productID= MB001,
                 @pruductName=MB002,
                 --@pruductSpec=MB003,刪除不須選取 
                 --@pruductUnit=MB004,刪除不須選取
                 --@productprice=MB051,刪除不須選取
                 @discount_membership= MB054,   --20200210新增
                 @discount_employee = MB055,    --20200210新增
                 @discount_venter = MB056       --20200210新增
                 from INVMB left join POSMJ on POSMJ.MJ004=INVMB.MB001 where MB007='009' and MJ004 is null ;



    
  -- 一般學員會員  會員等級 1
  insert into POSMI
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, 
CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup,
 MI001, MI002, MI003, MI004, MI005, MI006, MI007, MI008, MI009, MI010, MI011, MI012, MI013, MI014, MI015, MI016, MI017, 
MI018, MI019, MI020, MI021, MI022, MI023, MI024, MI025, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ('TMMA_MAIN','DS','DS',@createdate,'','',1,@createtime,'','P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate,'護腳促銷一般會員',@date1,@date2,@createdate,'2','1','','','','1',@createdate,'Y','DS',0,0,1,@discount_membership,'N','N','N','Y','N','','','','','',0,0,0,0,0)

  insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.0.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.3.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.5.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)


  insert into POSMJ
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup, MJ001, MJ002, MJ003, MJ004, MJ005, MJ006, MJ007, MJ013, MJ015, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ( 'TMMA_MAIN','DS','DS',@createdate,'DS',@createdate,0,@createtime,@createtime,'P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate, @productID,1,'Y','',1,'0001','','','','','',0,0,0,0,0)

 insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.0.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
  insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.3.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.5.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift1 ,'1',1,0,0,'0001')

insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift2 ,'1',1,0,0,'0002')



-- 經銷商會員  會員等級 2
set @snum=@snum+1
set @CodeDate=substring(Convert(varchar(10),Getdate(),112),1,6)+ IIF(@snum+1 < 10,'00000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=10 and @snum+1 <100),'0000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=100 and @snum+1 <=999),'000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=1000 and @snum+1 <=9999),'00'+convert(varchar(5),@snum+1),IIF((@snum+1 >=10000 and @snum+1 <=99999),'0'+convert(varchar(5),@snum+1),IIF((@snum+1 >=100000 and @snum+1 <=999999),convert(varchar(6),@snum+1),'XXX'))))));

 insert into POSMI
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, 
CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup,
 MI001, MI002, MI003, MI004, MI005, MI006, MI007, MI008, MI009, MI010, MI011, MI012, MI013, MI014, MI015, MI016, MI017, 
MI018, MI019, MI020, MI021, MI022, MI023, MI024, MI025, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ('TMMA_MAIN','DS','DS',@createdate,'','',1,@createtime,'','P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate,'護腳促銷經銷商',@date1,@date2,@createdate,'2','2','','','','1',@createdate,'Y','DS',0,0,1,@discount_venter,'N','N','N','Y','N','','','','','',0,0,0,0,0)

  insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.0.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.3.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.5.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)


  insert into POSMJ
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup, MJ001, MJ002, MJ003, MJ004, MJ005, MJ006, MJ007, MJ013, MJ015, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ( 'TMMA_MAIN','DS','DS',@createdate,'DS',@createdate,0,@createtime,@createtime,'P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate, @productID,1,'Y','',1,'0001','','','','','',0,0,0,0,0)

 insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.0.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
  insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.3.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.5.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift1 ,'1',1,0,0,'0001')

insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift2 ,'1',1,0,0,'0002')



-- 員工會員  會員等級 3

set @snum=@snum+1
set @CodeDate= substring(Convert(varchar(10),Getdate(),112),1,6)+ IIF(@snum+1 < 10,'00000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=10 and @snum+1 <100),'0000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=100 and @snum+1 <=999),'000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=1000 and @snum+1 <=9999),'00'+convert(varchar(5),@snum+1),IIF((@snum+1 >=10000 and @snum+1 <=99999),'0'+convert(varchar(5),@snum+1),IIF((@snum+1 >=100000 and @snum+1 <=999999),convert(varchar(6),@snum+1),'XXX'))))));

 insert into POSMI
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, 
CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup,
 MI001, MI002, MI003, MI004, MI005, MI006, MI007, MI008, MI009, MI010, MI011, MI012, MI013, MI014, MI015, MI016, MI017, 
MI018, MI019, MI020, MI021, MI022, MI023, MI024, MI025, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ('TMMA_MAIN','DS','DS',@createdate,'','',1,@createtime,'','P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate,'護腳促銷員工',@date1,@date2,@createdate,'2','3','','','','1',@createdate,'Y','DS',0,0,1,@discount_employee,'N','N','N','Y','N','','','','','',0,0,0,0,0)

  insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.0.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.3.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.5.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)


  insert into POSMJ
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup, MJ001, MJ002, MJ003, MJ004, MJ005, MJ006, MJ007, MJ013, MJ015, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ( 'TMMA_MAIN','DS','DS',@createdate,'DS',@createdate,0,@createtime,@createtime,'P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate, @productID,1,'Y','',1,'0001','','','','','',0,0,0,0,0)

 insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.0.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
  insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.3.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.5.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift1 ,'1',1,0,0,'0001')

insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift2 ,'1',1,0,0,'0002')

-- 沒有會員 

set @snum=@snum+1
set @CodeDate=substring(Convert(varchar(10),Getdate(),112),1,6)+ IIF(@snum+1 < 10,'00000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=10 and @snum+1 <100),'0000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=100 and @snum+1 <=999),'000'+convert(varchar(4),@snum+1),IIF((@snum+1 >=1000 and @snum+1 <=9999),'00'+convert(varchar(5),@snum+1),IIF((@snum+1 >=10000 and @snum+1 <=99999),'0'+convert(varchar(5),@snum+1),IIF((@snum+1 >=100000 and @snum+1 <=999999),convert(varchar(6),@snum+1),'XXX'))))));

 insert into POSMI
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, 
CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup,
 MI001, MI002, MI003, MI004, MI005, MI006, MI007, MI008, MI009, MI010, MI011, MI012, MI013, MI014, MI015, MI016, MI017, 
MI018, MI019, MI020, MI021, MI022, MI023, MI024, MI025, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ('TMMA_MAIN','DS','DS',@createdate,'','',1,@createtime,'','P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate,'護腳促銷',@date1,@date2,@createdate,'2','','','','','1',@createdate,'Y','DS',0,0,1,1,'N','N','N','Y','N','','','','','',0,0,0,0,0)

  insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.0.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.3.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)

   insert into LOG_POSMI
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MI001,MI002,MI003)
  values
  ('2',@createdate,@createtime,'192.168.5.9',@createdate,'','N','0', @eventcode,'4', @CodeDate)


  insert into POSMJ
  (COMPANY, CREATOR, USR_GROUP, CREATE_DATE, MODIFIER, MODI_DATE, FLAG, CREATE_TIME, MODI_TIME, TRANS_TYPE, TRANS_NAME, sync_date, sync_time, sync_mark, sync_count, DataUser, DataGroup, MJ001, MJ002, MJ003, MJ004, MJ005, MJ006, MJ007, MJ013, MJ015, UDF01, UDF02, UDF03, UDF04, UDF05, UDF06, UDF07, UDF08, UDF09, UDF10)
values
  ( 'TMMA_MAIN','DS','DS',@createdate,'DS',@createdate,0,@createtime,@createtime,'P001','POSI05','','','',0,'','DS',@eventcode,'4', @CodeDate, @productID,1,'Y','',1,'0001','','','','','',0,0,0,0,0)

 insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.0.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
  insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.2.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.3.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')

  
    insert into LOG_POSMJ
  (TRS_CODE,TRS_DATE,TRS_TIME,store_ip,sync_date,sync_time,sync_mark,sync_count,MJ001,MJ002,MJ003,MJ004,MJ015)
  values
  ('2',@createdate,@createtime,'192.168.5.9','','','N','0',@eventcode,'4',@CodeDate,@productID,'0001')


insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift1 ,'1',1,0,0,'0001')

insert into POSMK
  (CREATE_DATE, MK001, MK002, MK003, MK004, MK005, MK006, MK007, MK008, MK017)
values
  (@createdate,@eventcode,'4', @CodeDate, @Gift2 ,'1',1,0,0,'0002')


 SET @Num = @Num + 1
END
