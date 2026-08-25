# Skill 开发

- `skills/`：需用户手动触发的 skill，也是 `npx skills add` 默认发现并全局安装的目录。
- `skills-project-level/`：项目级 skill，需在项目根目录通过包含 skill name 的仓库子路径单独安装。
- `working/`：正在开发尚未完成、暂不可用的 skill
- `collection`: 一些收藏

- 维护 `readme.md` 中的 skill 目录，及时更新；小改动无需同步修改。
- 除非用户明确要求，skill 彼此独立；开发时仅阅读相关目录，避免引入无关上下文。
- 若 skill 涉及用户交互，skill 提示词应指示：
“Prefer built-in user-input tools exposed by the current agent runtime — e.g., `request_user_input`， `ask_user_question`, `ask_user`, `AskUserQuestion`”
