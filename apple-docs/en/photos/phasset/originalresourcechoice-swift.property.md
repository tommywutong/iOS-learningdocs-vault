---
title: originalResourceChoice
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phasset/originalresourcechoice-swift.property
source_url: 'https://developer.apple.com/documentation/photos/phasset/originalresourcechoice-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/originalresourcechoice-swift.property.json'
content_hash: 'sha256:3e4498d56f76ba93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# originalResourceChoice

<sub>Instance Property</sub>

The original resource used as the basis for rendering this asset’s derivatives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var originalResourceChoice: PHAsset.OriginalResourceChoice { get }
```

## Discussion

This value is only meaningful for assets that have a RAW alternate, such as RAW+JPEG assets, where it indicates whether the RAW or the compressed resource serves as the unadjusted base. For all other assets the value is [PHOriginalResourceChoiceCompressed](originalresourcechoice-swift.enum/compressed.md).
