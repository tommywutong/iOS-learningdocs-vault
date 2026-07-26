---
title: releasing
framework: Synchronization
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicupdateordering/releasing
source_url: 'https://developer.apple.com/documentation/synchronization/atomicupdateordering/releasing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicupdateordering/releasing.json'
content_hash: 'sha256:aeed66404c224d54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicUpdateOrdering](../atomicupdateordering.md)

# releasing

<sub>Type Property</sub>

A releasing update synchronizes with acquiring operations that read the value it stores. It ensures that the releasing and acquiring threads agree that all preceding variable accesses on the releasing thread happen before the atomic operation itself.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var releasing: AtomicUpdateOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_release` in C++.
