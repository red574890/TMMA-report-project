USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[Three_months_no_transaction]    Script Date: 2021/3/5 上午 07:04:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER Procedure [dbo].[Three_months_no_transaction]
     @date1 date,
	 @date2 date

as

select 
        temp3.品名,
        temp3.品號,
		temp3.品號類別一,
		temp3.品號類別一名稱, 
		temp3.品號類別二, 
		temp3.品號類別二名稱, 
		temp3.品號類別三, 
		temp3.品號類別三名稱, 
		temp3.品號類別四, 
		temp3.品號類別四名稱,
		temp3.備註,
		temp3.單別,
		temp3.單號,
		temp3.最近銷售日期,
		isnull(temp4.LA004,'沒進過') as '最近進貨日期'
	

from
(
select  temp.品名,
        temp.品號,
		temp.品號類別一,
		temp.品號類別一名稱, 
		temp.品號類別二, 
		temp.品號類別二名稱, 
		temp.品號類別三, 
		temp.品號類別三名稱, 
		temp.品號類別四, 
		temp.品號類別四名稱,
		isnull(temp2.LA004,'沒賣過') as '最近銷售日期',
		isnull(temp2.LA010,'沒賣過') as '備註',
		isnull(temp2.LA006,'沒賣過') as '單別',
		isnull(temp2.LA007,'沒賣過') as '單號'
		from (
select I.MB001 as '品號',I.MB002 as '品名',I.MB005 as '品號類別一',isnull(I.name1,'') as '品號類別一名稱',isnull(I.MB006,'') as  '品號類別二', isnull(I.name2,'') as '品號類別二名稱', isnull(I.MB007,'') as   '品號類別三',isnull(I.name3,'') as '品號類別三名稱',I.MB008 as '品號類別四',isnull(J.MA002,'') as '品號類別四名稱' from (
select  G.MB001 ,G.MB002,G.MB005,G.name1,G.MB006,G.name2,G.MB007,H.MA003 as 'name3', G.MB008  from

(select D.MB001,D.MB002,D.MB005,D.MA003 as 'name1',D.MB006,E.MA003 as 'name2',D.MB007,D.MB008 from (

select A.MB001,A.MB002,A.MB005,B.MA003,A.MB006,A.MB007,A.MB008 from (

 select MB001,MB002,MB005,MB006,MB007,MB008  from INVMB 
 left join  (select LA001,LA002,LA006 from INVLA where LA014='2' and LA004> @date1 and  LA004< @date2) as A
 on INVMB.MB001 = A.LA001
  where MB019='Y' and MB064 > 0 and INVMB.CREATE_DATE <=@date2 and  A.LA001 is null
 ) as A
 left join (select MA001, MA002 ,MA003 from INVMA where MA001='1') as B

 on A.MB005 = B.MA002
 ) as D

 left join (select MA001, MA002 ,MA003 from INVMA where MA001='2') as E on D.MB006 = E.MA002) as G 
 left join (select MA001, MA002 ,MA003 from INVMA where MA001='3') as H on G.MB007 = H.MA002) as I
 left join  (select MA001, MA002,MA003 from INVMA where MA001='4') as J on I.MB008 = J.MA002) as temp
 left join (select R.LA001, R.LA004, R.LA010,R.LA006,R.LA007 from  (
select LA001, LA004, LA010,LA006,LA007, ROW_NUMBER() OVER(PARTITION BY LA001 ORDER BY LA004 desc) as rn from INVLA
where  LA014 = '2' 
group by LA001,LA004, LA010,LA006,LA007)R

where rn='1') as temp2 on temp.品號 = temp2.LA001)temp3

left join  (select M.LA001, M.LA004, M.LA010,M.LA006,M.LA007 from  (
select LA001, LA004, LA010,LA006,LA007, ROW_NUMBER() OVER(PARTITION BY LA001 ORDER BY LA004 desc) as rn from INVLA
where  LA014 = '1'  or LA014='5' and LA005 = '1'
group by LA001,LA004, LA010,LA006,LA007)M where rn='1') as temp4 on temp3.品號 = temp4.LA001
