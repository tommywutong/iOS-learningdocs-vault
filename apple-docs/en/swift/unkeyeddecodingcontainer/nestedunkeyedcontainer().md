---
title: nestedUnkeyedContainer()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyeddecodingcontainer/nestedunkeyedcontainer()
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/nestedunkeyedcontainer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/nestedunkeyedcontainer%28%29.json'
content_hash: 'sha256:d0f67210a21eae6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# nestedUnkeyedContainer()

<sub>Instance Method</sub>

Decodes an unkeyed nested container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nestedUnkeyedContainer() throws -> any UnkeyedDecodingContainer
```

## Return Value

An unkeyed decoding container view into `self`.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not an unkeyed container.
