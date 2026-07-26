---
title: 'DecodingError.keyNotFound(_:_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/keynotfound(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/keynotfound(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/keynotfound%28_%3A_%3A%29.json'
content_hash: 'sha256:02f9474500d8cce5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# DecodingError.keyNotFound(_:_:)

<sub>Case</sub>

An indication that a keyed decoding container was asked for an entry for the given key, but did not contain one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case keyNotFound(any CodingKey, DecodingError.Context)
```

## Discussion

As associated values, this case contains the attempted key and context for debugging.
