import pygal
# 引入一个自带的漂亮主题（比如清爽的浅色风格）
from pygal.style import Style

# 自定义一个主色调（比如科技蓝）
custom_style = Style(


    colors=(
        "#E80080",
        "#404040",
        "#9BC850",
        "#F0A830",
    ),  # 依次对应第一条线、第二条线...的颜色
)

# 创建折线图对象，直接套用主题
line_chart = pygal.Line(
    style=custom_style,
    width=400,
    height=300,
    js=["pygal-tooltips.min.js"],
    show_dots=False,
    legend_at_bottom=True,
)
line_chart.title = '期货季节性价格走势分析' # 标题
line_chart.x_labels = ['1月', '2月', '3月', '4月', '5月', '6月']

# 添加数据，自带鼠标悬停交互
line_chart.add('螺纹钢2024', [3800, 3900, 4100, 4200, 4000, 3950])
line_chart.add('螺纹钢2025', [3850, 3950, 4050, 4150, 4050, 4000])

# 直接把 SVG 代码渲染成字符串！
# 你可以把这个 svg_code 直接塞进你的 Jinja2 模板，或者通过 API 传给前端
svg_code = line_chart.render(disable_xml_declaration=True)
print(svg_code) 
with open("test.html", "w", encoding="utf-8") as f:
    f.write(svg_code)

