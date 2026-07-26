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
doc_path: '/documentation/synchronization/atomic/load(ordering:)-3u18o'
source_url: 'https://developer.apple.com/documentation/synchronization/atomic/load(ordering:)-3u18o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic/load%28ordering%3A%29-3u18o.json'
content_hash: 'sha256:975cf6b48d428e48'
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
