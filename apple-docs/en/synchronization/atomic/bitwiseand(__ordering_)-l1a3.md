---
title: 'bitwiseAnd(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/bitwiseand(_:ordering:)-l1a3'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/bitwiseand(_:ordering:)-l1a3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/bitwiseand%28_%3Aordering%3A%29-l1a3.json'
content_hash: 'sha256:23d7b6ab4ee2964b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# bitwiseAnd(_:ordering:)

<sub>Instance Method</sub>

Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func bitwiseAnd(_ operand: UInt8, ordering: AtomicUpdateOrdering) -> (oldValue: UInt8, newValue: UInt8)
```

## Parameters

- `operand` — An integer value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple containing the original value before the operation and the new value after the operation.
