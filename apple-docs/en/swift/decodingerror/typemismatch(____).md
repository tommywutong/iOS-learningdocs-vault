---
title: 'DecodingError.typeMismatch(_:_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/typemismatch(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/typemismatch(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/typemismatch%28_%3A_%3A%29.json'
content_hash: 'sha256:d15a762c322f2ee7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# DecodingError.typeMismatch(_:_:)

<sub>Case</sub>

An indication that a value of the given type could not be decoded because it did not match the type of what was found in the encoded payload.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case typeMismatch(any Any.Type, DecodingError.Context)
```

## Discussion

As associated values, this case contains the attempted type and context for debugging.
