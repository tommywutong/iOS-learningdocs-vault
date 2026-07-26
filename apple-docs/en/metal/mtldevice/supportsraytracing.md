---
title: supportsRaytracing
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supportsraytracing
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsraytracing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsraytracing.json'
content_hash: 'sha256:777b7f27e5b46059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsRaytracing

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU device supports ray tracing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsRaytracing: Bool { get }
```

## See Also

### Checking render support

- [supportsPrimitiveMotionBlur](supportsprimitivemotionblur.md) — A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [supportsRaytracingFromRender](supportsraytracingfromrender.md) — A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [supports32BitMSAA](supports32bitmsaa.md) — A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [supportsPullModelInterpolation](supportspullmodelinterpolation.md) — A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [supportsShaderBarycentricCoordinates](supportsshaderbarycentriccoordinates.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [- supportsVertexAmplificationCount:](<supportsvertexamplificationcount(__).md>) — Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [programmableSamplePositionsSupported](areprogrammablesamplepositionssupported.md) — A Boolean value that indicates whether the GPU supports programmable sample positions.
- [rasterOrderGroupsSupported](arerasterordergroupssupported.md) — A Boolean value that indicates whether the GPU supports raster order groups.
- [barycentricCoordsSupported](arebarycentriccoordssupported.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates. _(deprecated)_
