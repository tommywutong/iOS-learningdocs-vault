---
title: allKeys
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyeddecodingcontainer/allkeys
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/allkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/allkeys.json'
content_hash: 'sha256:a0a430f2667243f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# allKeys

<sub>Instance Property</sub>

All the keys the decoder has for this container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allKeys: [KeyedDecodingContainer<K>.Key] { get }
```

## Discussion

Different keyed containers from the same decoder may return different keys here, because it is possible to encode with multiple key types which are not convertible to one another. This should report all keys present which are convertible to the requested type.
