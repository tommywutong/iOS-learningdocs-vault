---
title: KeyedDecodingContainerProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyeddecodingcontainerprotocol
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainerprotocol.json'
content_hash: 'sha256:777664d490df821e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# KeyedDecodingContainerProtocol

<sub>Protocol</sub>

A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol KeyedDecodingContainerProtocol
```

## Overview

Decoders should provide types conforming to `UnkeyedDecodingContainer` for their format.

## Relationships

- **Conforming Types**: [KeyedDecodingContainer](keyeddecodingcontainer.md)

## Topics

### Associated Types

- [Key](keyeddecodingcontainerprotocol/key.md)

### Instance Properties

- [allKeys](keyeddecodingcontainerprotocol/allkeys.md) — All the keys the `Decoder` has for this container.
- [codingPath](keyeddecodingcontainerprotocol/codingpath.md) — The path of coding keys taken to get to this point in decoding.

### Instance Methods

- [contains(_:)](<keyeddecodingcontainerprotocol/contains(__).md>) — Returns a Boolean value indicating whether the decoder contains a value associated with the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-1pd5k.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-2sa7a.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-3cyg.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-3zluy.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-43hen.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-4d1ff.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-4k53i.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-5jtvg.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-5kzmf.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-62kn6.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-873gm.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-880hl.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-8h5vd.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-decq.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-kecy.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-p613.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainerprotocol/decode(__forkey_)-xuqk.md>) — Decodes a value of the given type for the given key.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-17w89.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-1qynx.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-1saky.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-375xf.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-39kc6.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-3pes5.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-5bqjw.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-5k5md.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-5ymbd.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-6n52q.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-6vzzs.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-7a1da.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-7jjj2.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-7opy8.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-7p1j1.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-8qp1h.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainerprotocol/decodeifpresent(__forkey_)-lc54.md>) — Decodes a value of the given type for the given key, if present.
- [decodeNil(forKey:)](<keyeddecodingcontainerprotocol/decodenil(forkey_).md>) — Decodes a null value for the given key.
- [nestedContainer(keyedBy:forKey:)](<keyeddecodingcontainerprotocol/nestedcontainer(keyedby_forkey_).md>) — Returns the data stored for the given key as represented in a container keyed by the given key type.
- [nestedUnkeyedContainer(forKey:)](<keyeddecodingcontainerprotocol/nestedunkeyedcontainer(forkey_).md>) — Returns the data stored for the given key as represented in an unkeyed container.
- [superDecoder()](<keyeddecodingcontainerprotocol/superdecoder().md>) — Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.
- [superDecoder(forKey:)](<keyeddecodingcontainerprotocol/superdecoder(forkey_).md>) — Returns a `Decoder` instance for decoding `super` from the container associated with the given key.

## See Also

### Decoding Containers

- [KeyedDecodingContainer](keyeddecodingcontainer.md) — A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [SingleValueDecodingContainer](singlevaluedecodingcontainer.md) — A container that can support the storage and direct decoding of a single nonkeyed value.
- [UnkeyedDecodingContainer](unkeyeddecodingcontainer.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.
