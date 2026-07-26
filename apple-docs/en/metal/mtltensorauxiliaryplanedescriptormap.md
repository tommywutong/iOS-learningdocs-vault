---
title: MTLTensorAuxiliaryPlaneDescriptorMap
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorauxiliaryplanedescriptormap
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplanedescriptormap.json'
content_hash: 'sha256:6484fe98233944e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTensorAuxiliaryPlaneDescriptorMap

<sub>Class</sub>

A map of auxiliary plane descriptors keyed by plane type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLTensorAuxiliaryPlaneDescriptorMap
```

## Overview

Use this collection to associate [MTLTensorPlaneType](mtltensorplanetype.md) values with [MTLTensorAuxiliaryPlaneDescriptor](mtltensorauxiliaryplanedescriptor.md) configurations, then attach it to a [MTLTensorDescriptor](mtltensordescriptor.md) to create a multi-plane tensor.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- descriptorForPlane:](<mtltensorauxiliaryplanedescriptormap/descriptor(for_).md>) — Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set. _(beta)_
- [- reset](<mtltensorauxiliaryplanedescriptormap/reset().md>) — Empties the map of all its elements. _(beta)_
- [- setDescriptor:forPlane:](<mtltensorauxiliaryplanedescriptormap/setdescriptor(__for_).md>) — Sets the auxiliary plane descriptor for the given plane type. _(beta)_
