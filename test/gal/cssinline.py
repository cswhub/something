import pygal
import css_inline  # 引入专门处理内联样式的库

# 1. 正常用 Pygal 生成带有 <style> 标签的原始 SVG
bar_chart = pygal.Bar(background="white")
bar_chart.title = "公众号测试图表"
bar_chart.add("数据系列", [10, 20, 30, 40])
raw_svg = bar_chart.render(disable_xml_declaration=True) # 获取原始的 SVG 字符串

# 2. 使用 css_inline 库一键将 CSS 转换为内联样式
# minify=True 可以顺便压缩代码，减小体积
inlined_svg = css_inline.inline(raw_svg)

# 3. 此时 inlined_svg 里的样式已经全部变成 style="..." 了
# 你可以顺手把不再需要的 <defs>...</defs> 模块清理掉
import re

final_svg = re.sub(r"<defs>.*?</defs>", "", inlined_svg, flags=re.DOTALL)

print(final_svg)
# 接下来直接把 final_svg 复制到 135 编辑器的 HTML 模式即可！
