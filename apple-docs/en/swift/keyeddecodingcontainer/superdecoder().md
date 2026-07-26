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
doc_path: /documentation/swift/keyeddecodingcontainer/superdecoder()
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/superdecoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/superdecoder%28%29.json'
content_hash: 'sha256:b8a60d1df6ef1eaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# superDecoder()

<sub>Instance Method</sub>

Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func superDecoder() throws -> any Decoder
```

## Discussion

Equivalent to calling `superDecoder(forKey:)` with `Key(stringValue: "super", intValue: 0)`.

> [!danger] Throws
> `DecodingError.keyNotFound` if `self` does not have an entry for the default `super` key.

> [!danger] Throws
> `DecodingError.valueNotFound` if `self` has a null entry for the default `super` key.
