---
name: grill-request
description: Grill the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.
disable-model-invocation: true
---

Interview me relentlessly about every aspect of the requirement/plan/task until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask one question at a time and wait for feedback before moving on; you may batch several when they are independent of one another.

If a *fact* can be found by exploring the codebase/existing context, look it up rather than asking me.

Prefer built-in user-input tools exposed by the current agent runtime — e.g., `request_user_input`, `request_user_input_async`, `ask_user_question`, `ask_user`, or `AskUserQuestion` — only when actually available and permitted in the current mode. Follow their declared schemas, restrictions, and lifecycle; do not guess tool names or bypass mode restrictions.

Put the question, options, and recommendation in the tool call. After the question is accepted, do not repeat it in commentary, a final response, or another tool call.

For asynchronous tools, an acknowledgment such as `{"accepted": true}` means the question is pending, not answered or failed. Wait for the actual user reply using the runtime's supported mechanism; only independent fact-finding may continue while it is pending. If no wait mechanism is exposed, yield according to the runtime's instructions. If a closing response is required, briefly state that you are waiting without restating the question. Do not advance to dependent decisions or ask the next question until the pending question is resolved. A preselected option or elapsed time is not an answer.

Fall back to a plain-text question only when no permitted user-input tool is available or the tool explicitly fails, and no question remains pending. For an explicit no-answer result, follow the runtime's instructions; do not infer a choice or automatically repeat the question.
