USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[Ray_POS_Sales]    Script Date: 2021/3/5 上午 07:07:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER Procedure [dbo].[Ray_POS_Sales]
     @date1 date,
	 @date2 date
as

select
NEWadd.品號,
NEWadd.品名,
NEWadd.規格,
NEWadd.品號類別一,
MA1.MA003 as  '分類名稱一',
NEWadd.品號類別二,
isnull(MA2.MA003,'') as  '分類名稱二',
NEWadd.品號類別三,
isnull(MA3.MA003,'') as  '分類名稱三',
NEWadd.品號類別四,
isnull(MA4.MA003,'') as  '分類名稱四',
NEWadd.銷貨數量,
NEWadd.銷貨單未稅金額,
NEWadd.銷貨單稅額,
NEWadd.原幣銷退金額,
NEWadd.原幣銷退稅額,
NEWadd.銷退數量,
NEWadd.銷貨淨額,
NEWadd.銷貨單成本,
NEWadd.銷貨毛利,
NEWadd.[POS 未稅金額],
NEWadd.[POS 稅額],
NEWadd.POS總金額,
NEWadd.POS銷貨成本,
NEWadd.POS毛利,
NEWadd.[POS 銷售總數量],
NEWadd.商品銷貨總數量,
NEWadd.商品銷售總金額,
NEWadd.商品銷貨總成本,
NEWadd.商品銷貨總毛利,
NEWadd.商品銷貨毛利率


from
(

Select      
NEW.品號,
NEW.品名,
NEW.規格,
INVMB.MB005 as '品號類別一',
INVMB.MB006 as '品號類別二',
INVMB.MB007 as '品號類別三',
INVMB.MB008 as '品號類別四',
NEW.銷貨數量,
NEW.銷貨單未稅金額,
NEW.銷貨單稅額,
NEW.原幣銷退金額,
NEW.原幣銷退稅額,
NEW.銷退數量,
NEW.銷貨淨額,
NEW.銷貨單成本,
NEW.銷貨毛利,
NEW.[POS 未稅金額],
NEW.[POS 稅額],
NEW.POS總金額,
NEW.POS銷貨成本,
NEW.POS毛利,
NEW.[POS 銷售總數量],
NEW.商品銷貨總數量,
NEW.商品銷售總金額,
NEW.商品銷貨總成本,
NEW.商品銷貨總毛利,
NEW.商品銷貨毛利率
from (
select  CC.品號,
        CC.品名,
		CC.規格,
		CC.銷貨數量,
		CC.銷貨單未稅金額,
		CC.銷貨單稅額,
		isnull(TJ.原幣銷退金額,0) as '原幣銷退金額' ,
		isnull(TJ.原幣銷退稅額,0) as '原幣銷退稅額' ,
		isnull(TJ.銷退數量,0) as '銷退數量',
		CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)+CC.銷貨單稅額+isnull(TJ.原幣銷退稅額,0) AS '銷貨淨額'　,　-- SALE MINUS SALE RETURN 
		isnull(LA.銷貨成本,0) as '銷貨單成本',
		(CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)-isnull(LA.銷貨成本,0)) as '銷貨毛利',
		CC.[POS 未稅金額],
		CC.[POS 稅額],
		CC.POS總金額,
		isnull(PO.POS成本,0) as 'POS銷貨成本',
		CC.[POS 未稅金額]-isnull(PO.POS成本,0) as 'POS毛利',
	    CC.[POS 銷售總數量],
		CC.[POS 銷售總數量]+CC.銷貨數量 as '商品銷貨總數量',
		CC.POS總金額+CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)+CC.銷貨單稅額+isnull(TJ.原幣銷退稅額,0) as '商品銷售總金額',
		isnull(PO.POS成本,0)+isnull(LA.銷貨成本,0) as '商品銷貨總成本',
		((CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)-isnull(LA.銷貨成本,0))+CC.[POS 未稅金額]-isnull(PO.POS成本,0))  as '商品銷貨總毛利',
		isnull((((CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)-isnull(LA.銷貨成本,0))+CC.[POS 未稅金額]-isnull(PO.POS成本,0)) /NULLIF((CC.銷貨單未稅金額+isnull(TJ.原幣銷退金額,0)+CC.[POS 未稅金額]),0)),0)*100 as '商品銷貨毛利率'
