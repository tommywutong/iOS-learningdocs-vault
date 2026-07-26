---
title: normalizedCoordinates
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/normalizedcoordinates
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/normalizedcoordinates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/normalizedcoordinates.json'
content_hash: 'sha256:7177b3c94301c53a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# normalizedCoordinates

<sub>Instance Property</sub>

A Boolean value that indicates whether texture coordinates are normalized to the range `[0.0, 1.0]`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var normalizedCoordinates: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), texture coordinates are from `0.0` to `1.0`. If [false](../../swift/false.md), texture coordinates are from `0` to `width` for horizontal coordinates and `0` to `height` for vertical coordinates. The default value is [true](../../swift/true.md).

Non-normalized texture coordinates should only be used with 1D and 2D textures with the following conditions; otherwise, the results of sampling are undefined.

- The [MTLSamplerAddressModeClampToEdge](../mtlsampleraddressmode/clamptoedge.md) or [MTLSamplerAddressModeClampToZero](../mtlsampleraddressmode/clamptozero.md) address mode.
- The [MTLSamplerMipFilterNotMipmapped](../mtlsamplermipfilter/notmipmapped.md) mipmap filtering option.
- [minFilter](minfilter.md) and [magFilter](magfilter.md) need to be equal to each other.
- [maxAnisotropy](maxanisotropy.md) needs to be `1`.
