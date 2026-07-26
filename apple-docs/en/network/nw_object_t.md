---
title: nw_object_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_object_t
source_url: 'https://developer.apple.com/documentation/network/nw_object_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_object_t.json'
content_hash: 'sha256:ccd8f2ecd07d0d88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_object_t

<sub>Type Alias</sub>

The generic type for objects in the Network framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_object_t = any OS_nw_object
```

## Discussion

Network.framework objects are reference-counted objects that can be used with Automatic Reference Counting (ARC) or directly retained and released.

The objects also conform to the description method of [NSObject](../objectivec/nsobject-swift.class.md) to be used for debugging.
