import pyperclip

def text_to_bangka(text):
    # 将文字转为UTF-8编码的字节数据
    byte_data = text.encode('utf-8')
    
    # 将每个字节转换为8位二进制字符串并连接，用空格分隔
    binary_str = ' '.join(format(byte, '08b') for byte in byte_data)
    
    # 替换二进制为邦咔
    bangka = binary_str.replace('0', '邦').replace('1', '咔')
    
    # 复制到剪贴板
    pyperclip.copy(bangka)
    
    return bangka

def bangka_to_text(bangka):
    try:
        # 将邦咔替换回二进制
        binary_str = bangka.replace('邦', '0').replace('咔', '1')
        
        # 按空格分割成每组8位二进制
        binary_groups = binary_str.split(' ')
        
        # 将每组二进制转换为字节
        byte_data = bytes(int(group, 2) for group in binary_groups)
        
        # 将字节数据解码为文字
        text = byte_data.decode('utf-8', errors='replace')
        return text
    except Exception as e:
        return f"转换错误：{str(e)}"

def main():
    while True:
        print("请选择模式：")
        print("1. 文字转邦咔二进制")
        print("2. 邦咔二进制转文字")
        print("0. 退出程序\n")
        
        mode = input("输入模式编号 (1, 2 或 0): ")

        if mode == '1':
            input_text = input("请输入要转换的文字：")
            result = text_to_bangka(input_text)
            print("转换结果：", result)
            print("转换结果已自动复制到剪贴板！\n")
        elif mode == '2':
            input_bangka = input("请输入要转换的邦咔二进制（用空格分隔每组）：")
            result = bangka_to_text(input_bangka)
            print("转换结果：\n", result)
        elif mode == '0':
            print("程序退出。\n")
            break
        else:
            print("无效的模式编号！\n")

if __name__ == "__main__":
    main()
