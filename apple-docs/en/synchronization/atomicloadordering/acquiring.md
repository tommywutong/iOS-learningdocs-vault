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
doc_path: /documentation/synchronization/atomicloadordering/acquiring
source_url: 'https://developer.apple.com/documentation/synchronization/atomicloadordering/acquiring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicloadordering/acquiring.json'
content_hash: 'sha256:e2f92fd4dd57bf09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicLoadOrdering](../atomicloadordering.md)

# acquiring

<sub>Type Property</sub>

An acquiring load synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var acquiring: AtomicLoadOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_acquire` in C++.
