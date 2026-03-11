#!/usr/bin/env bash
CMD="$1"; shift 2>/dev/null; INPUT="$*"
case "$CMD" in
  name) cat << 'PROMPT'
You are a Chinese content expert. Help with: 品牌命名(10个方案). Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  slogan) cat << 'PROMPT'
You are a Chinese content expert. Help with: 品牌口号/Slogan. Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  domain) cat << 'PROMPT'
You are a Chinese content expert. Help with: 域名可用性建议. Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  story) cat << 'PROMPT'
You are a Chinese content expert. Help with: 品牌故事. Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  identity) cat << 'PROMPT'
You are a Chinese content expert. Help with: 品牌定位分析. Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  check) cat << 'PROMPT'
You are a Chinese content expert. Help with: 商标/域名查询指南. Be detailed and practical. Output in Chinese.
User input:
PROMPT
    echo "$INPUT" ;;
  *) cat << 'EOF'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Brand Namer — 使用指南
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  name            品牌命名(10个方案)
  slogan          品牌口号/Slogan
  domain          域名可用性建议
  story           品牌故事
  identity        品牌定位分析
  check           商标/域名查询指南

  Powered by BytesAgain | bytesagain.com | hello@bytesagain.com
EOF
    ;;
esac
