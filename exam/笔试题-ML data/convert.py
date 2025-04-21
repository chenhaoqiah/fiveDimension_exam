import json
import re
import time
from uuid import uuid4

# 示例输入数据（假设从数据集中加载）
input_data = [
    "Is this a test? Yes\nIs this a real question? No",
    "Is this another test? Yes\nIs this a real answer? No"
]

# 定义输出格式
output_schema = {
    "id": "string",
    "Question": "string",
    "Answer": "string"
}

# 转换函数
def parse_questions_answers(input_entries):
    qa_pairs = []
    for entry in input_entries:
        # 使用正则表达式分割问题和答案
        questions_answers = re.split(r'\n', entry)
        for qa in questions_answers:
            if "?" in qa:
                question, answer = qa.split("?")
                qa_pairs.append({
                    "id": str(uuid4()),  # 生成唯一标识符
                    "Question": question.strip(),
                    "Answer": answer.strip()
                })
    return qa_pairs

# 开始转换
start_time = time.time()
parsed_data = parse_questions_answers(input_data)
end_time = time.time()

# 保存为JSON文件
with open("output.json", "w") as f:
    json.dump(parsed_data, f, indent=4)

# 统计信息
total_pairs = len(parsed_data)
processing_time = end_time - start_time

# 打印结果
print(f"Total Question-Answer pairs extracted: {total_pairs}")
print(f"Processing time: {processing_time:.2f} seconds")

# 输出架构
print("Output Schema:")
print(json.dumps(output_schema, indent=4))