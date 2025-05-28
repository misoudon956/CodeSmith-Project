import customtkinter as ctk

#アプリ本体のクラス
class CodeSmithApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("CodeSmithApp")
        self.geometry("600x400")
        #/左サイドバーのコード
        self.blocks = ["none", "if", "while", "for", "true", "false"]

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.sidebar = ctk.CTkFrame(
        self, 
        width=150, 
        fg_color="#1F1F1F", 
        border_color="#606060", 
        border_width=1, 
        corner_radius=0
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.mainbar = ctk.CTkFrame(self, fg_color="#1F1F1F")
        self.mainbar.grid(row=0, column=1, sticky="nsew")

        for block in self.blocks:
            btn = ctk.CTkButton(self.sidebar, text=block, command=lambda b=block: self.add_block_to_canvas(b))
            btn.pack(pady=5, padx=10, fill="x")
        #\

    #ブロックをクリックしたときのメソッド
    def add_block_to_canvas(self, block_name):
        if block_name == self.blocks[0]:
            #Myflameでフレームを作る
            self.my_frame = Myflame(master=self.mainbar)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="w")

#フレームの処理をするクラス
class Myflame(ctk.CTkFrame):
    def __init__(sel, master, **kwargs):
        super().__init__(master, fg_color="#444444", **kwargs)


if __name__ == "__main__":
    app = CodeSmithApp()
    app.mainloop()