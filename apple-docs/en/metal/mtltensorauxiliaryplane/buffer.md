---
title: buffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/metal/mtltensorauxiliaryplane/buffer
source_url: 'https://developer.apple.com/documentation/metal/mtltensorauxiliaryplane/buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorauxiliaryplane/buffer.json'
content_hash: 'sha256:adbf047920a40ea3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorAuxiliaryPlane](../mtltensorauxiliaryplane.md)

# buffer

<sub>Instance Property</sub>

The buffer that provides the underlying storage for this plane, or `nil` if no buffer was provided at initialization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var buffer: (any MTLBuffer)? { get }
```
