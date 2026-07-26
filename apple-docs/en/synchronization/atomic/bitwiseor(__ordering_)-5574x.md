---
title: 'bitwiseOr(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/bitwiseor(_:ordering:)-5574x'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/bitwiseor(_:ordering:)-5574x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/bitwiseor%28_%3Aordering%3A%29-5574x.json'
content_hash: 'sha256:62a21d045e210ab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# bitwiseOr(_:ordering:)

<sub>Instance Method</sub>

Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func bitwiseOr(_ operand: UInt128, ordering: AtomicUpdateOrdering) -> (oldValue: UInt128, newValue: UInt128)
```

## Parameters

- `operand` — An integer value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple containing the original value before the operation and the new value after the operation.
