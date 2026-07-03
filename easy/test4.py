from pywinauto import Desktop

desktop = Desktop(backend="uia")


real_window = desktop.window(
    title_re=r"^国泰海通通财 网上交易系统.*本委托系统提示.*", control_type="Window"
)

if real_window.exists():
    print("成功在桌面层级锁定交易窗口！")
    print(f"窗口完整标题: {real_window.window_text()}")

    # 接下来你就可以继续在这个 real_window 下寻找 SplitButton 和 TreeView 了
else:
    print("未找到目标交易窗口，请检查软件是否已打开。")


topw = real_window.top_window()
print(topw)

# asset_panel = real_window.child_window(control_type="TreeView", title_re="资  产.*")

# tree_view = asset_panel.child_window(control_type="TreeView")
# tree_view.wait("ready", timeout=5)



