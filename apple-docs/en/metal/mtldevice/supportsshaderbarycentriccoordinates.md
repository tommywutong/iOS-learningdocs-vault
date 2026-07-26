---
title: supportsShaderBarycentricCoordinates
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supportsshaderbarycentriccoordinates
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsshaderbarycentriccoordinates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsshaderbarycentriccoordinates.json'
content_hash: 'sha256:48fc213d94a30c0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsShaderBarycentricCoordinates

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU supports barycentric coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsShaderBarycentricCoordinates: Bool { get }
```

## Discussion

If a GPU device supports barycentric coordinates, a fragment shader can receive them by adding the `[[barycentric_coord]]` attribute to one of its arguments. See the [Metal Shading Language specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) and [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md) for more information.

## See Also

### Checking render support

- [supportsRaytracing](supportsraytracing.md) — A Boolean value that indicates whether the GPU device supports ray tracing.
- [supportsPrimitiveMotionBlur](supportsprimitivemotionblur.md) — A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [supportsRaytracingFromRender](supportsraytracingfromrender.md) — A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [supports32BitMSAA](supports32bitmsaa.md) — A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [supportsPullModelInterpolation](supportspullmodelinterpolation.md) — A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [- supportsVertexAmplificationCount:](<supportsvertexamplificationcount(__).md>) — Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [programmableSamplePositionsSupported](areprogrammablesamplepositionssupported.md) — A Boolean value that indicates whether the GPU supports programmable sample positions.
- [rasterOrderGroupsSupported](arerasterordergroupssupported.md) — A Boolean value that indicates whether the GPU supports raster order groups.
- [barycentricCoordsSupported](arebarycentriccoordssupported.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates. _(deprecated)_
