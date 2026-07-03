from pywinauto import Application

app = Application(backend="uia").connect(
    title_re=".*网上交易.*", timeout=10#, control_type="Window"
)

# topw = app.top_window()
topw = app.window(
    title_re=".*网上交易.*"  # , control_type="Window"
)

# 假设你已经连接到了应用并获取了顶级窗口 topw
# 1. 精准定位到包含持仓数据的 Tree 控件
position_tree = (
    topw.child_window(
        control_type="Custom", found_index=2
    )  # 匹配有文字的Custom，自动跳过空的
    .child_window(control_type="Tree", found_index=2)
    .wait("ready", timeout=5)
)

print("成功锁定持仓表格！正在提取数据...")

# 2. 提取表头（所有的 Header 控件）
headers = position_tree.descendants(control_type="Header")
print(len(headers), "表头")
header_names = [h.window_text() for h in headers]
print(f"表头字段：{header_names}")

# 3. 提取具体的持仓数据（所有的 TreeItem 控件）
items = position_tree.descendants(control_type="TreeItem")
print(len(items), "表身")
data_list = [item.window_text() for item in items if item.window_text()]

# print(f"共抓取到 {len(data_list)} 个数据节点，前10个数据如下：")
# print(data_list[:10])
# 预期输出类似：['1', '格力电器', '000651', '1700', '1700', '39.710', ...]

col_count = len(header_names)
structured_data = []

# 按列数切片，将平铺的数据还原成一行行记录
for i in range(0, len(data_list), col_count):
    row_values = data_list[i : i + col_count]
    # zip 把表头和数据配对，dict 转成字典
    row_dict = dict(zip(header_names, row_values))
    structured_data.append(row_dict)

print(structured_data)
# 输出示例：[{'序号': '1', '证券名称': '格力电器', ...}, {...}]