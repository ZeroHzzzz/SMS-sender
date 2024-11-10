import os
import pandas as pd
import time

def main(template_path, excel_path):
    try:
        df = pd.read_excel(excel_path)
        
        for index, row in df.iterrows():
            phone = row['Phone']
            variables = {
                "name": row['Name'],
            }

            output_lines = []
            with open(template_path, 'r', encoding='utf-8') as file:
                for line in file:
                    for key, value in variables.items():
                    # 如果变量存在于当前行，则进行替换
                        if f"{{{key}}}" in line:
                            line = line.replace(f"{{{key}}}", value)
                    output_lines.append(line)
        
            print(f"生成的消息（第 {index + 1} 行）：")
            print(f"手机号：{phone}")
            
            os.system(f"adb shell am start -a android.intent.action.SENDTO -d sms:{phone}")
            time.sleep(0.5) # 这里不能太快，不然会出现焦点错误的问题
            os.system("adb shell input tap 389 2305")
            
            for line in output_lines:
                os.system(f"adb shell am broadcast -a ADB_INPUT_TEXT --es msg \"{line}\"")
                os.system("adb shell input keyevent 66") # 系统默认回车
            # return
            os.system("adb shell input swipe 985 2140 985 2140") # 发送按键位置
            
            print("-" * 50)
        
    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
    except KeyError as e:
        print(f"Excel 文件中缺少所需的列: {e}")
    except Exception as e:
        print(f"读取文件或处理数据时发生错误: {e}")

if __name__ == "__main__":
    template_path = "template.txt"
    excel_path = "data.xlsx"

    main(template_path, excel_path)
