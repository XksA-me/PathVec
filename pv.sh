#!/bin/bash

# 检查是否提供了命令
if [ $# -lt 2 ]; then
  echo "使用方法: $0 <命令> <参数>"
  exit 1
fi

# 获取命令
COMMAND=$1
shift  # 去掉第一个参数（命令），然后移到下一个参数

CODE_PATH="/usr/local/PathVec/pv.py"

case $COMMAND in
  add)
    # 参数检查：-m <描述信息> 是必须的，-p <项目路径> 是可选的
    if [ $# -lt 2 ]; then
      echo "使用方法: $0 add -m <描述信息> [-p <项目路径>]"
      exit 1
    fi
    python $CODE_PATH add "$@"
    ;;
  
  search)
    # 参数检查：-s <搜索字符串> 是必须的
    if [ $# -lt 2 ]; then
      echo "使用方法: $0 search -s <搜索字符串>"
      exit 1
    fi
    python $CODE_PATH search "$@"
    ;;
  
  *)
    echo "未知命令: $COMMAND"
    exit 1
    ;;
esac
