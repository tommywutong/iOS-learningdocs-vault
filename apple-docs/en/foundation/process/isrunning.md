---
title: isRunning
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/isrunning
source_url: 'https://developer.apple.com/documentation/foundation/process/isrunning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/isrunning.json'
content_hash: 'sha256:56deb95a11fdff90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# isRunning

<sub>Instance Property</sub>

A status that indicates whether the receiver is still running.

<sub>Mac Catalyst, macOS</sub>

```swift
var isRunning: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the receiver is still running, otherwise [false](../../swift/false.md). [false](../../swift/false.md) means either the receiver could not run or it has terminated.

## See Also

### Related Documentation

- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.

### Querying the process state

- [terminationStatus](terminationstatus.md) — The exit status the receiver’s executable returns.
- [terminationReason](terminationreason-swift.property.md) — The reason the system terminated the task.
