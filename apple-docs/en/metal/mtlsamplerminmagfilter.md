---
title: MTLSamplerMinMagFilter
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerminmagfilter
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerminmagfilter.json'
content_hash: 'sha256:ddf93e300de1c813'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSamplerMinMagFilter

<sub>Enumeration</sub>

Filtering options for determining which pixel value is returned within a mipmap level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLSamplerMinMagFilter
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Filter options

- [MTLSamplerMinMagFilterNearest](mtlsamplerminmagfilter/nearest.md) — Select the single pixel nearest to the sample point.
- [MTLSamplerMinMagFilterLinear](mtlsamplerminmagfilter/linear.md) — Select two pixels in each dimension and interpolate linearly between them.

### Initializers

- [init(rawValue:)](<mtlsamplerminmagfilter/init(rawvalue_).md>)

## See Also

### Declaring filter modes

- [minFilter](mtlsamplerdescriptor/minfilter.md) — The filtering option for combining pixels within one mipmap level when the sample footprint is larger than a pixel (minification).
- [magFilter](mtlsamplerdescriptor/magfilter.md) — The filtering operation for combining pixels within one mipmap level when the sample footprint is smaller than a pixel (magnification).
- [mipFilter](mtlsamplerdescriptor/mipfilter.md) — The filtering option for combining pixels between two mipmap levels.
- [lodMinClamp](mtlsamplerdescriptor/lodminclamp.md) — The minimum level of detail (LOD) to use when sampling from a texture.
- [lodMaxClamp](mtlsamplerdescriptor/lodmaxclamp.md) — The maximum level of detail (LOD) to use when sampling from a texture.
- [lodAverage](mtlsamplerdescriptor/lodaverage.md) — A Boolean value that specifies whether the GPU can use an average level of detail (LOD) when sampling from a texture.
- [maxAnisotropy](mtlsamplerdescriptor/maxanisotropy.md) — The number of samples that can be taken to improve the quality of sample footprints that are anisotropic.
- [MTLSamplerMipFilter](mtlsamplermipfilter.md) — Filtering options for determining what pixel value is returned with multiple mipmap levels.
