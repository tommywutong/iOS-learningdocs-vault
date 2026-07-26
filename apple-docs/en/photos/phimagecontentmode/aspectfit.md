---
title: PHImageContentMode.aspectFit
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagecontentmode/aspectfit
source_url: 'https://developer.apple.com/documentation/photos/phimagecontentmode/aspectfit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagecontentmode/aspectfit.json'
content_hash: 'sha256:6daa9dec7798d122'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageContentMode](../phimagecontentmode.md)

# PHImageContentMode.aspectFit

<sub>Case</sub>

Scales the image so that its larger dimension fits the target size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case aspectFit
```

## Discussion

Use this option when you want the entire image to be visible, such as when presenting it in a view with the [UIView.ContentMode.scaleAspectFit](../../uikit/uiview/contentmode-swift.enum/scaleaspectfit.md) content mode.

## See Also

### Constants

- [PHImageContentModeDefault](default.md) — Fits the image to the requested size using the default option, [PHImageContentModeAspectFit](aspectfit.md).
- [PHImageContentModeAspectFill](aspectfill.md) — Scales the image so that it completely fills the target size.
