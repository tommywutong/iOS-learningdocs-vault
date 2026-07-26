---
title: 'run(_:arguments:terminationHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.13+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/process/run(_:arguments:terminationhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/process/run(_:arguments:terminationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/run%28_%3Aarguments%3Aterminationhandler%3A%29.json'
content_hash: 'sha256:3ded6971b66096bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# run(_:arguments:terminationHandler:)

<sub>Type Method</sub>

Creates and runs a task with a specified executable and arguments.

<sub>macOS</sub>

```swift
class func run(_ url: URL, arguments: [String], terminationHandler: (@Sendable (Process) -> Void)? = nil) throws -> Process
```

## Parameters

- `url` — The URL for the executable.

- `arguments` — An array of `NSString` objects that supplies the arguments to the task. If `arguments` is `nil`, the system raises an `NSInvalidArgumentException`.

- `terminationHandler` — The system invokes this completion block when the task has completed.

## Return Value

An initialized `NSTask` object with the environment of the current process.

## See Also

### Creating and initializing a process

- [- init](<init().md>) — Returns an initialized process object with the environment of the current process.
