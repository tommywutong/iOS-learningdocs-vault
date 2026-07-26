---
title: 'resumeExecution(withResult:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommand/resumeexecution(withresult:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/resumeexecution(withresult:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/resumeexecution%28withresult%3A%29.json'
content_hash: 'sha256:16c072290ad51e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# resumeExecution(withResult:)

<sub>Instance Method</sub>

If a successful, unmatched, invocation of [- suspendExecution](<suspendexecution().md>) has been made, resume the execution of the command.

<sub>Mac Catalyst, macOS</sub>

```swift
func resumeExecution(withResult result: Any?)
```

## Discussion

Resumes the execution of the command if a successful, unmatched, invocation of [- suspendExecution](<suspendexecution().md>) has been made—otherwise, does nothing. The value for `result` is dependent on the segment of command execution that was suspended:

- If [- suspendExecution](<suspendexecution().md>) was invoked from within a command handler of one of the command’s receivers, `result` is considered to be the return value of the handler. Unless the command has received a [scriptErrorNumber](scripterrornumber.md) message with a nonzero error number, execution of the command will continue and the command handlers of other receivers will be invoked.
- If [- suspendExecution](<suspendexecution().md>) was invoked from within an override of [- performDefaultImplementation](<performdefaultimplementation().md>) the result is treated as if it were the return value of the invocation of [- performDefaultImplementation](<performdefaultimplementation().md>).

[- resumeExecutionWithResult:](<resumeexecution(withresult_).md>) may be invoked in any thread, not just the one in which the corresponding invocation of [- suspendExecution](<suspendexecution().md>) occurred.

> [!important] Important
> The script command handler that is being executed when [- suspendExecution](<suspendexecution().md>) is invoked must return before you invoke [- resumeExecutionWithResult:](<resumeexecution(withresult_).md>). That is, it is not valid to suspend a command’s execution and then resume it immediately.

## See Also

### Suspending and resuming commands

- [- suspendExecution](<suspendexecution().md>) — Suspends the execution of the receiver.
