---
title: relaxed
framework: Synchronization
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicupdateordering/relaxed
source_url: 'https://developer.apple.com/documentation/synchronization/atomicupdateordering/relaxed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicupdateordering/relaxed.json'
content_hash: 'sha256:9153bd2fa03eb32a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicUpdateOrdering](../atomicupdateordering.md)

# relaxed

<sub>Type Property</sub>

Guarantees the atomicity of the specific operation on which it is applied, but imposes no ordering constraints on any other variable accesses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var relaxed: AtomicUpdateOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_relaxed` in C++.
