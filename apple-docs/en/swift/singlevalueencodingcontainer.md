---
title: SingleValueEncodingContainer
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/singlevalueencodingcontainer
source_url: 'https://developer.apple.com/documentation/swift/singlevalueencodingcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/singlevalueencodingcontainer.json'
content_hash: 'sha256:0617f2c1d0968dac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SingleValueEncodingContainer

<sub>Protocol</sub>

A container that can support the storage and direct encoding of a single non-keyed value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SingleValueEncodingContainer
```

## Topics

### Instance Properties

- [codingPath](singlevalueencodingcontainer/codingpath.md) — The path of coding keys taken to get to this point in encoding.

### Instance Methods

- [encode(_:)](<singlevalueencodingcontainer/encode(__)-1mftu.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-23skf.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-2c14h.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-2oplx.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-39vhy.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-44wsc.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-5111.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-512uf.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-5fuor.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-5kf5u.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-5ndtj.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-687yj.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-6a9w5.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-7alir.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-9mmv6.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-hruu.md>) — Encodes a single value of the given type.
- [encode(_:)](<singlevalueencodingcontainer/encode(__)-r5hk.md>) — Encodes a single value of the given type.
- [encodeNil()](<singlevalueencodingcontainer/encodenil().md>) — Encodes a null value.

## See Also

### Encoding Containers

- [KeyedEncodingContainer](keyedencodingcontainer.md) — A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [UnkeyedEncodingContainer](unkeyedencodingcontainer.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.
