---
title: MTLTensorAuxiliaryPlane
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorauxiliaryplane
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplane'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplane.json'
content_hash: 'sha256:68b85ec9d9bcb446'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorAuxiliaryPlane

<sub>Protocol</sub>

A type that represents the configuration and storage of an auxiliary plane in a multi-plane tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLTensorAuxiliaryPlane : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [blockFactors](mtltensorauxiliaryplane/blockfactors.md) — The number of data plane elements that correspond to one element in this auxiliary plane. _(beta)_
- [buffer](mtltensorauxiliaryplane/buffer.md) — The buffer that provides the underlying storage for this plane, or `nil` if no buffer was provided at initialization. _(beta)_
- [bufferOffset](mtltensorauxiliaryplane/bufferoffset.md) — The byte offset into [buffer](mtltensorauxiliaryplane/buffer.md) where this plane’s data begins, or `0` if no buffer was provided at initialization. _(beta)_
- [dataType](mtltensorauxiliaryplane/datatype.md) — The data format of all elements in the plane. _(beta)_
- [planeType](mtltensorauxiliaryplane/planetype.md) — The type of information this plane stores. _(beta)_
