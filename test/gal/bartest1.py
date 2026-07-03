import pygal

# 实例化一个横向堆叠条形图对象
bar_chart = pygal.HorizontalStackedBar()

# 设置图表标题和X轴标签（可选）
bar_chart.title = "横向堆叠条形图示例"
bar_chart.x_labels = ["类别A", "类别B", "类别C"]

# 添加数据系列
bar_chart.add("系列1", [10, 20, 30])
bar_chart.add("系列2", [15, 25, 35])

# 将图表渲染并保存为SVG文件
bar_chart.render_to_file("horizontal_stacked_bar.svg")
