---
title: resume()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/resume()
source_url: 'https://developer.apple.com/documentation/foundation/process/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/resume%28%29.json'
content_hash: 'sha256:3ad2bb1a1a4ec507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# resume()

<sub>Instance Method</sub>

Resumes execution of a suspended task.

<sub>Mac Catalyst, macOS</sub>

```swift
func resume() -> Bool
```

## Return Value

[true](../../swift/true.md) if the receiver was able to resume execution, [false](../../swift/false.md) otherwise.

## Discussion

If the system sent multiple [- suspend](<suspend().md>) messages to the receiver, an equal number of [- resume](<resume().md>) messages must be sent before the task resumes execution.

## See Also

### Running and stopping

- [- launchAndReturnError:](<run().md>) — Runs the process with the current environment.
- [- interrupt](<interrupt().md>) — Sends an interrupt signal to the receiver and all of its subtasks.
- [- suspend](<suspend().md>) — Suspends execution of the receiver task.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.
- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
