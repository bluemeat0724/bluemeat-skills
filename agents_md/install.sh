#!/bin/sh
set -eu

download=$(mktemp)
stage=''
trap 'rm -f "$download" "$stage"' EXIT
trap 'exit 1' HUP INT TERM

curl -fL https://raw.githubusercontent.com/bluemeat0724/bluemeat-skills/main/agents_md/AGENTS.md -o "$download"
if [ ! -s "$download" ]; then
  echo '下载内容为空，未修改原文件。' >&2
  exit 1
fi

for dir in "$HOME/.agent" "$HOME/.codex"; do
  file="$dir/AGENTS.md"
  if [ -L "$file" ] || { [ -e "$file" ] && [ ! -f "$file" ]; }; then
    echo "目标不是普通文件，停止安装：$file" >&2
    exit 1
  fi
done

for dir in "$HOME/.agent" "$HOME/.codex"; do
  mkdir -p "$dir"
  file="$dir/AGENTS.md"
  stage=$(mktemp "$dir/.AGENTS.md.XXXXXX")
  cp "$download" "$stage"
  if [ -f "$file" ]; then
    backup=$(mktemp "$file.bak.XXXXXX")
    cp -p "$file" "$backup"
    echo "已备份：$backup"
  fi
  mv -f "$stage" "$file"
  stage=''
  echo "已安装：$file"
done
