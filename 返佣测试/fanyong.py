
from excel_manage import ExcelManage

targethearderlist = ['营销人员营业部', '营销人员编号', '营销人员', '客户号', '客户姓名', '期末权益', '日均权益', '总盈亏', '净手续费', '返还比例', '返还金额']

excel = ExcelManage("raw/营销人员资金返佣明细.xlsx", read_only=True)

excel.sheet("Sheet1")


sheet_content = excel.read_ws()
headers = sheet_content[0]

if list(headers) != targethearderlist:
    raise RuntimeError("请查看字段是否正确")

datas = sheet_content[1:]

# excel_data_dict = [dict(zip(headers, row)) for row in datas]


datadict= {}

lastdepartment = ""
for d in datas:
    if d[8] < 0:
        d[8] = 0
        d[10] = 0
    if d[0] not in datadict:
        datadict[d[0]] = {}
    if d[2] not in datadict[d[0]]:
        datadict[d[0]][d[2]] = []
    if d[0] == '小计':
        datadict[lastdepartment][d[2]].append(d)
    datadict[d[0]][d[2]].append(d)
    lastdepartment = d[0]









