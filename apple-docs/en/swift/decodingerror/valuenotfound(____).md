---
title: 'DecodingError.valueNotFound(_:_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/valuenotfound(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/valuenotfound(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/valuenotfound%28_%3A_%3A%29.json'
content_hash: 'sha256:093d2f6f6cc02daa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# DecodingError.valueNotFound(_:_:)

<sub>Case</sub>

An indication that a non-optional value of the given type was expected, but a null value was found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case valueNotFound(any Any.Type, DecodingError.Context)
```

## Discussion

As associated values, this case contains the attempted type and context for debugging.
