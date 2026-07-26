---
title: suspendExecution()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/suspendexecution()
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/suspendexecution()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/suspendexecution%28%29.json'
content_hash: 'sha256:8a73fb3a95c9421d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# suspendExecution()

<sub>Instance Method</sub>

Suspends the execution of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func suspendExecution()
```

## Discussion

Suspends the execution of the receiver only if the receiver is being executed in the current thread by Cocoa scripting’s built-in Apple event handling (that is, the receiver would be returned by `[NSScriptCommand currentCommand]`)—otherwise, does nothing. A matching invocation of [- resumeExecutionWithResult:](<resumeexecution(withresult_).md>) must be made.

> [!important] Important
> The script command handler that is being executed when this method is invoked must return before the subsequent invocation of [- resumeExecutionWithResult:](<resumeexecution(withresult_).md>). That is, it is not valid to suspend a command’s execution and then resume it immediately.

Another command can execute while a command is suspended.

## See Also

### Suspending and resuming commands

- [- resumeExecutionWithResult:](<resumeexecution(withresult_).md>) — If a successful, unmatched, invocation of [- suspendExecution](<suspendexecution().md>) has been made, resume the execution of the command.
