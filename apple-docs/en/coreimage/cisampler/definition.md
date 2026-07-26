---
title: definition
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisampler/definition
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/definition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/definition.json'
content_hash: 'sha256:e0cae2ef4f2a118b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# definition

<sub>Instance Property</sub>

The domain of definition (DOD) of the sampler

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var definition: CIFilterShape { get }
```

## Discussion

The DOD contains all nontransparent pixels produced by referencing the sampler.

## See Also

### Getting Information About the Sampler Object

- [extent](extent.md) — The rectangle that specifies the extent of the sampler
