---
title: primitiveDataStride
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatastride
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatastride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor/primitivedatastride.json'
content_hash: 'sha256:694822aa64982642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureGeometryDescriptor](../mtl4accelerationstructuregeometrydescriptor.md)

# primitiveDataStride

<sub>Instance Property</sub>

Defines the stride, in bytes, between each primitive’s data in the primitive data buffer [primitiveDataBuffer](primitivedatabuffer.md) references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var primitiveDataStride: Int { get set }
```

## Discussion

You are responsible for ensuring the stride is at least [primitiveDataElementSize](primitivedataelementsize.md) in size and a multiple of 4 bytes.

This property defaults to `0` bytes,  which indicates the stride is equal to [primitiveDataElementSize](primitivedataelementsize.md).
