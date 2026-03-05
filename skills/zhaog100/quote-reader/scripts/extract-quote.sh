#!/bin/bash

# 引用提取脚本
# 功能：根据引用信息检索会话历史，提取完整引用内容

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
INTENT_FILE="$SKILL_DIR/config/intent-rules.json"

QUOTE_INFO="$1"

if [ -z "$QUOTE_INFO" ]; then
    echo "用法: extract-quote.sh <引用信息JSON>"
    exit 1
fi

# 解析引用信息
HAS_QUOTE=$(echo "$QUOTE_INFO" | jq -r '.has_quote')
PLATFORM=$(echo "$QUOTE_INFO" | jq -r '.platform')
MESSAGE_ID=$(echo "$QUOTE_INFO" | jq -r '.message_id')
QUOTED_TEXT=$(echo "$QUOTE_INFO" | jq -r '.quoted_text // empty')

# 如果没有引用，直接返回
if [ "$HAS_QUOTE" != "true" ]; then
    echo '{"error": "无引用信息"}'
    exit 0
fi

# 识别引用意图
detect_intent() {
    local user_message="$1"
    
    # 读取意图规则
    local intents=$(jq -r '.intents | keys[]' "$INTENT_FILE" 2>/dev/null)
    
    for intent in $intents; do
        local keywords=$(jq -r ".intents.\"$intent\".keywords[]" "$INTENT_FILE" 2>/dev/null)
        
        for keyword in $keywords; do
            if echo "$user_message" | grep -qi "$keyword"; then
                echo "$intent"
                return 0
            fi
        done
    done
    
    echo "unknown"
}

# 模拟检索会话历史（实际应调用sessions_history）
retrieve_message() {
    local message_id="$1"
    local platform="$2"
    
    # 这里是模拟数据，实际应调用OpenClaw的sessions_history工具
    # 示例：sessions_history sessionKey="xxx" limit=50
    
    # 模拟返回
    case "$message_id" in
        "om_x100b55b"*)
            cat <<EOF
{
  "id": "$message_id",
  "content": "QMD向量生成需要CUDA支持，但VMware虚拟GPU不支持CUDA。",
  "timestamp": "2026-03-05T08:00:00Z",
  "role": "assistant"
}
EOF
            ;;
        *)
            cat <<EOF
{
  "id": "$message_id",
  "content": "未找到消息ID: $message_id",
  "timestamp": "$(date -Iseconds)",
  "role": "system"
}
EOF
            ;;
    esac
}

# 提取上下文
extract_context() {
    local message_id="$1"
    
    # 这里应调用sessions_history获取上下文
    # 目前返回模拟数据
    
    cat <<EOF
{
  "before": [
    {"role": "user", "content": "QMD怎么用？"},
    {"role": "assistant", "content": "QMD是向量搜索工具..."}
  ],
  "after": [
    {"role": "user", "content": "那怎么解决？"},
    {"role": "assistant", "content": "可以使用CPU模式..."}
  ]
}
EOF
}

# 主提取逻辑
main() {
    # 1. 检索引用消息
    local quoted_message
    if [ -n "$MESSAGE_ID" ] && [ "$MESSAGE_ID" != "null" ]; then
        quoted_message=$(retrieve_message "$MESSAGE_ID" "$PLATFORM")
    else
        # 使用提供的引用文本
        quoted_message=$(cat <<EOF
{
  "id": "unknown",
  "content": "$QUOTED_TEXT",
  "timestamp": "$(date -Iseconds)",
  "role": "unknown"
}
EOF
)
    fi
    
    # 2. 提取上下文
    local context
    if [ -n "$MESSAGE_ID" ] && [ "$MESSAGE_ID" != "null" ]; then
        context=$(extract_context "$MESSAGE_ID")
    else
        context='{"before": [], "after": []}'
    fi
    
    # 3. 识别意图
    local intent=$(detect_intent "$QUOTED_TEXT")
    
    # 4. 生成输出
    cat <<EOF
{
  "quoted_message": $(echo "$quoted_message" | jq .),
  "context": $(echo "$context" | jq .),
  "intent": "$intent",
  "platform": "$PLATFORM",
  "suggested_response": "$(get_suggested_response "$intent")"
}
EOF
}

# 获取建议的回复方式
get_suggested_response() {
    local intent="$1"
    
    case "$intent" in
        "clarify")
            echo "解释引用内容的具体含义"
            ;;
        "supplement")
            echo "基于引用内容补充相关信息"
            ;;
        "refute")
            echo "修正或反驳引用中的观点"
            ;;
        "deepen")
            echo "深入分析引用内容"
            ;;
        "relate")
            echo "关联引用内容和其他对话"
            ;;
        "example")
            echo "为引用内容举例说明"
            ;;
        *)
            echo "基于引用内容回答问题"
            ;;
    esac
}

# 执行主函数
main
