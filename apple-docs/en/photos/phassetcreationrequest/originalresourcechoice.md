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
doc_path: /documentation/photos/phassetcreationrequest/originalresourcechoice
source_url: 'https://developer.apple.com/documentation/photos/phassetcreationrequest/originalresourcechoice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcreationrequest/originalresourcechoice.json'
content_hash: 'sha256:bdc087bd25b44f6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCreationRequest](../phassetcreationrequest.md)

# originalResourceChoice

<sub>Instance Property</sub>

The original resource to use as the unadjusted base for rendering derivatives of the new asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var originalResourceChoice: PHAsset.OriginalResourceChoice { get set }
```

## Discussion

This property applies to RAW+JPEG assets only, where it selects whether the RAW or the compressed resource serves as the original. Setting it on assets that have only a single original resource is an error.
