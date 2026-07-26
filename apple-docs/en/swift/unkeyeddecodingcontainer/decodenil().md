---
title: decodeNil()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyeddecodingcontainer/decodenil()
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodenil()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodenil%28%29.json'
content_hash: 'sha256:d2e27b6165ec44be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodeNil()

<sub>Instance Method</sub>

Decodes a null value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodeNil() throws -> Bool
```

## Return Value

Whether the encountered value was null.

## Discussion

If the value is not null, does not increment currentIndex.

> [!danger] Throws
> `DecodingError.valueNotFound` if there are no more values to decode.