--select isnull(1/nullif(0,0),0);
from (
select AA.productID as '品號',AA.品名,AA.規格,isnull(AA.[sale amount],0) as '銷貨數量',isnull([sale COPTG],0) as '銷貨單未稅金額',
isnull(AA.[Tax COPTG],0) as '銷貨單稅額',
isnull(F.未稅金額,0) as 'POS 未稅金額',isnull(F.稅額,0) as 'POS 稅額',
isnull(F.未稅金額,0)+isnull(F.稅額,0) as 'POS總金額',
isnull(F.[POS sales number],0) as 'POS 銷售總數量',
isnull([sale COPTG],0)+isnull(AA.[Tax COPTG],0)+isnull(F.未稅金額,0)+isnull(F.稅額,0) as '總金額'
 from (
   select INVMB.MB001 as 'productID',
          INVMB.MB002 as '品名',
    INVMB.MB003 as '規格',
       P.[sale COPTG],
    P.[Tax COPTG],
	P.[sale amount]
    from (select INVMB.MB001 as 'productID',
       sum( TH037)as 'sale COPTG',
    sum(TH038) as 'Tax COPTG' ,
	sum(TH008) as  'sale amount'

    from ((COPTH inner join COPTG A on COPTH.TH001+COPTH.TH002= A.TG001+A.TG002))
    right outer join INVMB on INVMB.MB001 = COPTH.TH004
    where TG003 >= @date1 and TG003<=@date2　and TG023='Y' --20190813 add confirmation
    group by  INVMB.MB001)P
    right outer join INVMB on INVMB.MB001 = P.productID
    group by  INVMB.MB001,INVMB.MB002,INVMB.MB003,P.[sale COPTG],P.[Tax COPTG],P.[sale amount])AA
    left join (select MB001 as '品號',
 D.[Sales amount] as '未稅金額',
 D.Tax1  as '稅額',
 D.[POS sales number]
 from (
 select MB001 as 'product.id',
 sum(TP019) as'Sales amount',
 sum(TP020) as 'Tax1',
 SUM(TP008) AS 'POS sales number'
 from INVMB 
 left join POSTP on INVMB.MB001=POSTP.TP004
 where TP001 >= @date1 and TP001 <= @date2 
 group by INVMB.MB001)D
 right join INVMB on INVMB.MB001=D.[product.id]
 group by MB001, D.[Sales amount], D.Tax1,D.[POS sales number])F
       on AA.productID=F.品號

 group by   AA.[sale COPTG],  AA.[Tax COPTG] , F.未稅金額, F.稅額, AA.productID,AA.規格,AA.品名,AA.[sale amount],F.[POS sales number]
 Having AA.[sale COPTG] is not Null or AA.[Tax COPTG]  is not null or F.未稅金額 is not null or F.稅額 is not null)CC

 left join (
 select INVMB.MB001 as 'productID',
-sum(COPTJ.TJ033) as '原幣銷退金額',
-sum(COPTJ.TJ034)　as'原幣銷退稅額',
sum(COPTJ.TJ007)  as'銷退數量'
from COPTJ
inner join COPTI as A on TJ001= TI001 and TJ002 = TI002
left join INVMB on INVMB.MB001=COPTJ.TJ004 
where COPTJ.TJ021='Y' and A.TI003 >= @date1 and  A.TI003 <= @date2
group by INVMB.MB001) TJ on TJ.productID=CC.品號

left join (select LA001 , sum(LA013) as '銷貨成本' 
       from INVLA as INV
	   inner join COPTH as COP on COP.TH001 = INV.LA006 and COP.TH002 = INV.LA007 and COP.TH003 = INV.LA008
	   where LA004 >= @date1 and LA004 <= @date2
	   group by LA001)LA on LA.LA001=CC.品號

left join(select LA001 , sum(LA013) as 'POS成本'
       from INVLA as INV 
	   where TRANS_NAME='POSB26' and LA004 >= @date1 and LA004 <= @date2
	   group by LA001)PO on PO.LA001=CC.品號
	   
	   )NEW    left join INVMB  on MB001 = NEW.品號)NEWadd   
	 
	 left join  (select MA002,MA003 from INVMA where MA001='1')MA1 on NEWadd.品號類別一 = MA1.MA002
	 left join  (select MA002,MA003 from INVMA where MA001='2')MA2 on NEWadd.品號類別二 = MA2.MA002
	 left join  (select MA002,MA003 from INVMA where MA001='3')MA3 on NEWadd.品號類別三 = MA3.MA002
	 left join  (select MA002,MA003 from INVMA where MA001='4')MA4 on NEWadd.品號類別四 = MA4.MA002;;
