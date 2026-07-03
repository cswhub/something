from pywinauto import Application

app = Application(backend="uia").connect(
    title_re=".*网上交易.*",
    timeout=10,  # , control_type="Window"
)

# topw = app.top_window()
mainwin = app.window(
    title_re=".*网上交易.*"  # , control_type="Window"
)
# print(topw.window_text())
all_children = mainwin.descendants()

print(len(all_children))

if len(all_children) <= 10:
    print("已锁定，需要输入密码")
    edit = mainwin.child_window(control_type="Edit")
    # edit.set_text("")          # 先清空原有内容
    edit.click_input()         # 鼠标真实点击一下，让输入框获取焦点
    edit.type_keys("123456")   # 再用模拟键盘的方式输入
    confirm = mainwin.child_window(title="确定",control_type="Button")
    confirm.click()
