# bluemeat-skills

仅会安装 manual-only skills， 均为需要用户主动调用的skills，name&description不进入system prompt，适合上下文洁癖患者。

```bash
npx skills add bluemeat0724/bluemeat-skills -g
```


## Manual-only

| Skill | 用途 |
|---|---|
| `architecture-evolution-review` 🔒 | 从全代码库视角评估自然生长或 vibe-coded 项目的架构漂移，配套可失效的 Markdown 架构日志（`.architecture/optimization-log.md`）做增量复扫，避免每次重读未变代码；输出 `architecture-optimization-<project>-<YYYY-MM-DD-HHmm>.md`，含 Python 后端与 React 前端专项 reference |
| `grill-request` 🔒 | 对需求/计划/任务做持续追问式访谈，沿设计树逐分支解耦依赖、逐项对齐决策；每个问题先给出推荐答案，可由代码/上下文确认的事实直接查证而非询问 |
| `html-report` 🔒 | 生成自包含的 HTML 报告/文档（单文件、免构建、随处可开），代替 Markdown 交付可视化、可交互、可分享的输出；仅用户手动触发 |
| `review-commit-push` 🔒 | 完整审核仓库变更，按功能点组织提交，每完成一批即单独推送，并保留无关用户改动 |
| `writing-great-skills` 🔒 | Skill 编写的元参考：把可预测性作为根美德，定义上下文/认知负载、信息层级（in-skill step → in-skill reference → external reference）、leading word 等 vocabulary，及过早完成、冗余、no-op、否定等失败模式；写/审 skill 时随取随用 |

带 🔒 「manual-only」
- disable-model-invocation: true 是部分 harness 用来实现 manual-only 的具体字段， Cursor、Pi、Claude Code 支持 disable-model-invocation: true。
- Codex 不支持这个 frontmatter 字段，但支持等价能力：
  
  agents/openai.yaml
  ```yaml
  policy:
    allow_implicit_invocation: false
  ```

安装

全局安装 manual-only skills：

```bash
npx skills add bluemeat0724/bluemeat-skills -g
```

默认入口只发现 `skills/` 下的 manual-only skills，不会发现项目级或实验性 skill。实际安装路径由 `skills` CLI 根据目标 agent 选择。

安装项目级 skill 时，在目标项目根目录执行包含 skill name 的仓库子路径命令；不要添加 `-g`：

```bash
npx skills add bluemeat0724/bluemeat-skills/skills-project-level/langchain-dev-guide
```



## 项目级

| Skill | 用途 |
|---|---|
| `langchain-dev-guide` | LangChain / LangGraph 工程实践参考，覆盖 DeepAgents、结构化输出、兼容模型接入、中间件、流式输出和多 Agent 编排等常见问题 |

## 工作区 / 实验性

| Skill | 用途 |
|---|---|
| `working/prototype` | 一次性原型代码，针对难以在纸上推理的逻辑/状态模型或 UI 形态做快速验证；分 `LOGIC.md`（终端交互式状态机）与 `UI.md`（同路由多风格切换）两条分支，使用完即弃并沉淀决策 |

## 致谢

`langchain-dev-guide` 来自 [agentseek](https://github.com/ob-labs/agentseek)；

`grill-request`、`prototype` 受 [mattpocock/skills](https://github.com/mattpocock/skills) 启发。

`taste-skill` 来自 https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md

`pony` skill 与 `agents_md/AGENTS.md` Pony 人设受以下项目启发：

- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — `ponytail:` 注释约定的原型
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — 四大原则（Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution）的 LLM 行为基线；原作者 [Andrej Karpathy](https://github.com/karpathy)

