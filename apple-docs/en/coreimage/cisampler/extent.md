---
title: extent
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisampler/extent
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/extent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/extent.json'
content_hash: 'sha256:4d717b01a848d504'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# extent

<sub>Instance Property</sub>

The rectangle that specifies the extent of the sampler

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extent: CGRect { get }
```

## Discussion

Extent is the rectangle that specifies the area outside which the wrap mode set for the sampler is invoked.

## See Also

### Getting Information About the Sampler Object

- [definition](definition.md) — The domain of definition (DOD) of the sampler
