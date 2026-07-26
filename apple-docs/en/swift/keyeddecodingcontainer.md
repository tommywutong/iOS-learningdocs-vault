---
title: KeyedDecodingContainer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyeddecodingcontainer
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer.json'
content_hash: 'sha256:dc0fd6f247011dbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# KeyedDecodingContainer

<sub>Structure</sub>

A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct KeyedDecodingContainer<K> where K : CodingKey
```

## Relationships

- **Conforms To**: [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md)

## Topics

### Initializers

- [init(_:)](<keyeddecodingcontainer/init(__).md>) — Creates a new instance with the given container.

### Instance Properties

- [allKeys](keyeddecodingcontainer/allkeys.md) — All the keys the decoder has for this container.
- [codingPath](keyeddecodingcontainer/codingpath.md) — The path of coding keys taken to get to this point in decoding.

### Instance Methods

- [contains(_:)](<keyeddecodingcontainer/contains(__).md>) — Returns a Boolean value indicating whether the decoder contains a value associated with the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-1d33g.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-1n3v.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-1u4zx.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-21ybk.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-3e257.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-3egly.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-3yw73.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-4mzei.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-5fh1x.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-5io1a.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-687gv.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-6d98c.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-721nc.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-7vj8e.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-8foeb.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-8u7rt.md>)
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-9633o.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:)](<keyeddecodingcontainer/decode(__forkey_)-9fa2u.md>) — Decodes a value of the given type for the given key.
- [decode(_:forKey:configuration:)](<keyeddecodingcontainer/decode(__forkey_configuration_)-2rk0t.md>)
- [decode(_:forKey:configuration:)](<keyeddecodingcontainer/decode(__forkey_configuration_)-6t8ew.md>)
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-1iwt4.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-1zmt1.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-23pwi.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-2ax45.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-2hn6i.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-2thz1.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-2yvgn.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-3thus.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-6zxms.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-74ir4.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-7ucyl.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-7x3cg.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-85fg3.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-897x4.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-8tib2.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-91iaz.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:)](<keyeddecodingcontainer/decodeifpresent(__forkey_)-9fnqb.md>) — Decodes a value of the given type for the given key, if present.
- [decodeIfPresent(_:forKey:configuration:)](<keyeddecodingcontainer/decodeifpresent(__forkey_configuration_)-469qf.md>)
- [decodeIfPresent(_:forKey:configuration:)](<keyeddecodingcontainer/decodeifpresent(__forkey_configuration_)-5g1cl.md>)
- [decodeNil(forKey:)](<keyeddecodingcontainer/decodenil(forkey_).md>) — Decodes a null value for the given key.
- [decodePredicateExpression(forKey:input:output:predicateConfiguration:)](<keyeddecodingcontainer/decodepredicateexpression(forkey_input_output_predicateconfiguration_).md>)
- [decodePredicateExpression(forKey:input:predicateConfiguration:)](<keyeddecodingcontainer/decodepredicateexpression(forkey_input_predicateconfiguration_).md>)
- [decodePredicateExpressionIfPresent(forKey:input:output:predicateConfiguration:)](<keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey_input_output_predicateconfiguration_).md>)
- [decodePredicateExpressionIfPresent(forKey:input:predicateConfiguration:)](<keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey_input_predicateconfiguration_).md>)
- [nestedContainer(keyedBy:forKey:)](<keyeddecodingcontainer/nestedcontainer(keyedby_forkey_).md>) — Returns the data stored for the given key as represented in a container keyed by the given key type.
- [nestedUnkeyedContainer(forKey:)](<keyeddecodingcontainer/nestedunkeyedcontainer(forkey_).md>) — Returns the data stored for the given key as represented in an unkeyed container.
- [superDecoder()](<keyeddecodingcontainer/superdecoder().md>) — Returns a `Decoder` instance for decoding `super` from the container associated with the default `super` key.
- [superDecoder(forKey:)](<keyeddecodingcontainer/superdecoder(forkey_).md>) — Returns a `Decoder` instance for decoding `super` from the container associated with the given key.

### Type Aliases

- [Key](keyeddecodingcontainer/key.md)

### Default Implementations

- [KeyedDecodingContainerProtocol Implementations](keyeddecodingcontainer/keyeddecodingcontainerprotocol-implementations.md)

## See Also

### Decoding Containers

- [SingleValueDecodingContainer](singlevaluedecodingcontainer.md) — A container that can support the storage and direct decoding of a single nonkeyed value.
- [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
- [UnkeyedDecodingContainer](unkeyeddecodingcontainer.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.
