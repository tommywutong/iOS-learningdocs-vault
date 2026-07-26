---
title: 'withExtendedLifetime(_:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withextendedlifetime(_:_:)-59dz3'
source_url: 'https://developer.apple.com/documentation/swift/withextendedlifetime(_:_:)-59dz3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withextendedlifetime%28_%3A_%3A%29-59dz3.json'
content_hash: 'sha256:169d27b56c8d3934'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withExtendedLifetime(_:_:)

<sub>Function</sub>

Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withExtendedLifetime<T, E, Result>(_ x: borrowing T, _ body: (borrowing T) throws(E) -> Result) throws(E) -> Result where E : Error, T : ~Copyable, T : ~Escapable, Result : ~Copyable
```

## Parameters

- `x` — An instance to preserve until the execution of `body` is completed.

- `body` — A closure to execute that depends on the lifetime of `x` being extended. If `body` has a return value, that value is also used as the return value for the `withExtendedLifetime(_:_:)` method.

## Return Value

The return value, if any, of the `body` closure parameter.

## See Also

### Reference Counting

- [Unmanaged](unmanaged.md) — A type for propagating an unmanaged object reference.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-4mmpv.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [extendLifetime(_:)](<extendlifetime(__).md>) — Extends the lifetime of the given instance.
