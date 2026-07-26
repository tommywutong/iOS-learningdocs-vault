---
title: 'extendLifetime(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/extendlifetime(_:)'
source_url: 'https://developer.apple.com/documentation/swift/extendlifetime(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/extendlifetime%28_%3A%29.json'
content_hash: 'sha256:93b3982a3d0c1fdd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# extendLifetime(_:)

<sub>Function</sub>

Extends the lifetime of the given instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extendLifetime<T>(_ x: borrowing T) where T : ~Copyable, T : ~Escapable
```

## Parameters

- `x` — An instance to preserve until this function returns.

## See Also

### Reference Counting

- [Unmanaged](unmanaged.md) — A type for propagating an unmanaged object reference.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-4mmpv.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-59dz3.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
