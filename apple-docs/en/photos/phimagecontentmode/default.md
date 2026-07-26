---
title: default
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagecontentmode/default
source_url: 'https://developer.apple.com/documentation/photos/phimagecontentmode/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagecontentmode/default.json'
content_hash: 'sha256:bd218b98f21bda5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageContentMode](../phimagecontentmode.md)

# default

<sub>Type Property</sub>

Fits the image to the requested size using the default option, [PHImageContentModeAspectFit](aspectfit.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var `default`: PHImageContentMode { get }
```

## Discussion

Use this content mode when requesting a full-sized image using the [PHImageManagerMaximumSize](../phimagemanagermaximumsize.md) value for the target size. In this case, the image manager does not scale or crop the image.

## See Also

### Constants

- [PHImageContentModeAspectFit](aspectfit.md) — Scales the image so that its larger dimension fits the target size.
- [PHImageContentModeAspectFill](aspectfill.md) — Scales the image so that it completely fills the target size.
