---
title: acquiring
framework: Synchronization
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicupdateordering/acquiring
source_url: 'https://developer.apple.com/documentation/synchronization/atomicupdateordering/acquiring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicupdateordering/acquiring.json'
content_hash: 'sha256:b7e5586663c55e4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicUpdateOrdering](../atomicupdateordering.md)

# acquiring

<sub>Type Property</sub>

An acquiring update synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var acquiring: AtomicUpdateOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_acquire` in C++.
