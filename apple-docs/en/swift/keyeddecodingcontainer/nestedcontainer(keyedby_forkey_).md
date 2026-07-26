---
title: 'nestedContainer(keyedBy:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/nestedcontainer(keyedby:forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/nestedcontainer(keyedby:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/nestedcontainer%28keyedby%3Aforkey%3A%29.json'
content_hash: 'sha256:bdce730600a3a0ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# nestedContainer(keyedBy:forKey:)

<sub>Instance Method</sub>

Returns the data stored for the given key as represented in a container keyed by the given key type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type, forKey key: KeyedDecodingContainer<K>.Key) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey
```

## Parameters

- `type` — The key type to use for the container.

- `key` — The key that the nested container is associated with.

## Return Value

A keyed decoding container view into `self`.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not a keyed container.
