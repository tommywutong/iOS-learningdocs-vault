---
title: MTLSamplerMipFilter.linear
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplermipfilter/linear
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplermipfilter/linear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplermipfilter/linear.json'
content_hash: 'sha256:00224aa4cf5865c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerMipFilter](../mtlsamplermipfilter.md)

# MTLSamplerMipFilter.linear

<sub>Case</sub>

If the filter falls between mipmap levels, both levels are sampled and the results are determined by linear interpolation between levels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case linear
```

## Discussion

Support for linear filtering between mipmaps varies by GPU and the format of the texture being sampled. For example, you can’t use linear filtering on textures with an integer format, and only some device objects support linear filtering for textures with a floating-point format. To determine whether linear filtering is available for a specific texture format, see:

- [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal feature set tables (Numbers)](https://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

### Specifying mip filter options

- [MTLSamplerMipFilterNotMipmapped](notmipmapped.md) — The texture is sampled from mipmap level `0`, and other mipmap levels are ignored.
- [MTLSamplerMipFilterNearest](nearest.md) — The nearest mipmap level is selected.
