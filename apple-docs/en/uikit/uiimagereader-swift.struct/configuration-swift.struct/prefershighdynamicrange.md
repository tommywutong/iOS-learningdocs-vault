---
title: prefersHighDynamicRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/prefershighdynamicrange
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/prefershighdynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct/prefershighdynamicrange.json'
content_hash: 'sha256:9a4965e92a6c3cdb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImageReader](../../uiimagereader-swift.struct.md) · [Configuration](../configuration-swift.struct.md)

# prefersHighDynamicRange

<sub>Instance Property</sub>

A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var prefersHighDynamicRange: Bool { get set }
```

## Discussion

This property doesn’t affect images that only decode in either SDR or HDR. The default value depends on the system capabilities.

## See Also

### Related Documentation

- [Applying Apple HDR effect to your photos](../../../appkit/applying-apple-hdr-effect-to-your-photos.md) — You can decode and apply Apple’s HDR gain map to your own images.

### Configuration properties

- [preparesImagesForDisplay](preparesimagesfordisplay.md) — A Boolean value that indicates whether the image reader prepares the image for display.
- [preferredThumbnailSize](preferredthumbnailsize.md) — The thumbnail size in pixels that the image reader makes the image.
- [pixelsPerInch](pixelsperinch.md) — The integral scale that the image reader applies to the image.
