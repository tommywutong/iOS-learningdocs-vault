---
title: 'container(keyedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decoder/container(keyedby:)'
source_url: 'https://developer.apple.com/documentation/swift/decoder/container(keyedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decoder/container%28keyedby%3A%29.json'
content_hash: 'sha256:e127366e9099237c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Decoder](../decoder.md)

# container(keyedBy:)

<sub>Instance Method</sub>

Returns the data stored in this decoder as represented in a container keyed by the given key type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func container<Key>(keyedBy type: Key.Type) throws -> KeyedDecodingContainer<Key> where Key : CodingKey
```

## Parameters

- `type` — The key type to use for the container.

## Return Value

A keyed decoding container view into this decoder.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.
