import pygal
from pygal.style import Style

# 1. 模拟 OHLC 数据 (Open, High, Low, Close)
ohlc_data = [
    {"label": "Day 1", "o": 0, "h": 5, "l": -2, "c": 2},  # 阳
    {"label": "Day 2", "o": 0, "h": 1, "l": -3, "c": -1},  # 阴
    {"label": "Day 3", "o": 0, "h": 0, "l": -4, "c": -4},  # 阴
    {"label": "Day 4", "o": 0, "h": 2, "l": 0, "c": 1},  # 阳
]

# 准备三个序列的数据
series_bottom_wick = []  # 下影线序列
series_body = []  # 实体序列
series_top_wick = []  # 上影线序列

for k in ohlc_data:
    o, h, l, c = k["o"], k["h"], k["l"], k["c"]

    # 判断涨跌，确定实体颜色
    is_up = c >= o
    body_color = "#ef4444" if is_up else "#22c55e"  # 涨红跌绿

    # 计算三个部分的起始值和高度
    if is_up:  # 阳线：下影->实体->上影
        series_bottom_wick.append(
            {"value": l, "color": body_color}
        )  # 下影线借用实体颜色做边框
        series_body.append({"value": c - o, "color": body_color})
        series_top_wick.append({"value": h - c, "color": body_color})
    else:  # 阴线：下影->实体->上影
        series_bottom_wick.append({"value": l, "color": body_color})
        series_body.append({"value": o - c, "color": body_color})
        series_top_wick.append({"value": h - o, "color": body_color})

# 2. 自定义样式 (去掉默认的背景和网格，让 SVG 更干净)
custom_style = Style(
    background="transparent",
    plot_background="transparent",
    opacity=".6",
    colors=("#ef4444", "#22c55e"),  # 定义红绿配色
)

# 3. 创建堆叠柱状图
chart = pygal.StackedBar(
    style=custom_style,
    width=800,
    height=400,
    show_legend=False,  # 不需要图例
    show_x_labels=True,
    show_y_labels=False,  # 隐藏Y轴标签
    x_label_rotation=0,
    margin=20,
)
chart.x_labels = [k["label"] for k in ohlc_data]

# 4. 添加三个序列
# 注意：Pygal 的 fill=False 表示只画边框不填充颜色，完美符合你的需求！
chart.add("Bottom Wick", series_bottom_wick, fill=False, stroke_width=2)
chart.add("Body", series_body, fill=True, stroke_width=1)
chart.add("Top Wick", series_top_wick, fill=False, stroke_width=2)

# 5. 渲染并保存为纯 SVG 文件
chart.render_to_file("kline_chart.svg")
print("SVG 图表已生成：kline_chart.svg")
