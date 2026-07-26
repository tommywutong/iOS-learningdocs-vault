---
title: Sampler Option Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/sampler-option-keys
source_url: 'https://developer.apple.com/documentation/coreimage/sampler-option-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/sampler-option-keys.json'
content_hash: 'sha256:b602e9eaebbcf1ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CISampler](cisampler.md)

# Sampler Option Keys

<sub>API Collection</sub>

Keys for creating a sampler.

## Topics

### Constants

- [kCISamplerAffineMatrix](kcisampleraffinematrix.md) — The key for an affine matrix. The associated value is an `NSArray` object ([_a b c d tx ty_]) that defines the transformation to apply to the sampler.
- [kCISamplerWrapMode](kcisamplerwrapmode.md) — The key for the sampler wrap mode. The wrap mode specifies how Core Image produces pixels that are outside the extent of the sample. Possible values are [kCISamplerWrapBlack](kcisamplerwrapblack.md) and [kCISamplerWrapClamp](kcisamplerwrapclamp.md).
- [kCISamplerFilterMode](kcisamplerfiltermode.md) — The key for the filtering to use when sampling the image. Possible values are [kCISamplerFilterNearest](kcisamplerfilternearest.md) and [kCISamplerFilterLinear](kcisamplerfilterlinear.md).
- [kCISamplerColorSpace](kcisamplercolorspace.md) — The key for the color space to use when sampling the image.

## See Also

### Constants

- [Sampler Option Values](sampler-option-values.md) — Values for sampler option keys.
