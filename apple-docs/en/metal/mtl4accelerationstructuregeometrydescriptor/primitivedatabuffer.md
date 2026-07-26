---
title: primitiveDataBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatabuffer.json'
content_hash: 'sha256:09e95c7e2e9d15ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureGeometryDescriptor](../mtl4accelerationstructuregeometrydescriptor.md)

# primitiveDataBuffer

<sub>Instance Property</sub>

Assigns optional buffer containing data to associate with each primitive in this geometry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var primitiveDataBuffer: MTL4BufferRange { get set }
```

## Discussion

You can use zero as the buffer address in this buffer range.
