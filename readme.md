# bluemeat-skills

带 🔒 的 skill 为「manual-only 仅用户手动触发」，模型不会自动调用、不占上下文。

manual-only 是一种行为模式：模型不能自动调用，但用户可以显式调用。
disable-model-invocation: true 是部分 harness 用来实现 manual-only 的具体字段。
Cursor、Pi、Claude Code 支持 disable-model-invocation: true。
Codex 不支持这个 frontmatter 字段，但支持等价能力：
agents/openai.yaml
```yaml
policy:
  allow_implicit_invocation: false
```

## Ready

| Skill | 用途 |
|---|---|
| `architecture-evolution-review` 🔒 | 从全代码库视角评估自然生长或 vibe-coded 项目的架构漂移，配套可失效的 Markdown 架构日志（`.architecture/optimization-log.md`）做增量复扫，避免每次重读未变代码；输出 `architecture-optimization-<project>-<YYYY-MM-DD-HHmm>.md`，含 Python 后端与 React 前端专项 reference |
| `grill-request` 🔒 | 对需求/计划/任务做持续追问式访谈，沿设计树逐分支解耦依赖、逐项对齐决策；每个问题先给出推荐答案，可由代码/上下文确认的事实直接查证而非询问 |
| `html-report` 🔒 | 生成自包含的 HTML 报告/文档（单文件、免构建、随处可开），代替 Markdown 交付可视化、可交互、可分享的输出；仅用户手动触发 |
| `writing-great-skills` 🔒 | Skill 编写的元参考：把可预测性作为根美德，定义上下文/认知负载、信息层级（in-skill step → in-skill reference → external reference）、leading word 等 vocabulary，及过早完成、冗余、no-op、否定等失败模式；写/审 skill 时随取随用 |

## 工作区 / 实验性

| Skill | 用途 |
|---|---|
| `working/prototype` | 一次性原型代码，针对难以在纸上推理的逻辑/状态模型或 UI 形态做快速验证；分 `LOGIC.md`（终端交互式状态机）与 `UI.md`（同路由多风格切换）两条分支，使用完即弃并沉淀决策 |

