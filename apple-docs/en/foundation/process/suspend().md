---
title: suspend()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/suspend()
source_url: 'https://developer.apple.com/documentation/foundation/process/suspend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/suspend%28%29.json'
content_hash: 'sha256:9000604ba5862521'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# suspend()

<sub>Instance Method</sub>

Suspends execution of the receiver task.

<sub>Mac Catalyst, macOS</sub>

```swift
func suspend() -> Bool
```

## Return Value

[true](../../swift/true.md) if the receiver was successfully suspended, [false](../../swift/false.md) otherwise.

## Discussion

Multiple [- suspend](<suspend().md>) messages can be sent, but they must be balanced with an equal number of [- resume](<resume().md>) messages before the task resumes execution.

## See Also

### Running and stopping

- [- launchAndReturnError:](<run().md>) — Runs the process with the current environment.
- [- interrupt](<interrupt().md>) — Sends an interrupt signal to the receiver and all of its subtasks.
- [- resume](<resume().md>) — Resumes execution of a suspended task.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.
- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
