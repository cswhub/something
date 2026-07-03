
from excel_manage import ExcelManage



excel = ExcelManage("raw/营销人员资金返佣明细.xlsx", read_only=True)
excel.sheet("Sheet1")


sheet_content = excel.read_ws()
headers = sheet_content[0]
datas = sheet_content[1:]

# excel_data_dict = [dict(zip(headers, row)) for row in datas]

print(headers)


data= {}

lastdepartment = ""
for d in datas:
    if d[0] not in data:
        data[d[0]] = {}

print(data)



