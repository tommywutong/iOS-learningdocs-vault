---
title: primitiveDataElementSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedataelementsize.json'
content_hash: 'sha256:2bf8a10c068c5a31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureGeometryDescriptor](../mtl4accelerationstructuregeometrydescriptor.md)

# primitiveDataElementSize

<sub>Instance Property</sub>

Sets the size, in bytes, of the data for each primitive in the primitive data buffer [primitiveDataBuffer](primitivedatabuffer.md) references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var primitiveDataElementSize: Int { get set }
```

## Discussion

This size needs to be at most [primitiveDataStride](primitivedatastride.md) in size and a multiple of 4 bytes.

This property defaults to 0 bytes.
