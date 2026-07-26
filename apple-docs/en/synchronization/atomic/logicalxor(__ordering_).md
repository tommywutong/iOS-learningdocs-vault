---
title: 'logicalXor(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/logicalxor(_:ordering:)'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/logicalxor(_:ordering:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/logicalxor%28_%3Aordering%3A%29.json'
content_hash: 'sha256:c12aa82d5bebf2d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# logicalXor(_:ordering:)

<sub>Instance Method</sub>

Perform an atomic logical XOR operation and return the old and new value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func logicalXor(_ operand: Bool, ordering: AtomicUpdateOrdering) -> (oldValue: Bool, newValue: Bool)
```

## Parameters

- `operand` — A boolean value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple with the old value before the operation and the new value after the operation.
