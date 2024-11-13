import click
import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np
from tabulate import tabulate

# 初始化模型
model = SentenceTransformer('all-MiniLM-L6-v2')
DB_PATH = "/Users/xks/Desktop/files/sync_file/MyRepo/tmp/PathVec/db.json"

# 读取或初始化数据库
try:
    with open(DB_PATH, "r") as f:
        db = json.load(f)
except FileNotFoundError:
    db = []

# 保存数据库
def save_db():
    with open(DB_PATH, "w") as f:
        json.dump(db, f)

@click.group()
def cli():
    pass

@cli.command()
@click.option("-p", "--path", default=os.getcwd(), help="项目路径，默认为当前路径")
@click.option("-m", "--message", required=True, help="项目描述，必须提供")
def add(path, message):
    """添加一个新的项目，包含路径和描述"""
    vector = model.encode(message).tolist()
    db.append({"path": path, "description": message, "vector": vector})
    save_db()
    click.echo(f"项目已添加: {path} - {message}")


@cli.command()
@click.option("-s", "--search", required=True, help="搜索关键词")
def search(search):
    """模糊查找与查询最匹配的项目"""
    query_vector = model.encode(search)
    similarities = []
    for project in db:
        project_vector = np.array(project["vector"])
        similarity = np.dot(query_vector, project_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(project_vector))
        similarities.append((similarity, project))
    
    # 排序并获取前3个结果
    similarities = sorted(similarities, key=lambda x: x[0], reverse=True)[:3]
    
    # 格式化为表格显示
    table_data = [(project['path'], project['description'], f"{score:.2f}") for score, project in similarities]
    headers = ["文件路径", "功能说明", "相似度"]
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid", maxcolwidths=[60, 20]))

if __name__ == "__main__":
    cli()
