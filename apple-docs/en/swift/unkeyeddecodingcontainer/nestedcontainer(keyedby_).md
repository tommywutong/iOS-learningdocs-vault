---
title: 'nestedContainer(keyedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/nestedcontainer(keyedby:)'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/nestedcontainer(keyedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/nestedcontainer%28keyedby%3A%29.json'
content_hash: 'sha256:5f99c6b5d1b016fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# nestedContainer(keyedBy:)

<sub>Instance Method</sub>

Decodes a nested container keyed by the given type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey
```

## Parameters

- `type` — The key type to use for the container.

## Return Value

A keyed decoding container view into `self`.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.
