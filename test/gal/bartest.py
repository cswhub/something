import pygal

# 创建堆叠柱状图
stacked_chart = pygal.StackedBar(
    width=800,
    height=300,
    show_legend=False,
    js=["pygal-tooltips.min.js"],
)
stacked_chart.title = "满足两个定制需求的堆叠图"
stacked_chart.x_labels = ["苹果", "香蕉", "橙子"]

# --- 需求二：中间序列按要求指定红色和绿色 ---
# 直接在每个数据里用 color 指定它自己的填充色
middle_data = [
    {"value": 30,"style": "fill: #ef4444; stroke: #ef4444; stroke-width: 11;",}, 
    {"value": -10, "style": "fill: #22c55e; stroke: #22c55e; stroke-width: 11;"},
    # {"value": -40, "color": "#22c55e"},  # 香蕉 -> 绿色
    {"value": 35,"style": "fill: #ef4444; stroke: #ef4444; stroke-width: 11;",}, 
]
stacked_chart.add("中间(红绿变色)", middle_data)

# 顶部序列保持默认即可（作为对比）
top_data = [
    {"value": 15, "style": "fill: none; fill-opacity: 100%; stroke: #ef4444; stroke-width: 11;"},
    {"value": 30, "style": "fill: none; stroke: #ef4444; stroke-width: 11;"},
    {"value": 10, "style": "fill: none; stroke: #ef4444; stroke-width: 11;"},
]
stacked_chart.add("顶部", top_data)

bottom_data = [
    {"value": -10, "style": "fill: none; stroke: #22c55e; stroke-width: 11;"},
    {"value": -20, "style": "fill: none; stroke: #22c55e; stroke-width: 11;"},
    {"value": -15, "style": "fill: none; stroke: #22c55e; stroke-width: 11;"},
]
stacked_chart.add("底部(绿框空心)", bottom_data, stroke_color="#080808")



# 渲染保存
# stacked_chart.render_to_file("custom_stacked.svg")
svg_code = stacked_chart.render(disable_xml_declaration=True)
print(svg_code)
with open("bar.html", "w", encoding="utf-8") as f:
    f.write(svg_code)
print("成功！请查看 custom_stacked.svg")
