---
title: 'wrappingSubtract(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/wrappingsubtract(_:ordering:)-6xyiw'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/wrappingsubtract(_:ordering:)-6xyiw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/wrappingsubtract%28_%3Aordering%3A%29-6xyiw.json'
content_hash: 'sha256:2ccac6c05fe6060d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# wrappingSubtract(_:ordering:)

<sub>Instance Method</sub>

Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func wrappingSubtract(_ operand: Int8, ordering: AtomicUpdateOrdering) -> (oldValue: Int8, newValue: Int8)
```

## Parameters

- `operand` — An integer value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple containing the original value before the operation and the new value after the operation.

## Discussion

> [!note] Note
> This operation silently wraps around on overflow, like the `&-` operator does on `Int8` values.
