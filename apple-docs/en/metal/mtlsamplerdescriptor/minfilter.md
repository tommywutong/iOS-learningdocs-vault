---
title: minFilter
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/minfilter
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/minfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/minfilter.json'
content_hash: 'sha256:2a8ffc570d77aae9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# minFilter

<sub>Instance Property</sub>

The filtering option for combining pixels within one mipmap level when the sample footprint is larger than a pixel (minification).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minFilter: MTLSamplerMinMagFilter { get set }
```

## Discussion

The default value is [MTLSamplerMinMagFilterNearest](../mtlsamplerminmagfilter/nearest.md).

## See Also

### Declaring filter modes

- [magFilter](magfilter.md) — The filtering operation for combining pixels within one mipmap level when the sample footprint is smaller than a pixel (magnification).
- [mipFilter](mipfilter.md) — The filtering option for combining pixels between two mipmap levels.
- [lodMinClamp](lodminclamp.md) — The minimum level of detail (LOD) to use when sampling from a texture.
- [lodMaxClamp](lodmaxclamp.md) — The maximum level of detail (LOD) to use when sampling from a texture.
- [lodAverage](lodaverage.md) — A Boolean value that specifies whether the GPU can use an average level of detail (LOD) when sampling from a texture.
- [maxAnisotropy](maxanisotropy.md) — The number of samples that can be taken to improve the quality of sample footprints that are anisotropic.
- [MTLSamplerMinMagFilter](../mtlsamplerminmagfilter.md) — Filtering options for determining which pixel value is returned within a mipmap level.
- [MTLSamplerMipFilter](../mtlsamplermipfilter.md) — Filtering options for determining what pixel value is returned with multiple mipmap levels.
