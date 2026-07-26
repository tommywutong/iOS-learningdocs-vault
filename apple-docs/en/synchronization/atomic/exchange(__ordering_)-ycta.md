---
title: 'exchange(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/exchange(_:ordering:)-ycta'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/exchange(_:ordering:)-ycta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/exchange%28_%3Aordering%3A%29-ycta.json'
content_hash: 'sha256:f952189206983eb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# exchange(_:ordering:)

<sub>Instance Method</sub>

Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func exchange(_ desired: consuming Value, ordering: AtomicUpdateOrdering) -> Value
```

## Parameters

- `desired` — The desired new value.

- `ordering` — The memory ordering to apply on this operation.

## Return Value

The original value.
