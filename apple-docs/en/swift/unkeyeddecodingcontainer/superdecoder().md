---
title: superDecoder()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyeddecodingcontainer/superdecoder()
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/superdecoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/superdecoder%28%29.json'
content_hash: 'sha256:543fe9f854471f19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# superDecoder()

<sub>Instance Method</sub>

Decodes a nested container and returns a `Decoder` instance for decoding `super` from that container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func superDecoder() throws -> any Decoder
```

## Return Value

A new `Decoder` to pass to `super.init(from:)`.

## Discussion

> [!danger] Throws
> `DecodingError.valueNotFound` if the encountered encoded value is null, or of there are no more values to decode.
