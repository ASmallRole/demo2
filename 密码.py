import os
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    while len(password) < length:
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)

def save_to_file(purpose, password):
    try:
        # 获取用户文档目录路径（跨平台兼容）
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        
        # 如果不存在则创建目录（Mac/Linux可能需要调整）
        os.makedirs(documents_path, exist_ok=True)
        
        # 构造完整文件路径
        file_path = os.path.join(documents_path, "密码.md")
        
        # 使用追加模式写入（UTF-8编码）
        with open(file_path, "a", encoding='utf-8') as file:
            file.write(f"---\n---\n# 用途：{purpose}\n```python\n{password}\n```\n\n")
            
    except Exception as e:
        # 显示错误提示（调试用）
        messagebox.showerror("文件保存失败", f"错误信息：{str(e)}")

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 12:
            messagebox.showerror("错误", "密码长度至少为12个字符")
            return
        purpose = purpose_entry.get()
        password = generate_password(length)
        result_label.config(text=f"生成的密码: {password}")
        
        # 将生成的密码复制到剪贴板
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # 确保立即执行剪贴板操作
        
        save_to_file(purpose, password)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字作为密码长度")

# 创建主窗口
root = tk.Tk()
root.title("密码生成器")

# 用途输入框
tk.Label(root, text="密码用途:").pack()
purpose_entry = tk.Entry(root)
purpose_entry.pack()

# 长度输入框
tk.Label(root, text="密码长度 (至少12):").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# 生成按钮
generate_button = tk.Button(root, text="生成密码", command=on_generate)
generate_button.pack()

# 结果显示标签
result_label = tk.Label(root, text="")
result_label.pack()

# 运行主循环
root.mainloop()