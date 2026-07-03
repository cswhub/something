' Attribute VB_Name = "actions"
Sub chartupdate()
	Sheets("test").Cells(1, 3) = "S000000096"
	Sheets("test").Cells(2, 3).Formula = "=@thsMEDB(B4,""2000/09/18"","""",""Format(isAsc=N,Display=R,FillBlank=B,DecimalPoint=2,LineBlank=N)"")"
End Sub



Sub 普通图表(index, myenddate)
	tutext = Sheets("参数").Cells(index, 2)
	sheetname = Sheets("参数").Cells(index, 3)
	datestartrow = Sheets("参数").Cells(index, 4)
	ts = Sheets("参数").Cells(index, 6)
	
	
	
	
	' Sheets(sheetname).Select
	
	daterows = Sheets(sheetname).Cells(20000, 1).End(xlUp).Row
	
	For i = 2 To 10
		
		shujurows = Sheets(sheetname).Cells(20000, i).End(xlUp).Row
		If daterows - shujurows >= 10 Then
			Exit For
			
		End If
		
	Next i
	
	shujucount = i - 1
	
	shujulie = 代码转换(shujucount)
	
	'zuixinriqi = Sheets(sheetname).Range("A" & daterows)
	'kaishiriqi = VBA.DateAdd("d", -Sheets("参数").Cells(index, 4), zuixinriqi)
	
	
	For i = daterows To datestartrow Step - 1
		If Format(Sheets(sheetname).Cells(i, 1), "yyyymmdd") <= myenddate Then
			Exit For
		End If
	Next i
	jieshurow = i
	jieshuriqi = Sheets(sheetname).Cells(jieshurow, 1)
	
	kaishiriqi = VBA.DateAdd("d", - ts, jieshuriqi)
	
	For i = datestartrow To daterows
		If Format(Sheets(sheetname).Cells(i, 1), "yyyymmdd") >= Format(kaishiriqi, "yyyymmdd") Then
			Exit For
		End If
	Next i
	kaishirow = i
	
	
	
	Sheets("周报图表").ChartObjects(index - 1).Activate
	ActiveChart.SetSourceData Source : = Sheets(sheetname).Range("A" & kaishirow & ":" & shujulie & jieshurow)
	For i = 2 To shujucount
		xilielie = 代码转换(i)
		xilie = Sheets(sheetname).Cells(2, i)
		danwei = Sheets(sheetname).Cells(4, i)
		If Left(danwei, 2) = "ID" Then
			danwei = Sheets(sheetname).Cells(3, i)
		End If
		xiliedanwei = xilie '& "(" & danwei & ")"
		ActiveChart.FullSeriesCollection(i - 1).Name = xiliedanwei
	Next i
	ActiveChart.ChartTitle.Text = tutext & "（单位：" & danwei & "）"
End Sub

