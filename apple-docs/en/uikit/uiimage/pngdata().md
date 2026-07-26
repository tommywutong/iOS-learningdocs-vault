---
title: pngData()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/pngdata()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/pngdata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/pngdata%28%29.json'
content_hash: 'sha256:0718c1188a9db4ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# pngData()

<sub>Instance Method</sub>

Returns a data object that contains the specified image in PNG format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func pngData() -> Data?
```

## Return Value

A data object containing the PNG data, or `nil` if there was a problem generating the data. This function may return `nil` if the image has no data or if the underlying `CGImageRef` contains data in an unsupported bitmap format.

## Discussion

If the image object’s underlying image data has been purged, calling this function forces that data to be reloaded into memory.

## See Also

### Image creation

- [Supporting HDR images in your app](../supporting-hdr-images-in-your-app.md) — ​ Load, display, edit, and save HDR images using SwiftUI and Core Image. ​
- [UIImageJPEGRepresentation](<jpegdata(compressionquality_).md>) — Returns a data object that contains the image in JPEG format.
