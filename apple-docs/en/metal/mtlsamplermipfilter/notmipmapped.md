---
title: MTLSamplerMipFilter.notMipmapped
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplermipfilter/notmipmapped
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplermipfilter/notmipmapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplermipfilter/notmipmapped.json'
content_hash: 'sha256:f3b080953562ea00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerMipFilter](../mtlsamplermipfilter.md)

# MTLSamplerMipFilter.notMipmapped

<sub>Case</sub>

The texture is sampled from mipmap level `0`, and other mipmap levels are ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case notMipmapped
```

## See Also

### Specifying mip filter options

- [MTLSamplerMipFilterNearest](nearest.md) — The nearest mipmap level is selected.
- [MTLSamplerMipFilterLinear](linear.md) — If the filter falls between mipmap levels, both levels are sampled and the results are determined by linear interpolation between levels.
