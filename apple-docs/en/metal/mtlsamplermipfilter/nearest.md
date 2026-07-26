---
title: MTLSamplerMipFilter.nearest
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplermipfilter/nearest
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplermipfilter/nearest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplermipfilter/nearest.json'
content_hash: 'sha256:1126384cb09c34b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerMipFilter](../mtlsamplermipfilter.md)

# MTLSamplerMipFilter.nearest

<sub>Case</sub>

The nearest mipmap level is selected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case nearest
```

## See Also

### Specifying mip filter options

- [MTLSamplerMipFilterNotMipmapped](notmipmapped.md) — The texture is sampled from mipmap level `0`, and other mipmap levels are ignored.
- [MTLSamplerMipFilterLinear](linear.md) — If the filter falls between mipmap levels, both levels are sampled and the results are determined by linear interpolation between levels.
