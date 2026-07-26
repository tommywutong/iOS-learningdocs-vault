---
title: isConcurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/isconcurrent
source_url: 'https://developer.apple.com/documentation/foundation/operation/isconcurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/isconcurrent.json'
content_hash: 'sha256:e3aaf6e030bad534'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# isConcurrent

<sub>Instance Property</sub>

A Boolean value indicating whether the operation executes its task asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isConcurrent: Bool { get }
```

## Discussion

Use the [asynchronous](isasynchronous.md) property instead.

The value of this property is [true](../../swift/true.md) for operations that run asynchronously with respect to the current thread or [false](../../swift/false.md) for operations that run synchronously on the current thread. The default value of this property is [false](../../swift/false.md).

In macOS 10.6 and later, operation queues ignore the value in this property and always start operations on a separate thread.

## See Also

### Getting the Operation Status

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
- [executing](isexecuting.md) — A Boolean value indicating whether the operation is currently executing.
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [asynchronous](isasynchronous.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [ready](isready.md) — A Boolean value indicating whether the operation can be performed now.
- [name](name.md) — The name of the operation.
