---
title: kCISamplerColorSpace
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kcisamplercolorspace
source_url: 'https://developer.apple.com/documentation/coreimage/kcisamplercolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kcisamplercolorspace.json'
content_hash: 'sha256:9e8b66a521f1791f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCISamplerColorSpace

<sub>Global Variable</sub>

The key for the color space to use when sampling the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCISamplerColorSpace: String
```

## Discussion

The associated value must be an RGB [CGColorSpace](../coregraphics/cgcolorspace.md) object. Using this option specifies that samples should be converted to this color space before being passed to a kernel. If not specified, samples will be passed to the kernel in the working color space of the Core Image context used to render the image.

## See Also

### Constants

- [kCISamplerAffineMatrix](kcisampleraffinematrix.md) — The key for an affine matrix. The associated value is an `NSArray` object ([_a b c d tx ty_]) that defines the transformation to apply to the sampler.
- [kCISamplerWrapMode](kcisamplerwrapmode.md) — The key for the sampler wrap mode. The wrap mode specifies how Core Image produces pixels that are outside the extent of the sample. Possible values are [kCISamplerWrapBlack](kcisamplerwrapblack.md) and [kCISamplerWrapClamp](kcisamplerwrapclamp.md).
- [kCISamplerFilterMode](kcisamplerfiltermode.md) — The key for the filtering to use when sampling the image. Possible values are [kCISamplerFilterNearest](kcisamplerfilternearest.md) and [kCISamplerFilterLinear](kcisamplerfilterlinear.md).
