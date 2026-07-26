---
title: terminationReason
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.6+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/terminationreason-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/process/terminationreason-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/terminationreason-swift.property.json'
content_hash: 'sha256:d6bae9c2a04a7c9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# terminationReason

<sub>Instance Property</sub>

The reason the system terminated the task.

<sub>macOS</sub>

```swift
var terminationReason: Process.TerminationReason { get }
```

## Return Value

The termination status. The possible values are described in [TerminationReason](terminationreason-swift.enum.md).

## See Also

### Querying the process state

- [running](isrunning.md) — A status that indicates whether the receiver is still running.
- [terminationStatus](terminationstatus.md) — The exit status the receiver’s executable returns.
