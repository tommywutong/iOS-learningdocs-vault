---
title: MTLTensorAuxiliaryPlaneDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorauxiliaryplanedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplanedescriptor.json'
content_hash: 'sha256:86297cf5b0b03c49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorAuxiliaryPlaneDescriptor

<sub>Class</sub>

A configuration for an auxiliary plane in a multi-plane tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorAuxiliaryPlaneDescriptor
```

## Overview

Use this descriptor to configure an auxiliary plane’s data type and block factors before attaching it to a [MTLTensorDescriptor](mtltensordescriptor.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [blockFactors](mtltensorauxiliaryplanedescriptor/blockfactors.md) — An extents instance that represents the number of data plane elements which correspond to one element in a plane you create with this descriptor. _(beta)_
- [dataType](mtltensorauxiliaryplanedescriptor/datatype.md) — The data format of all elements in the plane. _(beta)_
