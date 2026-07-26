---
title: preparesImagesForDisplay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preparesimagesfordisplay
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preparesimagesfordisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/preparesimagesfordisplay.json'
content_hash: 'sha256:f5adb326c9a2bf58'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImageReader](../../uiimagereader-swift.struct.md) · [Configuration](../configuration-swift.struct.md)

# preparesImagesForDisplay

<sub>Instance Property</sub>

A Boolean value that indicates whether the image reader prepares the image for display.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var preparesImagesForDisplay: Bool { get set }
```

## Discussion

The default value is [false](../../../swift/false.md).

## See Also

### Configuration properties

- [prefersHighDynamicRange](prefershighdynamicrange.md) — A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preferredThumbnailSize](preferredthumbnailsize.md) — The thumbnail size in pixels that the image reader makes the image.
- [pixelsPerInch](pixelsperinch.md) — The integral scale that the image reader applies to the image.
