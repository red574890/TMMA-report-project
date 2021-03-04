USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[posall]    Script Date: 2021/3/5 上午 07:10:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[posall]
AS   
exec Boxing_gloves;
exec legprotection;
exec helmet;
