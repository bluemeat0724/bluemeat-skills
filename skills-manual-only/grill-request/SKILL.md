---
name: grill-request
description: Grill the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.
disable-model-invocation: true
---

Interview me relentlessly about every aspect of the requirement/plan/task until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask one question at a time and wait for feedback before moving on; you may batch several when they are independent of one another.

If a *fact* can be found by exploring the codebase/existing context, look it up rather than asking me. 

Prefer built-in user-input tools exposed by the current agent runtime — e.g., `AskUserQuestion`, `request_user_input`, `clarify`, `ask_user`, or any equivalent.