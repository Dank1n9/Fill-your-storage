import os
import time

# 欢迎信息和警告
print("欢迎使用炸机模块！请确保你已经关闭了所有重要的程序，以免数据丢失。")
time.sleep(1)
print("如果您使用此程序造成了严重后果，本程序不承担责任！")
time.sleep(1)
print("此程序危害性较大，确认使用吗?  //五秒后弹出下一个提示框")
time.sleep(5)
print("输入N立即取消操作 输入其他任意键继续操作")
if input() == "N":
    print("操作已取消！下次见！")
    time.sleep(1)
    exit()

# 用户确认继续
print("您已确认使用炸机模块，继续操作...")
time.sleep(1)
print("此项目将会输出在你的默认桌面，文件名为example.txt，请注意查收！")
time.sleep(1)


print("首先你需要学习怎么暂停！")
time.sleep(1)
print("在写入过程中，按下Ctrl+C可以暂停写入！")
time.sleep(1)
print("现在请你来重复一下停止写入的命令吧！")
while True:
    cmd = input("请输入停止写入的命令：")
    if cmd.strip().lower() in ["ctrl+c", "ctrl + c", "ctrl+c", "ctrl +c"]:
        print("正确！你已经学会了如何暂停写入！")
        break
    else:
        print("不正确，请再试一次！")
time.sleep(1)
print("现在我们获取您的用户信息/////此过程完全在您本地操作，不会上传到云端！")
time.sleep(1.5)


# 获取用户名并构建桌面路径
username = input("请输入你电脑的用户名（不需要管理员权限）：")
path = f"C:\\Users\\{username}\\Desktop"

print(f"尝试切换到：{path}")
w = 0
try:
    os.chdir(path)
    print(f"成功切换至：{os.getcwd()}")
    w = 1
except FileNotFoundError:
    print(f"错误：路径 {path} 不存在！请检查用户名是否正确。")
except Exception as e:
    print(f"其他错误：{e}")

if w == 0:
    print("无法继续操作，请修正路径问题后重试。")
    print("3秒后程序将退出...")
    time.sleep(3)
    exit()

# 用户获取成功
print("用户获取成功")
time.sleep(1)
print("正在准备写入文件...")
print("准备内容中..." )
time.sleep(2)
print("准备完成！")
time.sleep(1)
print("脚本将在3秒后开始写入文件...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("开始写入文件！")


# 构造大量文本内容（预计算其字节长度）
text_block = (
    "🔥🐉🤯🧠💥✨🌌🌀⚡️💣🌍🌎🌏🌐🌑🌒🌓🌔🌕🌖🌗🌘🌙☀️🌟🌠⭐️✨💫" * 50000 +
    "﷽" * 50000 * 10  # 注意：原写法重复了 50000 次字符串，这里简化为直接乘
)
# 注意：实际字节数取决于编码（UTF-8 中 emoji 和 ﷽ 占多个字节）
text_bytes = text_block.encode('utf-8')
block_size = len(text_bytes) + len("这是一个测试文件，用于炸机模块。\n".encode('utf-8'))

# 初始化统计变量
total_written = 0
start_time = time.time()
report_interval = 1.0  # 每隔1秒报告一次速度
last_report_time = start_time

with open('example.txt', 'wb') as file:  # 改用二进制模式避免 encode 开销
    try:
        while True:
            # 写入一行说明 + 大文本块
            line = "这是一个测试文件，用于炸机模块。\n".encode('utf-8')
            file.write(line)
            file.write(text_bytes)
            file.flush()
            # 可选：强制同步到磁盘（会显著降低速度，但更真实）
            # os.fsync(file.fileno())

            total_written += block_size

            # 实时速度计算（每秒更新一次）
            current_time = time.time()
            if current_time - last_report_time >= report_interval:
                elapsed = current_time - start_time
                speed_mbps = (total_written / (1024 * 1024)) / elapsed  # MB/s
                print(f"[实时] 已写入: {total_written / (1024*1024):.2f} MB | 平均速度: {speed_mbps:.2f} MB/s")
                last_report_time = current_time

    except KeyboardInterrupt:
        print("\n用户中断写入！")
    except Exception as e:
        print(f"\n写入过程中发生错误////请检查你的磁盘剩余空间: {e}")

print("程序结束。")
time.sleep(5)