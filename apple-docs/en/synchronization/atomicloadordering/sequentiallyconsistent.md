---
title: sequentiallyConsistent
framework: Synchronization
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicloadordering/sequentiallyconsistent
source_url: 'https://developer.apple.com/documentation/synchronization/atomicloadordering/sequentiallyconsistent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicloadordering/sequentiallyconsistent.json'
content_hash: 'sha256:38fb0fe7007cbae5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicLoadOrdering](../atomicloadordering.md)

# sequentiallyConsistent

<sub>Type Property</sub>

A sequentially consistent load performs an acquiring load and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var sequentiallyConsistent: AtomicLoadOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_seq_cst` in C++.
