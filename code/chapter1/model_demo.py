# 静态模型示例（DeepSeek）
# 本示例演示如何使用DeepSeek模型创建静态智能体

# 导入必要的库
from langchain.agents import create_agent  # 用于创建智能体
from langchain_deepseek import ChatDeepSeek  # DeepSeek模型集成
from dotenv import load_dotenv  # 用于加载环境变量
import os  # 用于访问环境变量

# 加载环境变量（从.env文件中读取）
load_dotenv()

# 确保API密钥已加载
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("错误：DEEPSEEK_API_KEY 环境变量未设置")
    exit(1)  # 如果API密钥未设置，退出程序

print("开始创建智能体...")

# 方法1：从模型标识符字符串初始化
# 使用完整的DeepSeek模型标识符格式
agent1 = create_agent(
    "deepseek:deepseek-chat",  # 模型标识符，格式为"提供商:模型名称"
    tools=[]  # 暂时为空工具列表
)
print("方法1：从模型标识符字符串创建智能体成功")

# 方法2：直接使用模型实例
# 创建ChatDeepSeek模型实例，明确指定模型参数
model = ChatDeepSeek(
    model="deepseek-chat",  # 模型名称
    api_key=api_key  # 传入API密钥
)

# 使用模型实例创建智能体
agent2 = create_agent(model, tools=[])
print("方法2：从模型实例创建智能体成功")

print("所有智能体创建完成！")
