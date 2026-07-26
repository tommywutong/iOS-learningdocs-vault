---
title: terminationHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/terminationhandler
source_url: 'https://developer.apple.com/documentation/foundation/process/terminationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/terminationhandler.json'
content_hash: 'sha256:8d1366975fce38b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# terminationHandler

<sub>Instance Property</sub>

A completion block the system invokes when the task completes.

<sub>macOS</sub>

```swift
var terminationHandler: (@Sendable (Process) -> Void)? { get set }
```

## Discussion

The system passes the task object to the block to allow access to the task parameters, for example to determine if the task completed successfully.

This block isn’t guaranteed to be fully executed prior to [- waitUntilExit](<waituntilexit().md>) returning.
