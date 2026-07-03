from pywinauto import Application


class GTHT:
    def __init__(self) -> None:
        self.app = Application(backend="uia").connect(title_re=".*网上交易.*", timeout=5)

    
    def get_main_window(self):
        main_window = self.app.window(
            title_re=".*网上交易.*", control_type="Window"
        )
        self.main_window = main_window
        return self.main_window

    def gettable(self, table_type):
        position_tree = (
            self.main_window.child_window(
                control_type="Custom", found_index=2
            )  # 匹配有文字的Custom，自动跳过空的
            .child_window(control_type="Tree", found_index=table_type)
            .wait("ready", timeout=5)
        )
        # print("成功锁定持仓表格！正在提取数据...")

        # 2. 提取表头（所有的 Header 控件）
        headers = position_tree.descendants(control_type="Header")
        print(len(headers), "表头")
        header_names = [h.window_text() for h in headers]
        # print(f"表头字段：{header_names}")

        # 3. 提取具体的持仓数据（所有的 TreeItem 控件）
        items = position_tree.descendants(control_type="TreeItem")
        print(len(items), "表身")
        data_list = [item.window_text() for item in items]

        col_count = len(header_names)
        structured_data = []

        # 按列数切片，将平铺的数据还原成一行行记录
        for i in range(0, len(data_list), col_count):
            row_values = data_list[i : i + col_count]
            # zip 把表头和数据配对，dict 转成字典
            row_dict = dict(zip(header_names, row_values))
            structured_data.append(row_dict)
        
        print(structured_data)

        if len(structured_data) <= 1:
            return None
        
        return structured_data


    def get_positions(self):
        gtht.get_main_window()
        return gtht.gettable(2)

    def get_weituo(self):
        gtht.get_main_window()
        return gtht.gettable(1)

    def get_chengjiao(self):
        gtht.get_main_window()
        return gtht.gettable(0)


if __name__ == "__main__":
    gtht = GTHT()
    gtht.get_positions()
    gtht.get_weituo()
    gtht.get_chengjiao()


