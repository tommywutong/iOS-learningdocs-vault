---
title: kCISamplerWrapMode
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kcisamplerwrapmode
source_url: 'https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kcisamplerwrapmode.json'
content_hash: 'sha256:94330e4cdd077044'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCISamplerWrapMode

<sub>Global Variable</sub>

The key for the sampler wrap mode. The wrap mode specifies how Core Image produces pixels that are outside the extent of the sample. Possible values are [kCISamplerWrapBlack](kcisamplerwrapblack.md) and [kCISamplerWrapClamp](kcisamplerwrapclamp.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCISamplerWrapMode: String
```

## See Also

### Constants

- [kCISamplerAffineMatrix](kcisampleraffinematrix.md) — The key for an affine matrix. The associated value is an `NSArray` object ([_a b c d tx ty_]) that defines the transformation to apply to the sampler.
- [kCISamplerFilterMode](kcisamplerfiltermode.md) — The key for the filtering to use when sampling the image. Possible values are [kCISamplerFilterNearest](kcisamplerfilternearest.md) and [kCISamplerFilterLinear](kcisamplerfilterlinear.md).
- [kCISamplerColorSpace](kcisamplercolorspace.md) — The key for the color space to use when sampling the image.
