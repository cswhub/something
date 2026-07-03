from pywinauto import Application

app = Application(backend="uia").connect(
    title_re=".*网上交易.*", timeout=10#, control_type="Window"
)

# topw = app.top_window()
mainwin = app.window(title_re=".*网上交易.*"#, control_type="Window"
)
# print(topw.window_text())
all_children = mainwin.descendants()

print(f"顶级窗口下共有 {len(all_children)} 个子/后代控件，详细信息如下：")
for i, child in enumerate(all_children):
    # 获取控件的核心元素信息对象
    element_info = child.element_info

    text = child.window_text()
    control_type = element_info.control_type  # 控件类型 (如 Button, Pane, DataItem)
    # class_name = element_info.class_name  # 控件的底层类名
    # auto_id = element_info.automation_id  # 自动化ID (现代UI应用常用来精准定位)
    # visible = element_info.visible  # 控件是否可见 (True/False)
    # enabled = element_info.enabled  # 控件是否可用/可点击 (True/False)
    # rect = element_info.rectangle  # 控件在屏幕上的坐标和大小

    print(f"\n--- 第 {i} 个控件 ---")
    print(f"文字: {text}")
    print(f"控件类型(control_type): {control_type}")
    # print(f"类名(class_name): {class_name}")
    # print(f"自动化ID(auto_id): {auto_id}")
    # print(f"是否可见(visible): {visible} | 是否可用(enabled): {enabled}")
    # print(f"屏幕坐标(rectangle): {rect}")


# topw = topw.child_window()
# print(topw)




