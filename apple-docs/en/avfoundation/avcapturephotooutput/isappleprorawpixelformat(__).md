---
title: 'isAppleProRAWPixelFormat(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.3+, iPadOS 14.3+, Mac Catalyst 14.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotooutput/isappleprorawpixelformat(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawpixelformat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isappleprorawpixelformat%28_%3A%29.json'
content_hash: 'sha256:0c0735637f1c274b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isAppleProRAWPixelFormat(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func isAppleProRAWPixelFormat(_ pixelFormat: OSType) -> Bool
```

## Parameters

- `pixelFormat` — The pixel format to query.

## Return Value

[true](../../swift/true.md) if the pixel format is an Apple ProRAW format, otherwise [false](../../swift/false.md).

## See Also

### Determining supported pixel formats

- [availablePhotoPixelFormatTypes](availablephotopixelformattypes-3ydgm.md) — The pixel formats the capture output supports for photo capture.
- [availableRawPhotoPixelFormatTypes](availablerawphotopixelformattypes-9t9k5.md) — The pixel formats the capture output supports for RAW photo capture.
- [supportedPhotoPixelFormatTypes(for:)](<supportedphotopixelformattypes(for_).md>) — Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [supportedRawPhotoPixelFormatTypes(for:)](<supportedrawphotopixelformattypes(for_).md>) — Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [+ isBayerRAWPixelFormat:](<isbayerrawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.
