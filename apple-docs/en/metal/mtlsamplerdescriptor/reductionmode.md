---
title: reductionMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/reductionmode
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/reductionmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/reductionmode.json'
content_hash: 'sha256:a64b4eb584f931de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# reductionMode

<sub>Instance Property</sub>

Sets the reduction mode for filtering contributing samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var reductionMode: MTLSamplerReductionMode { get set }
```

## Discussion

The property’s default value is `MTLSamplerReductionModeWeightedAverage`. The sampler ignores this property if any of the following property values are equal to a specific value:

- The sampler’s [mipFilter](mipfilter.md) property is equal to `MTLSamplerMipFilterNotMipmapped`.
- The sampler’s [mipFilter](mipfilter.md) property is equal to `MTLSamplerMipFilterNearest`.
- The sampler’s [minFilter](minfilter.md) property is equal to `MTLSamplerMinMagFilterNearest`.
- The sampler’s [magFilter](magfilter.md) property is equal to `MTLSamplerMinMagFilterNearest`.
