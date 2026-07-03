遍历组件树
main_window.print_control_identifiers()


只是一个子窗口定位器，并不是求所有子窗口，如果找到多个会报错，需要加found_index=1
topw.child_window()


这个是找到所有符合条件的子孙元素集合，而.children()是找到直接儿子的元素集合
all_position_items = topw.descendants(control_type="TreeItem")
print(f"\n✅ 成功在全局抓取到 {len(all_position_items)} 条持仓数据节点！内容如下：")
for i, item in enumerate(all_position_items):
    text = item.window_text()
    # 过滤掉可能存在的空节点
    if text:
        print(f"{i}: {text}")



.parent()：获取父级容器
.children() / .descendants()：获取子级或所有后代


输入文本可以用set_text或者使用下面的方法模拟输入
edit.set_text("")          # 先清空原有内容
edit.click_input()         # 鼠标真实点击一下，让输入框获取焦点
edit.type_keys("600519")   # 再用模拟键盘的方式输入

