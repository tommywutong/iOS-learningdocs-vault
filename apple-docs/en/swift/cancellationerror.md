---
title: CancellationError
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/cancellationerror
source_url: 'https://developer.apple.com/documentation/swift/cancellationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/cancellationerror.json'
content_hash: 'sha256:577c47899290de46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CancellationError

<sub>Structure</sub>

An error that indicates a task was canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CancellationError
```

## Overview

This error is also thrown automatically by `Task.checkCancellation()`, if the current task has been canceled.

## Relationships

- **Conforms To**: [Error](error.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<cancellationerror/init().md>)

## See Also

### Canceling Tasks

- [cancel()](<task/cancel().md>) — Cancels this task.
- [isCancelled](task/iscancelled-swift.property.md) — A Boolean value that indicates whether the task should stop executing.
- [isCancelled](task/iscancelled-swift.type.property.md) — A Boolean value that indicates whether the task should stop executing.
- [checkCancellation()](<task/checkcancellation().md>) — Throws an error if the task was canceled.
- [withTaskCancellationHandler(operation:onCancel:)](<withtaskcancellationhandler(operation_oncancel_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
- [withTaskCancellationHandler(operation:onCancel:isolation:)](<withtaskcancellationhandler(operation_oncancel_isolation_).md>) — Execute an operation with a cancellation handler that’s immediately invoked if the current task is canceled.
