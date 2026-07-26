---
title: UnkeyedEncodingContainer
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unkeyedencodingcontainer
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer.json'
content_hash: 'sha256:a077b4c6d9424b47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnkeyedEncodingContainer

<sub>Protocol</sub>

A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol UnkeyedEncodingContainer
```

## Overview

Encoders should provide types conforming to `UnkeyedEncodingContainer` for their format.

## Topics

### Instance Properties

- [codingPath](unkeyedencodingcontainer/codingpath.md) — The path of coding keys taken to get to this point in encoding.
- [count](unkeyedencodingcontainer/count.md) — The number of elements encoded into the container.

### Instance Methods

- [encode(_:)](<unkeyedencodingcontainer/encode(__)-1rqbg.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-1yl36.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-24em8.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-30ux3.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-3dtgb.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-4ehqa.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-6460j.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-6jau2.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-6moq8.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-6o2fd.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-784h2.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-7cs0h.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-7vq.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-7za3t.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-9d3m0.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-9k4uf.md>) — Encodes the given value.
- [encode(_:)](<unkeyedencodingcontainer/encode(__)-9sz81.md>) — Encodes the given value.
- [encode(_:configuration:)](<unkeyedencodingcontainer/encode(__configuration_)-3y681.md>)
- [encode(_:configuration:)](<unkeyedencodingcontainer/encode(__configuration_)-85f4v.md>)
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-19w8r.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-2bav9.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-36ny.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-3upp3.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-4tdyr.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-54d9i.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-58k1b.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-62wy5.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-7m806.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-862ok.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-89pyf.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-8d3h.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-8vtn5.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-9s06k.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-9sogk.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-kdw8.md>) — Encodes the elements of the given sequence.
- [encode(contentsOf:)](<unkeyedencodingcontainer/encode(contentsof_)-xykc.md>) — Encodes the elements of the given sequence.
- [encodeConditional(_:)](<unkeyedencodingcontainer/encodeconditional(__).md>) — Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [encodeNil()](<unkeyedencodingcontainer/encodenil().md>) — Encodes a null value.
- [encodePredicateExpression(_:variable:predicateConfiguration:)](<unkeyedencodingcontainer/encodepredicateexpression(__variable_predicateconfiguration_)-30xlk.md>)
- [encodePredicateExpression(_:variable:predicateConfiguration:)](<unkeyedencodingcontainer/encodepredicateexpression(__variable_predicateconfiguration_)-3p9ec.md>)
- [encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)](<unkeyedencodingcontainer/encodepredicateexpressionifpresent(__variable_predicateconfiguration_)-438on.md>)
- [encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)](<unkeyedencodingcontainer/encodepredicateexpressionifpresent(__variable_predicateconfiguration_)-75j8t.md>)
- [nestedContainer(keyedBy:)](<unkeyedencodingcontainer/nestedcontainer(keyedby_).md>) — Encodes a nested container keyed by the given type and returns it.
- [nestedUnkeyedContainer()](<unkeyedencodingcontainer/nestedunkeyedcontainer().md>) — Encodes an unkeyed encoding container and returns it.
- [superEncoder()](<unkeyedencodingcontainer/superencoder().md>) — Encodes a nested container and returns an `Encoder` instance for encoding `super` into that container.

## See Also

### Encoding Containers

- [SingleValueEncodingContainer](singlevalueencodingcontainer.md) — A container that can support the storage and direct encoding of a single non-keyed value.
- [KeyedEncodingContainer](keyedencodingcontainer.md) — A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
