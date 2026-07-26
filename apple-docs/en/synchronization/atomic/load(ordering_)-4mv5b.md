---
title: 'load(ordering:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomic/load(ordering:)-4mv5b'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/load(ordering:)-4mv5b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/load%28ordering%3A%29-4mv5b.json'
content_hash: 'sha256:61b2863e8d89b8f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [Atomic](../atomic.md)

# load(ordering:)

<sub>Instance Method</sub>

Atomically loads and returns the current value, applying the specified memory ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load(ordering: AtomicLoadOrdering) -> Value
```

## Parameters

- `ordering` — The memory ordering to apply on this operation.

## Return Value

The current value.
