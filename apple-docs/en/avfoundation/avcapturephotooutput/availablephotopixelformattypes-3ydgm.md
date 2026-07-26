---
title: availablePhotoPixelFormatTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablephotopixelformattypes-3ydgm
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotopixelformattypes-3ydgm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablephotopixelformattypes-3ydgm.json'
content_hash: 'sha256:436ace4307ed9fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availablePhotoPixelFormatTypes

<sub>Instance Property</sub>

The pixel formats the capture output supports for photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var availablePhotoPixelFormatTypes: [OSType] { get }
```

## Discussion

To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, use the [+ photoSettingsWithFormat:](<../avcapturephotosettings/init(format_).md>) initializer to create your photo settings object. In that initializer’s `format` dictionary, pass the key [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md), whose value must be one of the pixel format identifiers listed in this array.

> [!note] Note
> Read this property only after adding the photo capture output to an [AVCaptureSession](../avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.

This property supports key-value observing.

## See Also

### Determining supported pixel formats

- [availableRawPhotoPixelFormatTypes](availablerawphotopixelformattypes-9t9k5.md) — The pixel formats the capture output supports for RAW photo capture.
- [supportedPhotoPixelFormatTypes(for:)](<supportedphotopixelformattypes(for_).md>) — Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [supportedRawPhotoPixelFormatTypes(for:)](<supportedrawphotopixelformattypes(for_).md>) — Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [+ isAppleProRAWPixelFormat:](<isappleprorawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [+ isBayerRAWPixelFormat:](<isbayerrawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.
