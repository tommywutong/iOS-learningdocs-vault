---
title: isExecuting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/isexecuting
source_url: 'https://developer.apple.com/documentation/foundation/operation/isexecuting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/isexecuting.json'
content_hash: 'sha256:981f727dd6998197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# isExecuting

<sub>Instance Property</sub>

A Boolean value indicating whether the operation is currently executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isExecuting: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the operation is currently executing its main task or [false](../../swift/false.md) if it is not.

When implementing a concurrent operation object, you must override the implementation of this property so that you can return the execution state of your operation. In your custom implementation, you must generate KVO notifications for the `isExecuting` key path whenever the execution state of your operation object changes. For more information about manually generating KVO notifications, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You do not need to reimplement this property for nonconcurrent operations.

## See Also

### Getting the Operation Status

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [concurrent](isconcurrent.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [asynchronous](isasynchronous.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [ready](isready.md) — A Boolean value indicating whether the operation can be performed now.
- [name](name.md) — The name of the operation.
