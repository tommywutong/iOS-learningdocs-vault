---
title: 'store(_:ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/store(_:ordering:)-22zxw'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/store(_:ordering:)-22zxw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/store%28_%3Aordering%3A%29-22zxw.json'
content_hash: 'sha256:c78f24e3702eea64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# store(_:ordering:)

<sub>Instance Method</sub>

Atomically sets the current value to `desired`, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func store(_ desired: consuming Value, ordering: AtomicStoreOrdering)
```

## Parameters

- `desired` — The desired new value.

- `ordering` — The memory ordering to apply on this operation.
