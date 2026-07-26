---
title: isCancelled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/iscancelled
source_url: 'https://developer.apple.com/documentation/foundation/operation/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/iscancelled.json'
content_hash: 'sha256:e1b0f340e50fe5ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# isCancelled

<sub>Instance Property</sub>

A Boolean value indicating whether the operation has been cancelled

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## Discussion

The default value of this property is [false](../../swift/false.md). Calling the [- cancel](<cancel().md>) method of this object sets the value of this property to [true](../../swift/true.md). Once canceled, an operation must move to the finished state.

Canceling an operation does not actively stop the receiver’s code from executing. An operation object is responsible for calling this method periodically and stopping itself if the method returns [true](../../swift/true.md).

You should always check the value of this property before doing any work towards accomplishing the operation’s task, which typically means checking it at the beginning of your custom [- main](<main().md>) method. It is possible for an operation to be cancelled before it begins executing or at any time while it is executing. Therefore, checking the value at the beginning of your [- main](<main().md>) method (and periodically throughout that method) lets you exit as quickly as possible when an operation is cancelled.

## See Also

### Related Documentation

- [- cancel](<cancel().md>) — Advises the operation object that it should stop executing its task.

### Getting the Operation Status

- [executing](isexecuting.md) — A Boolean value indicating whether the operation is currently executing.
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [concurrent](isconcurrent.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [asynchronous](isasynchronous.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [ready](isready.md) — A Boolean value indicating whether the operation can be performed now.
- [name](name.md) — The name of the operation.
