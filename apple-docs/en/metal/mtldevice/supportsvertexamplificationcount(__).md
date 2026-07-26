---
title: 'supportsVertexAmplificationCount(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/supportsvertexamplificationcount(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsvertexamplificationcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsvertexamplificationcount%28_%3A%29.json'
content_hash: 'sha256:630928ea9e9f70fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsVertexAmplificationCount(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the GPU supports an amplification factor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsVertexAmplificationCount(_ count: Int) -> Bool
```

## Parameters

- `count` — An integer that represents the number of output streams you want the GPU to generate from an input stream.

## Discussion

A vertex amplification factor of `1` has no effect because it effectively disables vertex amplification.

> [!important] Important
> Passing a vertex amplification factor of `1` or less to this method triggers an API validation error.

For more information about vertex amplification, see [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md).

## See Also

### Checking render support

- [supportsRaytracing](supportsraytracing.md) — A Boolean value that indicates whether the GPU device supports ray tracing.
- [supportsPrimitiveMotionBlur](supportsprimitivemotionblur.md) — A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [supportsRaytracingFromRender](supportsraytracingfromrender.md) — A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [supports32BitMSAA](supports32bitmsaa.md) — A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [supportsPullModelInterpolation](supportspullmodelinterpolation.md) — A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [supportsShaderBarycentricCoordinates](supportsshaderbarycentriccoordinates.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [programmableSamplePositionsSupported](areprogrammablesamplepositionssupported.md) — A Boolean value that indicates whether the GPU supports programmable sample positions.
- [rasterOrderGroupsSupported](arerasterordergroupssupported.md) — A Boolean value that indicates whether the GPU supports raster order groups.
- [barycentricCoordsSupported](arebarycentriccoordssupported.md) — A Boolean value that indicates whether the GPU supports barycentric coordinates. _(deprecated)_
