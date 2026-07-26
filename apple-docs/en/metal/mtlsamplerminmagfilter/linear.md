---
title: MTLSamplerMinMagFilter.linear
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerminmagfilter/linear
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter/linear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerminmagfilter/linear.json'
content_hash: 'sha256:ffaadfb70461e776'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerMinMagFilter](../mtlsamplerminmagfilter.md)

# MTLSamplerMinMagFilter.linear

<sub>Case</sub>

Select two pixels in each dimension and interpolate linearly between them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case linear
```

## Discussion

Support for linear filtering varies by GPU and the format of the texture being sampled. For example, you can’t use linear filtering on textures with an integer format, and only some device objects support linear filtering for textures with a floating-point format. To determine whether linear filtering is available for a specific texture format, see:

- [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal feature set tables (Numbers)](https://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

### Filter options

- [MTLSamplerMinMagFilterNearest](nearest.md) — Select the single pixel nearest to the sample point.
