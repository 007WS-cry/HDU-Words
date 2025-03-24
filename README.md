# HDU我爱记单词脚本

## 脚本说明
本脚本仅供个人学习编程使用，绝无引导作弊行为！使用作弊者后果自负！

## 简介
本脚本用于自动化完成HDU我爱记单词平台上的英语测试。通过Selenium模拟浏览器操作，打开指定网页，进入测试页面，并使用OpenAI API获取问题的答案，自动选择答案完成测试。

## 环境要求
- Python 3.x
- 相关Python库：
  - selenium
  - openai

### 安装依赖
在命令行中运行以下命令来安装所需的Python库：
```bash
pip install selenium openai
```

### 浏览器驱动
本脚本使用Edge浏览器，需要下载对应的`msedgedriver.exe`，并将其放在脚本同一目录下。下载地址：[Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## 使用方法
1. **配置API密钥**：
   打开`Script.py`文件，找到以下代码：
   ```python
   client = OpenAI(
       api_key = '输入你的API密钥',
       base_url = '输入你的API URL'
   )
   ```
   将`api_key`替换为你自己的OpenAI API密钥，`base_url`替换为你的API URL（如果需要的话）。

2. **运行脚本**：
   在命令行中进入脚本所在目录，运行以下命令：
   ```bash
   python Script.py
   ```

## 脚本流程
1. **初始化浏览器**：
   使用Selenium初始化Edge浏览器，并模拟移动设备访问。
2. **打开网页**：
   打开HDU我爱记单词的英语测试页面。
3. **进入测试**：
   点击相关按钮进入测试页面。
4. **循环答题**：
   - 每次循环获取问题和四个选项。
   - 将问题和选项发送到OpenAI API，获取答案。
   - 根据答案点击相应的选项。
5. **提交测试**：
   完成100道题后，点击提交按钮。

## 注意事项
- **API费用**：使用OpenAI API会产生费用，请确保你的账户有足够的余额。
- **网络问题**：脚本依赖网络连接，请确保网络稳定。
- **页面结构变化**：如果HDU我爱记单词平台的页面结构发生变化，脚本中的XPath可能需要相应调整。

以上就是本脚本的详细说明和使用方法。如有任何问题，请随时联系。