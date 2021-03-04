USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[Adjustpr3]    Script Date: 2021/3/5 上午 07:02:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Adjustpr3]
as
declare 
@TotalNum numeric,
@Num numeric,
@productID varchar(40),
@discount_rate numeric(15,6),  
@evencode varchar(10),    --活動代號 @discountcode varchar(12)
@discountcode varchar(12)   --特價代號

select @TotalNum = count(*) from
(select B.eventcode, B.MI003, MB001, MB055 as MainDisrate, B.mdisrate  from INVMB as A 

      inner join   (select MI001 as eventcode, MI003, POSMJ.MJ004 as itemNum , MI009 as mlevel , MI020 as mdisrate from POSMI 
       inner join POSMJ on POSMI.MI003 = POSMJ.MJ003
      where MI001='123' and MI009 = '3') as B on  A.MB001 = B.itemNum)C

where C.MainDisrate <> C.mdisrate


set @Num = 1


WHILE @Num <= @TotalNum  --當目前次數小於等於執行次數
Begin
select Top 1 @evencode = C.eventcode, @discountcode = C.MI003, @discount_rate = C.MainDisrate from
(select B.eventcode, B.MI003, MB001, MB055 as MainDisrate, B.mdisrate  from INVMB as A 

      inner join   (select MI001 as eventcode, MI003, POSMJ.MJ004 as itemNum , MI009 as mlevel , MI020 as mdisrate from POSMI 
       inner join POSMJ on POSMI.MI003 = POSMJ.MJ003
       where MI001='123' and MI009 = '3') as B on  A.MB001 = B.itemNum)C

where C.MainDisrate <> C.mdisrate

-- 更新
update POSMI

set MI020 = @discount_rate, MI015 = 'N' 
where MI001 = @evencode and MI003 = @discountcode and MI009 = '3'


set @Num=@Num+1
END;


