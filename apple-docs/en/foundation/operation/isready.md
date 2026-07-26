---
title: isReady
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/isready
source_url: 'https://developer.apple.com/documentation/foundation/operation/isready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/isready.json'
content_hash: 'sha256:84d448f2f48ef58f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# isReady

<sub>Instance Property</sub>

A Boolean value indicating whether the operation can be performed now.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isReady: Bool { get }
```

## Discussion

The readiness of operations is determined by their dependencies on other operations and potentially by custom conditions that you define. The `NSOperation` class manages dependencies on other operations and reports the readiness of the receiver based on those dependencies.

If you want to use custom conditions to define the readiness of your operation object, reimplement this property and return a value that accurately reflects the readiness of the receiver. If you do so, your custom implementation must get the default property value from `super` and incorporate that readiness value into the new value of the property. In your custom implementation, you must generate KVO notifications for the `isReady` key path whenever the ready state of your operation object changes. For more information about generating KVO notifications, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Related Documentation

- [dependencies](dependencies.md) — An array of the operation objects that must finish executing before the current object can begin executing.

### Getting the Operation Status

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
- [executing](isexecuting.md) — A Boolean value indicating whether the operation is currently executing.
- [finished](isfinished.md) — A Boolean value indicating whether the operation has finished executing its task.
- [concurrent](isconcurrent.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [asynchronous](isasynchronous.md) — A Boolean value indicating whether the operation executes its task asynchronously.
- [name](name.md) — The name of the operation.
