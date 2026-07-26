---
title: UnkeyedDecodingContainer
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyeddecodingcontainer
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer.json'
content_hash: 'sha256:8da8bfafe0f27487'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnkeyedDecodingContainer

<sub>Protocol</sub>

A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type sequentially, without keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UnkeyedDecodingContainer
```

## Overview

Decoders should provide types conforming to `UnkeyedDecodingContainer` for their format.

## Topics

### Instance Properties

- [codingPath](unkeyeddecodingcontainer/codingpath.md) — The path of coding keys taken to get to this point in decoding.
- [count](unkeyeddecodingcontainer/count.md) — The number of elements contained within this container.
- [currentIndex](unkeyeddecodingcontainer/currentindex.md) — The current decoding index of the container (i.e. the index of the next element to be decoded.) Incremented after every successful decode call.
- [isAtEnd](unkeyeddecodingcontainer/isatend.md) — A Boolean value indicating whether there are no more elements left to be decoded in the container.

### Instance Methods

- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-1jjjp.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-276l5.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-2jd5t.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-30psn.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-499mt.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-4cm6k.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-5eszo.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-5kbz9.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-66zb4.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-6o9j1.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-7gp3y.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-83ekt.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-8g0io.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-96zc5.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-9gfvr.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-gn40.md>) — Decodes a value of the given type.
- [decode(_:)](<unkeyeddecodingcontainer/decode(__)-nztw.md>) — Decodes a value of the given type.
- [decode(_:configuration:)](<unkeyeddecodingcontainer/decode(__configuration_)-3q1ra.md>)
- [decode(_:configuration:)](<unkeyeddecodingcontainer/decode(__configuration_)-72ctg.md>)
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-1lbyq.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-1oxo9.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-24deb.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-2n0nb.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-4d6xc.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-599d9.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-5t8p7.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-62i7k.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-6aqhk.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-6d53.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-6j7g9.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-6uoka.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-7dfq.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-80st4.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-86f1g.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-gxli.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:)](<unkeyeddecodingcontainer/decodeifpresent(__)-n5tj.md>) — Decodes a value of the given type, if present.
- [decodeIfPresent(_:configuration:)](<unkeyeddecodingcontainer/decodeifpresent(__configuration_)-3i2jl.md>)
- [decodeIfPresent(_:configuration:)](<unkeyeddecodingcontainer/decodeifpresent(__configuration_)-7nafo.md>)
- [decodeNil()](<unkeyeddecodingcontainer/decodenil().md>) — Decodes a null value.
- [decodePredicateExpression(input:output:predicateConfiguration:)](<unkeyeddecodingcontainer/decodepredicateexpression(input_output_predicateconfiguration_).md>)
- [decodePredicateExpression(input:predicateConfiguration:)](<unkeyeddecodingcontainer/decodepredicateexpression(input_predicateconfiguration_).md>)
- [decodePredicateExpressionIfPresent(input:output:predicateConfiguration:)](<unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input_output_predicateconfiguration_).md>)
- [decodePredicateExpressionIfPresent(input:predicateConfiguration:)](<unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input_predicateconfiguration_).md>)
- [nestedContainer(keyedBy:)](<unkeyeddecodingcontainer/nestedcontainer(keyedby_).md>) — Decodes a nested container keyed by the given type.
- [nestedUnkeyedContainer()](<unkeyeddecodingcontainer/nestedunkeyedcontainer().md>) — Decodes an unkeyed nested container.
- [superDecoder()](<unkeyeddecodingcontainer/superdecoder().md>) — Decodes a nested container and returns a `Decoder` instance for decoding `super` from that container.

## See Also

### Decoding Containers

- [KeyedDecodingContainer](keyeddecodingcontainer.md) — A concrete container that provides a view into a decoder’s storage, making the encoded properties of a decodable type accessible by keys.
- [SingleValueDecodingContainer](singlevaluedecodingcontainer.md) — A container that can support the storage and direct decoding of a single nonkeyed value.
- [KeyedDecodingContainerProtocol](keyeddecodingcontainerprotocol.md) — A type that provides a view into a decoder’s storage and is used to hold the encoded properties of a decodable type in a keyed manner.
