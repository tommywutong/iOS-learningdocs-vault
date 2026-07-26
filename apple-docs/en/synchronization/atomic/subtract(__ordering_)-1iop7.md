---
title: 'subtract(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/subtract(_:ordering:)-1iop7'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/subtract(_:ordering:)-1iop7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/subtract%28_%3Aordering%3A%29-1iop7.json'
content_hash: 'sha256:452806665ec6d87e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# subtract(_:ordering:)

<sub>Instance Method</sub>

Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func subtract(_ operand: Int, ordering: AtomicUpdateOrdering) -> (oldValue: Int, newValue: Int)
```

## Parameters

- `operand` — An integer value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

A tuple containing the original value before the operation and the new value after the operation.

## Discussion

> [!note] Note
> This operation checks for overflow at runtime and will trap if an overflow does occur. In `-Ounchecked` builds, overflow checking is not performed.
>
> The need to check for overflow means that this operation is typically compiled into a compare-exchange loop. For use cases that require a direct atomic subtraction, see the `wrappingSubtract` operation: it avoids the loop, but in exchange it allows silent wraps on overflow.
