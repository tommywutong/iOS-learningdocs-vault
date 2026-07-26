---
title: 'decodeNil(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainerprotocol/decodenil(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decodenil(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol/decodenil%28forkey%3A%29.json'
content_hash: 'sha256:58a44c8284768e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainerProtocol](../keyeddecodingcontainerprotocol.md)

# decodeNil(forKey:)

<sub>Instance Method</sub>

Decodes a null value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeNil(forKey key: Self.Key) throws -> Bool
```

## Parameters

- `key` — The key that the decoded value is associated with.

## Return Value

Whether the encountered value was null.

## Discussion

> [!danger] Throws
> `DecodingError.keyNotFound` if `self` does not have an entry for the given key.
