---
title: preferredThumbnailSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereaderconfiguration/preferredthumbnailsize
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereaderconfiguration/preferredthumbnailsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereaderconfiguration/preferredthumbnailsize.json'
content_hash: 'sha256:f809070f0ebc96ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageReaderConfiguration](../uiimagereaderconfiguration.md)

# preferredThumbnailSize

<sub>Instance Property</sub>

The thumbnail size in pixels that the image reader makes the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) CGSize preferredThumbnailSize;
```

## Discussion

The default value is [CGSizeZero](../../coregraphics/cgsizezero.md).

## See Also

### Configuration properties

- [prefersHighDynamicRange](prefershighdynamicrange.md) — A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preparesImagesForDisplay](preparesimagesfordisplay.md) — A Boolean value that indicates whether the image reader prepares the image for display.
- [pixelsPerInch](pixelsperinch.md) — The integral scale that the image reader applies to the image.
