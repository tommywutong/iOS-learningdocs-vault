---
title: 'jpegData(compressionQuality:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/jpegdata(compressionquality:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/jpegdata(compressionquality:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/jpegdata%28compressionquality%3A%29.json'
content_hash: 'sha256:fbf34836b06f10c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# jpegData(compressionQuality:)

<sub>Instance Method</sub>

Returns a data object that contains the image in JPEG format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func jpegData(compressionQuality: CGFloat) -> Data?
```

## Parameters

- `compressionQuality` — The quality of the resulting JPEG image, expressed as a value from `0.0` to `1.0`. The value `0.0` represents the maximum compression (or lowest quality) while the value `1.0` represents the least compression (or best quality).

## Return Value

A data object containing the JPEG data, or `nil` if there’s a problem generating the data. This function may return `nil` if the image has no data or if the underlying `CGImageRef` contains data in an unsupported bitmap format.

## Discussion

If the image object’s underlying image data has been purged, calling this function forces that data to be reloaded into memory.

## See Also

### Image creation

- [Supporting HDR images in your app](../supporting-hdr-images-in-your-app.md) — ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [UIImagePNGRepresentation](<pngdata().md>) — Returns a data object that contains the specified image in PNG format.
