# SMS Sender

该脚本通过读取 Excel 文件中的数据，并使用 ADB 工具自动向指定的电话号码发送自定义短信消息。

## 测试环境

### 手机设备

-   **型号**: OPPO K11 5G
-   **系统版本**: Android 14

### 软件环境

-   **ADB 版本**: Android Debug Bridge version 1.0.41  
    Version 35.0.2-12147458

## 原理

该脚本使用 ADB 命令启动默认的短信应用，并将短信内容填充到指定的联系人号码中。基本操作流程如下：

1. **启动短信应用并准备发送**：使用以下命令启动默认的短信应用，输入指定的电话号码：

    ```bash
    adb shell am start -a android.intent.action.SENDTO -d sms:{phone}
    ```

2. **解决焦点问题**：经测试，开启短信应用时焦点不会自动置于文本框，因此需要使用 ADB 模拟点击文本框的位置。可选择以下命令之一：

    - **单击**：

        ```bash
        adb shell input tap <x> <y>
        ```

    - **滑动**（适用于需要更精确控制点击位置的情况）：

        ```bash
        adb shell input swipe <x1> <y1> <x2> <y2>
        ```

3. **输入短信内容**：由于 ADB 默认不支持直接输入中文文本，因此建议使用 `ADBKeyBoard` 插件，该插件支持通过 ADB 命令发送中文字符。

## 注意事项

-   程序在每次发送消息时会添加短暂的延时 (time.sleep(0.5))，以避免焦点错误。
-   确保 text.txt 和 data.xlsx 文件存在于脚本相同目录下，否则会触发文件未找到的错误。
-   安装[ADBKeyboard](https://github.com/senzhk/ADBKeyBoard)以解决`adb shell input text`命令不能输入中文的问题
-   确保设备已连接到计算机，并启用了开发者模式和 USB 调试。
-   确保 Excel 文件中包含 Phone 和 Name 列
-   短信模板文件中，空格等特殊符号都需要转义。也就是`\ `。虽然这很逆天，但是他就是这么用的。
