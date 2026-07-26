---
title: PHImageContentMode.aspectFill
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagecontentmode/aspectfill
source_url: 'https://developer.apple.com/documentation/photos/phimagecontentmode/aspectfill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagecontentmode/aspectfill.json'
content_hash: 'sha256:696aba71dd01847d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageContentMode](../phimagecontentmode.md)

# PHImageContentMode.aspectFill

<sub>Case</sub>

Scales the image so that it completely fills the target size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case aspectFill
```

## Discussion

Use this option when you want the image to completely fill an area, such as when presenting it in a view with the [UIView.ContentMode.scaleAspectFill](../../uikit/uiview/contentmode-swift.enum/scaleaspectfill.md) content mode.

## See Also

### Constants

- [PHImageContentModeDefault](default.md) — Fits the image to the requested size using the default option, [PHImageContentModeAspectFit](aspectfit.md).
- [PHImageContentModeAspectFit](aspectfit.md) — Scales the image so that its larger dimension fits the target size.
