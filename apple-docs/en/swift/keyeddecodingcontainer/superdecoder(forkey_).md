---
title: 'superDecoder(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/superdecoder(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/superdecoder(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/superdecoder%28forkey%3A%29.json'
content_hash: 'sha256:3b84f3e14f7b5e4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# superDecoder(forKey:)

<sub>Instance Method</sub>

Returns a `Decoder` instance for decoding `super` from the container associated with the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func superDecoder(forKey key: KeyedDecodingContainer<K>.Key) throws -> any Decoder
```

## Parameters

- `key` — The key to decode `super` for.

## Return Value

A new `Decoder` to pass to `super.init(from:)`.

## Discussion

> [!danger] Throws
> `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> [!danger] Throws
> `DecodingError.valueNotFound` if `self` has a null entry for the given key.
