---
title: preferredThumbnailSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preferredthumbnailsize
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preferredthumbnailsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preferredthumbnailsize.json'
content_hash: 'sha256:610c27a63535fba8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImageReader](../../uiimagereader-swift.struct.md) · [Configuration](../configuration-swift.struct.md)

# preferredThumbnailSize

<sub>Instance Property</sub>

The thumbnail size in pixels that the image reader makes the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var preferredThumbnailSize: CGSize { get set }
```

## Discussion

The default value is [CGSizeZero](../../../coregraphics/cgsizezero.md).

## See Also

### Configuration properties

- [prefersHighDynamicRange](prefershighdynamicrange.md) — A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preparesImagesForDisplay](preparesimagesfordisplay.md) — A Boolean value that indicates whether the image reader prepares the image for display.
- [pixelsPerInch](pixelsperinch.md) — The integral scale that the image reader applies to the image.
