---
title: dispatch_data_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_t.json'
content_hash: 'sha256:681ab99b8445d630'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_t

<sub>Type Alias</sub>

An immutable object representing a contiguous or sparse region of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_data_t = __DispatchData
```

## Discussion

Any direct access to the memory in a dispatch data object must not modify that memory.

In 64-bit apps, you may cast a [dispatch_data_t](dispatch_data_t.md) type to an [NSData](../foundation/nsdata.md) object. However, you may not perform a reverse cast — that is, cast an [NSData](../foundation/nsdata.md) object to a [dispatch_data_t](dispatch_data_t.md) type.
