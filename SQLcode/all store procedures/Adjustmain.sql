USE [TMMA_MAIN]
GO
/****** Object:  StoredProcedure [dbo].[Adjustmain]    Script Date: 2021/3/5 上午 07:03:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Adjustmain]
as
exec Adjustpr1;
exec Adjustpr2;
exec Adjustpr3;
