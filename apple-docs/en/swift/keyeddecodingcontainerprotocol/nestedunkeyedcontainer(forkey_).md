---
title: 'nestedUnkeyedContainer(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainerprotocol/nestedunkeyedcontainer(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/nestedunkeyedcontainer(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol/nestedunkeyedcontainer%28forkey%3A%29.json'
content_hash: 'sha256:de1f1ea4f47749e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainerProtocol](../keyeddecodingcontainerprotocol.md)

# nestedUnkeyedContainer(forKey:)

<sub>Instance Method</sub>

Returns the data stored for the given key as represented in an unkeyed container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nestedUnkeyedContainer(forKey key: Self.Key) throws -> any UnkeyedDecodingContainer
```

## Parameters

- `key` — The key that the nested container is associated with.

## Return Value

An unkeyed decoding container view into `self`.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered stored value is not an unkeyed container.
