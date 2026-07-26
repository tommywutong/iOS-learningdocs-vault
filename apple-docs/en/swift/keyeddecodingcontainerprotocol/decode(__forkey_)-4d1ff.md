---
title: 'decode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainerprotocol/decode(_:forkey:)-4d1ff'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decode(_:forkey:)-4d1ff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol/decode%28_%3Aforkey%3A%29-4d1ff.json'
content_hash: 'sha256:5537ab35ba8a16a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainerProtocol](../keyeddecodingcontainerprotocol.md)

# decode(_:forKey:)

<sub>Instance Method</sub>

Decodes a value of the given type for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode(_ type: UInt128.Type, forKey key: Self.Key) throws -> UInt128
```

## Parameters

- `type` — The type of value to decode.

- `key` — The key that the decoded value is associated with.

## Return Value

A value of the requested type, if present for the given key and convertible to the requested type.

## Discussion

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

> [!danger] Throws
> `DecodingError.keyNotFound` if `self` does not have an entry for the given key.

> [!danger] Throws
> `DecodingError.valueNotFound` if `self` has a null entry for the given key.

## Default Implementations

### KeyedDecodingContainerProtocol Implementations

- [decode(_:forKey:)](<decode(__forkey_)-7za3v.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<decode(__forkey_)-u839.md>) — Decodes a value of the given type for the given key.
