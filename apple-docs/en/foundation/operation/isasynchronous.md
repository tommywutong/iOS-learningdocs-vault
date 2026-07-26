---
title: isAsynchronous
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/isasynchronous
source_url: 'https://developer.apple.com/documentation/foundation/operation/isasynchronous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/isasynchronous.json'
content_hash: 'sha256:5fa8459f91d6aca0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# isAsynchronous

<sub>Instance Property</sub>

A Boolean value indicating whether the operation executes its task asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isAsynchronous: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) for operations that run asynchronously with respect to the current thread or [false](../../swift/false.md) for operations that run synchronously on the current thread. The default value of this property is [false](../../swift/false.md).

When implementing an asynchronous operation object, you must implement this property and return [true](../../swift/true.md). For more information about how to implement an asynchronous operation, see [Asynchronous Versus Synchronous Operations](../operation.md#Asynchronous-Versus-Synchronous-Operations).

## See Also

### Getting the Operation Status

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
- [executing](isexecuting.md) — A Boolean value indicating whether the operation is currently executing.
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [concurrent](isconcurrent.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [ready](isready.md) — A Boolean value indicating whether the operation can be performed now.
- [name](name.md) — The name of the operation.
