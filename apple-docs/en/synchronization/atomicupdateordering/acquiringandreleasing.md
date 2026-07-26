---
title: acquiringAndReleasing
framework: Synchronization
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicupdateordering/acquiringandreleasing
source_url: 'https://developer.apple.com/documentation/synchronization/atomicupdateordering/acquiringandreleasing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicupdateordering/acquiringandreleasing.json'
content_hash: 'sha256:71d010b5e338d845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicUpdateOrdering](../atomicupdateordering.md)

# acquiringAndReleasing

<sub>Type Property</sub>

An acquiring-and-releasing operation is a combination of `.acquiring` and `.releasing` operation on the same variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var acquiringAndReleasing: AtomicUpdateOrdering { get }
```

## Discussion

This value corresponds to `std::memory_order_acq_rel` in C++.
