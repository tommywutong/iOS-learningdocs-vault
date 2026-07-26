---
title: 'decodeIfPresent(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-3pes5'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/decodeifpresent(_:forkey:)-3pes5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol/decodeifpresent%28_%3Aforkey%3A%29-3pes5.json'
content_hash: 'sha256:4f1db7e6d806f1f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainerProtocol](../keyeddecodingcontainerprotocol.md)

# decodeIfPresent(_:forKey:)

<sub>Instance Method</sub>

Decodes a value of the given type for the given key, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeIfPresent(_ type: Int32.Type, forKey key: Self.Key) throws -> Int32?
```

## Parameters

- `type` — The type of value to decode.

- `key` — The key that the decoded value is associated with.

## Return Value

A decoded value of the requested type, or `nil` if the `Decoder` does not have an entry associated with the given key, or if the value is a null value.

## Discussion

This method returns `nil` if the container does not have a value associated with `key`, or if the value is null. The difference between these states can be distinguished with a `contains(_:)` call.

> [!danger] Throws
> `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Default Implementations

### KeyedDecodingContainerProtocol Implementations

- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-189q8.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-1i7qt.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-2g0dg.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-2o9mb.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-4j3g5.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-5vg9.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-613fl.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-6d6xo.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-6lga8.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-6ze9z.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-8cej4.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-8l1ao.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-8ujl.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-8w7i2.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-8wk2a.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-fyzb.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<decodeifpresent(__forkey_)-g4cp.md>) — Decodes a value of the given type for the given key, if present.
